import os
import io
import base64
import random
from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageChops, ImageDraw

app = Flask(__name__)

# Style presets definitions
STYLE_PRESETS = {
    "ccd": {
        "contrast": 1.15,
        "brightness": 1.05,
        "saturation": 0.95,
        "r_shift": -5,
        "g_shift": -8,
        "b_shift": 15,
        "pixelate": True,
        "bloom": False,
        "vignette_strength": 0.15
    },
    "leica": {
        "contrast": 1.28,
        "brightness": 0.95,
        "saturation": 0.85,
        "r_shift": -3,
        "g_shift": 4,
        "b_shift": 2,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.22
    },
    "portra": {
        "contrast": 0.92,
        "brightness": 1.05,
        "saturation": 0.92,
        "r_shift": 12,
        "g_shift": 4,
        "b_shift": -10,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.0
    },
    "iphone": {
        "contrast": 0.98,
        "brightness": 1.06,
        "saturation": 1.05,
        "r_shift": 0,
        "g_shift": 0,
        "b_shift": 0,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.0
    },
    "samsung": {
        "contrast": 1.12,
        "brightness": 1.02,
        "saturation": 1.25,
        "r_shift": -2,
        "g_shift": 6,
        "b_shift": 4,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.0
    },
    "insta360": {
        "contrast": 1.10,
        "brightness": 1.04,
        "saturation": 1.15,
        "r_shift": -2,
        "g_shift": 4,
        "b_shift": 4,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.0,
        "barrel_distort": 50
    },
    "korean": {
        "contrast": 0.82,
        "brightness": 1.15,
        "saturation": 0.90,
        "r_shift": 8,
        "g_shift": -2,
        "b_shift": 4,
        "pixelate": False,
        "bloom": True,
        "bloom_radius": 18,
        "bloom_opacity": 0.40,
        "vignette_strength": 0.0
    },
    "xhs": {
        "contrast": 0.92,
        "brightness": 1.06,
        "saturation": 0.92,
        "r_shift": 12,
        "g_shift": 6,
        "b_shift": -12,
        "pixelate": False,
        "bloom": True,
        "bloom_radius": 10,
        "bloom_opacity": 0.25,
        "vignette_strength": 0.0
    },
    "dslr": {
        "contrast": 1.02,
        "brightness": 1.00,
        "saturation": 1.00,
        "r_shift": 0,
        "g_shift": 0,
        "b_shift": 0,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.0
    },
    "tokyo": {
        "contrast": 1.18,
        "brightness": 0.98,
        "saturation": 0.92,
        "split_toning": True,
        "shadow_r": -10, "shadow_g": 5, "shadow_b": 15,     # Cyan shadows
        "highlight_r": 10, "highlight_g": 5, "highlight_b": -10, # Warm highlights
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.18
    },
    "fuji": {
        "contrast": 1.15,
        "brightness": 0.98,
        "saturation": 0.76,
        "r_shift": -8,
        "g_shift": 8,
        "b_shift": -4,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.0
    },
    "gold": {
        "contrast": 1.02,
        "brightness": 1.00,
        "saturation": 1.06,
        "r_shift": 14,
        "g_shift": 6,
        "b_shift": -20,
        "pixelate": False,
        "bloom": False,
        "vignette_strength": 0.0
    },
    "cinestill": {
        "contrast": 1.15,
        "brightness": 0.95,
        "saturation": 0.98,
        "r_shift": -18,
        "g_shift": 6,
        "b_shift": 22,
        "pixelate": False,
        "bloom": False,
        "cinestill_halation": True,
        "vignette_strength": 0.15
    },
    "disposable": {
        "contrast": 1.22,
        "brightness": 0.98,
        "saturation": 0.85,
        "r_shift": 10,
        "g_shift": 12,
        "b_shift": -15,
        "pixelate": True,
        "bloom": False,
        "vignette_strength": 0.28
    }
}

# Image Processing Helpers
def apply_color_grade(img, r_shift, g_shift, b_shift):
    """Apply smooth photographic color grading using non-linear channel LUTs."""
    if r_shift == 0 and g_shift == 0 and b_shift == 0:
        return img
    r, g, b = img.split()
    
    def get_lut(shift):
        # Shift midtones while keeping shadows (0) and highlights (255) anchored
        factor = shift / 100.0
        return [min(255, max(0, int(p + 128 * factor * (1.0 - abs(p - 128) / 128.0)))) for p in range(256)]
        
    r = r.point(get_lut(r_shift))
    g = g.point(get_lut(g_shift))
    b = b.point(get_lut(b_shift))
    return Image.merge("RGB", (r, g, b))

def apply_split_toning(img, shadow_r, shadow_g, shadow_b, highlight_r, highlight_g, highlight_b):
    """Apply photographic split toning: shadows get cool/cyan, highlights get warm/gold."""
    r, g, b = img.split()
    
    def get_split_lut(s_shift, h_shift):
        lut = []
        for p in range(256):
            w_s = (1.0 - p/255.0) ** 2  # shadow weight
            w_h = (p/255.0) ** 2        # highlight weight
            val = p + (s_shift * w_s * 30.0) + (h_shift * w_h * 30.0)
            lut.append(min(255, max(0, int(val))))
        return lut
        
    r = r.point(get_split_lut(shadow_r, highlight_r))
    g = g.point(get_split_lut(shadow_g, highlight_g))
    b = b.point(get_split_lut(shadow_b, highlight_b))
    return Image.merge("RGB", (r, g, b))

def apply_pixelation(img):
    """Slightly lower the resolution to simulate CCD pixel texture."""
    width, height = img.size
    shrink_factor = 0.70  # More aggressive zoom texture
    small = img.resize((int(width * shrink_factor), int(height * shrink_factor)), Image.Resampling.BILINEAR)
    return small.resize((width, height), Image.Resampling.NEAREST)

def apply_vignette(img, strength):
    """Add a subtle, professional brightness falloff to the corners using multiply."""
    if strength <= 0:
        return img
    width, height = img.size
    
    # Create radial vignette mask
    grad_size = (100, 100)
    grad = Image.new("L", grad_size, 255)
    draw = ImageDraw.Draw(grad)
    cx, cy = 50, 50
    
    # Max diagonal distance
    max_d = 70.7
    for r in range(75, 0, -1):
        dist = r / max_d
        # Corners get darker by strength percentage
        val = int(255 - (255 * strength) * (dist ** 2.2))
        val = min(255, max(0, val))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=val)
        
    mask = grad.resize((width, height), Image.Resampling.BILINEAR)
    mask_rgb = Image.merge("RGB", (mask, mask, mask))
    
    # Multiply exposure changes
    return ImageChops.multiply(img, mask_rgb)

def apply_bloom(img, radius=12, opacity=0.3):
    """Apply soft light glow bloom to highlights."""
    blurred = img.filter(ImageFilter.GaussianBlur(radius))
    screen_blend = ImageChops.screen(img, blurred)
    return Image.blend(img, screen_blend, opacity)

def apply_cinestill_halation(img, radius=15, opacity=0.5):
    """Simulate Cinestill red halation glow around bright highlights."""
    # Extract bright highlights (luminance > 200)
    luminance = img.convert("L")
    mask = luminance.point(lambda p: 255 if p > 200 else 0)
    
    # Create a solid warm red-orange halation color layer
    red_layer = Image.new("RGB", img.size, (255, 55, 15))
    red_highlights = Image.composite(red_layer, Image.new("RGB", img.size, (0, 0, 0)), mask)
    
    # Blur the red highlights to bleed outwards
    blurred_red = red_highlights.filter(ImageFilter.GaussianBlur(radius))
    
    # Blend back onto image using screen mode
    return Image.blend(img, ImageChops.screen(img, blurred_red), opacity)

def apply_barrel_distortion(img, strength):
    """Barrel distortion simulation using grid mesh transform."""
    if strength <= 0:
        return img
    width, height = img.size
    grid_size = 12
    w_step = width / grid_size
    h_step = height / grid_size
    
    mesh = []
    k = strength * 0.0022
    
    center_x = width / 2.0
    center_y = height / 2.0
    max_r = (center_x**2 + center_y**2) ** 0.5
    
    def distort_point(px, py):
        dx = px - center_x
        dy = py - center_y
        r = (dx**2 + dy**2) ** 0.5
        if r == 0:
            return px, py
        factor = 1.0 - k * ((r / max_r) ** 2)
        return center_x + dx * factor, center_y + dy * factor

    for i in range(grid_size):
        for j in range(grid_size):
            x0 = i * w_step
            y0 = j * h_step
            x1 = x0 + w_step
            y1 = y0 + h_step
            
            sx0, sy0 = distort_point(x0, y0)
            sx1, sy1 = distort_point(x0, y1)
            sx2, sy2 = distort_point(x1, y1)
            sx3, sy3 = distort_point(x1, y0)
            
            mesh.append(((int(x0), int(y0), int(x1), int(y1)), 
                          (sx0, sy0, sx1, sy1, sx2, sy2, sx3, sy3)))
            
    return img.transform(img.size, Image.MESH, mesh, Image.Resampling.BILINEAR)

def apply_dof(img, dof_strength):
    """Depth of field blur using radial focus mask."""
    if dof_strength <= 0:
        return img
    width, height = img.size
    
    radius = (dof_strength / 100.0) * 12.0
    blurred = img.filter(ImageFilter.GaussianBlur(radius))
    
    grad_size = (120, 120)
    grad = Image.new("L", grad_size, 0)
    draw = ImageDraw.Draw(grad)
    cx, cy = 60, 60
    
    inner_rad = 0.12
    outer_rad = 0.65
    
    for r in range(60, 0, -1):
        dist = r / 60.0
        if dist <= inner_rad:
            val = 255
        elif dist >= outer_rad:
            val = 0
        else:
            val = int(255 * (1.0 - (dist - inner_rad) / (outer_rad - inner_rad)))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=val)
        
    draw.ellipse([cx - int(60*inner_rad), cy - int(60*inner_rad), 
                  cx + int(60*inner_rad), cy + int(60*inner_rad)], fill=255)
                  
    mask = grad.resize((width, height), Image.Resampling.BILINEAR)
    return Image.composite(img, blurred, mask)

def apply_flash_render(img, flash_strength):
    """Direct flash simulation: bright center, dark vignette."""
    if flash_strength <= 0:
        return img
    width, height = img.size
    
    grad_size = (100, 100)
    grad = Image.new("L", grad_size, 0)
    draw = ImageDraw.Draw(grad)
    cx, cy = 50, 50
    for r in range(75, 0, -1):
        dist = r / 70.7
        val = int(255 * (1.0 - dist ** 1.6))
        val = min(255, max(0, val))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=val)
        
    flash_mask = grad.resize((width, height), Image.Resampling.BILINEAR)
    
    # Brighten center
    bright_factor = 1.0 + (flash_strength / 100.0) * 0.25
    bright_img = ImageEnhance.Brightness(img).enhance(bright_factor)
    
    # Darken corners
    dark_factor = 1.0 - (flash_strength / 100.0) * 0.22
    dark_img = ImageEnhance.Brightness(img).enhance(dark_factor)
    
    return Image.composite(bright_img, dark_img, flash_mask)

def apply_hdr(img, hdr_strength):
    """Lift shadows and boost local contrast."""
    if hdr_strength <= 0:
        return img
    
    factor = (hdr_strength / 100.0) * 0.30
    lut = [int(p + (255 - p) * factor * (1.0 - p/255.0)) for p in range(256)]
    shadow_lifted = img.point(lut * 3)
    
    contrast_factor = 1.0 + (hdr_strength / 100.0) * 0.12
    hdr_img = ImageEnhance.Contrast(shadow_lifted).enhance(contrast_factor)
    
    return Image.blend(img, hdr_img, 0.75)

def apply_grain(img, grain_strength):
    """Apply film grain noise overlay."""
    if grain_strength <= 0:
        return img
    width, height = img.size
    
    grain_scale = 2
    n_width, n_height = width // grain_scale, height // grain_scale
    if n_width == 0 or n_height == 0:
        return img
        
    noise_img = Image.new("L", (n_width, n_height))
    pixels = [random.randint(128 - 25, 128 + 25) for _ in range(n_width * n_height)]
    noise_img.putdata(pixels)
    noise_img = noise_img.resize((width, height), Image.Resampling.BILINEAR)
    
    noise_rgb = Image.merge("RGB", (noise_img, noise_img, noise_img))
    
    blend_factor = (grain_strength / 100.0) * 0.20
    return Image.blend(img, noise_rgb, blend_factor)

def process_image(img, preset, sliders):
    """Process an image according to style preset parameters and slider overrides."""
    if img.mode != "RGB":
        img = img.convert("RGB")
        
    # Scale down to reasonable preview size (max 900px)
    max_size = 900
    img.thumbnail((max_size, max_size))
    
    # 1. Base Preset Adjustments
    # Saturation
    sat_factor = preset.get("saturation", 1.0)
    img = ImageEnhance.Color(img).enhance(sat_factor)
    
    # Contrast
    cont_factor = preset.get("contrast", 1.0)
    img = ImageEnhance.Contrast(img).enhance(cont_factor)
    
    # Brightness
    bright_factor = preset.get("brightness", 1.0)
    img = ImageEnhance.Brightness(img).enhance(bright_factor)
    
    # Non-linear Color Grading (Professional LUT shifts)
    if "split_toning" in preset:
        img = apply_split_toning(
            img, 
            preset["shadow_r"], preset["shadow_g"], preset["shadow_b"],
            preset["highlight_r"], preset["highlight_g"], preset["highlight_b"]
        )
    else:
        img = apply_color_grade(
            img, 
            preset.get("r_shift", 0), 
            preset.get("g_shift", 0), 
            preset.get("b_shift", 0)
        )
    
    # Pixelation (CCD/disposable texture)
    if preset.get("pixelate", False):
        img = apply_pixelation(img)
        
    # Bloom (Soft light glow)
    if preset.get("bloom", False):
        img = apply_bloom(img, preset.get("bloom_radius", 12), preset.get("bloom_opacity", 0.3))
        
    # Cinestill red halation glow
    if preset.get("cinestill_halation", False):
        img = apply_cinestill_halation(img)
        
    # Vignette (Subtle lighting falloff)
    if preset.get("vignette_strength", 0.0) > 0.0:
        img = apply_vignette(img, preset["vignette_strength"])
        
    # Barrel distortion (Wide action lens)
    if "barrel_distort" in preset:
        img = apply_barrel_distortion(img, preset["barrel_distort"])
        
    # 2. Sliders overrides & overlays
    original_copy = img.copy()
    
    # Apply Depth of Field
    img = apply_dof(img, sliders["dof"])
    
    # Apply Flash
    img = apply_flash_render(img, sliders["flash"])
    
    # Apply HDR shadow lift
    img = apply_hdr(img, sliders["hdr"])
    
    # Apply Sharpness
    sharpness_val = sliders["sharpness"]
    if sharpness_val != 50:
        factor = sharpness_val / 50.0
        img = ImageEnhance.Sharpness(img).enhance(factor)
        
    # Apply Grain
    img = apply_grain(img, sliders["grain"])
    
    # Final Intensity Blending (Style Strength)
    intensity_factor = sliders["intensity"] / 100.0
    final_img = Image.blend(original_copy, img, intensity_factor)
    
    # Skin tone preservation
    skin_factor = sliders["skin"] / 100.0
    if skin_factor > 0:
        final_img = Image.blend(final_img, original_copy, skin_factor * 0.22)

    return final_img

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transfer', methods=['POST'])
def api_transfer():
    try:
        file = request.files.get('image')
        if not file:
            return jsonify({"error": "No image uploaded"}), 400
            
        mix_enabled = request.form.get('mix_enabled') == 'true'
        
        sliders = {
            "intensity": int(request.form.get('intensity', 80)),
            "grain": int(request.form.get('grain', 15)),
            "dof": int(request.form.get('dof', 20)),
            "sharpness": int(request.form.get('sharpness', 50)),
            "skin": int(request.form.get('skin', 90)),
            "flash": int(request.form.get('flash', 0)),
            "hdr": int(request.form.get('hdr', 40))
        }
        
        image_bytes = file.read()
        img = Image.open(io.BytesIO(image_bytes))
        
        if mix_enabled:
            p_style = request.form.get('primary_style', 'ccd')
            s_style = request.form.get('secondary_style', 'leica')
            
            p_preset = STYLE_PRESETS.get(p_style, STYLE_PRESETS['ccd'])
            s_preset = STYLE_PRESETS.get(s_style, STYLE_PRESETS['leica'])
            
            img_p = process_image(img.copy(), p_preset, sliders)
            img_s = process_image(img.copy(), s_preset, sliders)
            
            final_img = Image.blend(img_s, img_p, 0.70)
        else:
            style_id = request.form.get('style', 'ccd')
            preset = STYLE_PRESETS.get(style_id, STYLE_PRESETS['ccd'])
            final_img = process_image(img, preset, sliders)
            
        output_buffer = io.BytesIO()
        final_img.save(output_buffer, format="PNG")
        output_buffer.seek(0)
        base64_img = base64.b64encode(output_buffer.read()).decode('utf-8')
        
        return jsonify({
            "success": True,
            "styled_image": f"data:image/png;base64,{base64_img}"
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
