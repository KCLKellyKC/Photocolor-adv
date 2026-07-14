# AI Camera Style Prompt Library

版本：1.0

## 專案目標

讓使用者只需要上傳一張照片，即可模擬不同器材拍攝出來的影像風格。

本系統不改變人物身份、服裝、場景與構圖，而是模擬不同相機系統的：

- 色彩科學（Color Science）
- 動態範圍（Dynamic Range）
- 銳利度（Sharpness）
- 景深（Depth of Field）
- 雜訊（Noise）
- 顆粒感（Grain）
- 閃光燈效果（Flash Rendering）
- 鏡頭特性（Lens Characteristics）
- 整體影像氛圍（Mood）

---

# 全域系統 Prompt

```text
You are an advanced photo style transfer engine.

Transform the uploaded image into the requested camera style.

Strictly preserve:

- facial identity
- facial features
- body proportions
- pose
- outfit
- hairstyle
- composition
- background layout
- scene content

Only modify:

- color science
- contrast
- sharpness
- dynamic range
- grain
- noise
- depth of field
- lens rendering
- flash rendering
- photographic mood

The result must look like a real photograph captured by the target camera style.

Do not:

- change facial identity
- add extra people
- add extra objects
- add text
- add logos
- add watermarks
- create illustration style
- create 3D render style
- create AI-art style
```

---

# Style 01：DSLR / Mirrorless

## 名稱

單眼高級人像

## 使用情境

- 咖啡廳
- 穿搭
- 人像
- 網拍
- 旅拍

## Prompt

```text
Professional DSLR camera photography.

Characteristics:

- natural skin tones
- realistic skin texture
- shallow depth of field
- creamy background bokeh
- precise eye focus
- realistic lens compression
- professional portrait photography
- soft natural lighting
- balanced contrast
- premium editorial photography style

Shot with a professional full-frame camera and portrait lens.

Keep the original person's identity and composition unchanged.
```

## 關鍵字

```text
dslr
mirrorless
50mm lens
85mm portrait lens
editorial photography
premium portrait
natural bokeh
professional photography
```

---

# Style 02：CCD Compact Camera

## 名稱

CCD 復古辣妹感

## 使用情境

- 夜店
- KTV
- 聚會
- 校園
- Y2K

## Prompt

```text
Early 2000s CCD compact digital camera style.

Characteristics:

- nostalgic digital camera look
- direct flash photography
- slightly overexposed highlights
- cool blue-purple tones
- visible digital noise
- sharp digital edges
- low resolution texture
- party snapshot feeling
- retro compact camera aesthetic
- candid lifestyle photography

Keep the original face and composition.

Do not add date stamps unless requested.
```

## 關鍵字

```text
ccd
y2k
retro digital camera
party snapshot
direct flash
2000s aesthetic
nostalgic camera
```

---

# Style 03：iPhone 16 Pro

## 名稱

iPhone 清透日常感

## 使用情境

- OOTD
- Instagram
- 旅遊
- 日常分享
- 咖啡廳

## Prompt

```text
Modern flagship iPhone photography style.

Characteristics:

- natural HDR
- bright but realistic exposure
- clean image quality
- accurate skin tones
- crisp details
- balanced contrast
- social-media-ready look
- natural daylight rendering
- subtle portrait mode background blur
- realistic smartphone photography

Keep the image natural and authentic.

Do not over-beautify or over-process.
```

## 關鍵字

```text
iphone
smartphone photography
natural hdr
clean aesthetic
social media photography
lifestyle photography
```

---

# Style 04：Samsung Galaxy Ultra

## 名稱

Samsung Ultra 超清夜拍感

## 使用情境

- 夜景
- 演唱會
- 城市街拍
- 旅遊
- 日常紀錄

## Prompt

```text
Samsung Galaxy Ultra flagship smartphone photography style.

Characteristics:

- ultra high detail
- sharp image rendering
- vivid colors
- strong HDR
- bright night photography
- detailed shadows
- clean low-light performance
- rich contrast
- flagship Android camera look
- AI-enhanced image processing

Preserve the original person's identity and composition.

Avoid unnatural oversharpening.
```

## 關鍵字

```text
galaxy ultra
android flagship
night photography
high detail
vivid colors
sharp smartphone image
```

---

# Style 05：Insta360

## 名稱

Insta360 廣角旅行感

## 使用情境

- 旅遊
- 機車
- 滑雪
- 登山
- Vlog

## Prompt

```text
Insta360 action camera photography style.

Characteristics:

- ultra wide angle
- immersive perspective
- dynamic composition
- slight fisheye lens effect
- vibrant colors
- travel photography mood
- action camera rendering
- outdoor lifestyle aesthetic
- strong sense of space
- energetic visual atmosphere

Keep the original person and environment.

Do not distort faces excessively.
```

## 關鍵字

```text
insta360
action camera
ultra wide angle
travel vlog
outdoor adventure
immersive photography
```

---

# Negative Prompt

所有風格共用

```text
low quality
blurry
cartoon
anime
illustration
3d render
cgi
fake skin
plastic skin
extra people
extra fingers
extra hands
deformed body
wrong anatomy
face changed
identity changed
watermark
logo
text
caption
distorted face
duplicate person
```

---

# JSON 範例

```json
{
  "style": "CCD",
  "preserve_face": true,
  "preserve_composition": true,
  "beauty_level": "natural",
  "intensity": 0.8,
  "grain": true,
  "flash": true,
  "output_ratio": "original"
}
```

---

# App Prompt 組裝範例

```text
[System Prompt]

{GLOBAL_PROMPT}

[Selected Style]

CCD Compact Camera Style

{CCD_PROMPT}

[Negative Prompt]

{NEGATIVE_PROMPT}
```

---

# Extended Style Packs

---

# Camera Collection

## Leica Q3

### 名稱

Leica 高級空氣感

### 使用情境

- 高級咖啡廳
- 旅遊
- 人像
- 時尚穿搭

### Prompt

```text
Leica photography style.

Characteristics:

- premium European aesthetic
- natural contrast
- cinematic rendering
- rich tonal depth
- elegant color transitions
- realistic skin texture
- three-dimensional subject separation
- sophisticated luxury mood
- subtle highlight rolloff
- timeless photography look

Keep the subject identity and composition unchanged.
```

### 關鍵字

```text
leica
luxury photography
premium look
cinematic
high-end portrait
editorial style
```

---

## Sony A7RV

### 名稱

Sony 超高解析感

### Prompt

```text
Sony flagship mirrorless photography style.

Characteristics:

- ultra high resolution
- highly detailed textures
- modern professional look
- crisp focus
- excellent eye sharpness
- rich dynamic range
- realistic color rendering
- commercial photography quality

Keep the photo realistic.
```

---

## Canon R5

### 名稱

Canon 柔膚人像感

### Prompt

```text
Canon professional photography style.

Characteristics:

- beautiful skin tones
- warm color science
- soft highlights
- natural portrait rendering
- wedding photography quality
- balanced contrast
- pleasing facial rendering

Keep skin realistic and natural.
```

---

## Nikon Z8

### 名稱

Nikon 真實色彩感

### Prompt

```text
Nikon professional photography style.

Characteristics:

- realistic colors
- strong micro contrast
- excellent landscape rendering
- rich shadows
- natural skin tones
- clean dynamic range

Professional photography output.
```

---

## Ricoh GR3

### 名稱

GR3 街拍感

### Prompt

```text
Ricoh GR III street photography style.

Characteristics:

- authentic street photography
- natural candid atmosphere
- urban documentary feel
- compact camera rendering
- subtle contrast
- realistic colors
- everyday life aesthetic

Maintain authenticity.
```

---

# Fujifilm Collection

## Fujifilm Classic Negative

### 名稱

富士復古街拍感

### Prompt

```text
Fujifilm Classic Negative simulation.

Characteristics:

- muted colors
- vintage contrast
- retro atmosphere
- Japanese street aesthetic
- nostalgic mood
- subtle shadows

Natural documentary feeling.
```

---

## Fujifilm Reala Ace

### 名稱

富士高級日常感

### Prompt

```text
Fujifilm Reala Ace simulation.

Characteristics:

- natural colors
- clean highlights
- elegant contrast
- lifestyle photography
- premium everyday look
- modern film aesthetic
```

---

## Fujifilm Nostalgic Neg

### 名稱

富士電影感

### Prompt

```text
Fujifilm Nostalgic Negative.

Characteristics:

- cinematic atmosphere
- warm highlights
- muted shadows
- nostalgic color palette
- elegant film rendering
```

---

# Film Collection

## Kodak Gold 200

### 名稱

夏日底片感

### Prompt

```text
Kodak Gold 200 film.

Characteristics:

- golden tones
- nostalgic summer feeling
- warm highlights
- soft grain
- vintage family-photo aesthetic

Natural analog film rendering.
```

---

## Kodak Portra 400

### 名稱

女友感底片

### Prompt

```text
Kodak Portra 400 film.

Characteristics:

- beautiful skin tones
- pastel colors
- soft contrast
- professional film photography
- elegant portrait rendering
- fine grain

Premium portrait look.
```

---

## Kodak Ultramax

### 名稱

旅行底片感

### Prompt

```text
Kodak Ultramax.

Characteristics:

- vivid colors
- travel photography mood
- cheerful atmosphere
- balanced film grain
- nostalgic outdoor feeling
```

---

## Cinestill 800T

### 名稱

夜晚電影感

### Prompt

```text
Cinestill 800T film.

Characteristics:

- cinematic night photography
- neon glow
- tungsten light rendering
- urban night atmosphere
- film grain
- movie-like mood
```

---

# Social Media Collection

## 韓國歐膩風

### 名稱

韓系女神感

### Prompt

```text
Korean influencer photography style.

Characteristics:

- bright skin tone
- soft natural light
- luxurious atmosphere
- clean composition
- premium lifestyle aesthetic
- airy mood

Natural social-media photography.
```

---

## 小紅書奶油風

### 名稱

奶油系網美感

### Prompt

```text
Xiaohongshu lifestyle photography.

Characteristics:

- creamy lighting
- bright neutral colors
- soft shadows
- luxury cafe atmosphere
- elegant lifestyle mood
- warm feminine feeling
```

---

## 東京街拍風

### 名稱

東京街頭感

### Prompt

```text
Tokyo street photography style.

Characteristics:

- urban atmosphere
- natural candid shot
- fashion editorial look
- cinematic lighting
- authentic city mood
```

---

## 香港電影風

### 名稱

港風電影感

### Prompt

```text
Hong Kong cinema photography style.

Characteristics:

- neon city lights
- cinematic contrast
- nostalgic mood
- urban storytelling
- moody colors
- retro film atmosphere
```

---

## Vogue 雜誌風

### 名稱

時尚雜誌感

### Prompt

```text
High fashion magazine photography.

Characteristics:

- editorial photography
- luxury fashion aesthetic
- professional lighting
- premium color grading
- magazine cover quality
```

---

# Retro Collection

## Disposable Camera

### 名稱

一次性底片機

### Prompt

```text
Disposable film camera style.

Characteristics:

- flash photography
- film grain
- imperfect exposure
- nostalgic atmosphere
- casual snapshot feeling
```

---

## Point and Shoot Camera

### 名稱

傻瓜相機感

### Prompt

```text
Point and shoot camera style.

Characteristics:

- casual photography
- slight flash effect
- everyday memory feeling
- authentic snapshot look
```

---

## MSN 相簿風

### 名稱

2000年代回憶感

### Prompt

```text
Early 2000s internet photo album style.

Characteristics:

- old digital camera rendering
- nostalgic colors
- casual family album feeling
- low dynamic range
- authentic memories
```

---

# Consumer-Friendly Names Mapping

| 技術名稱 | App 顯示名稱 |
|----------|------------|
| Leica | 高級空氣感 |
| Sony A7RV | 超高解析感 |
| Canon R5 | 柔膚人像感 |
| Nikon Z8 | 真實色彩感 |
| Ricoh GR3 | 街拍感 |
| Fujifilm Classic Negative | 日系復古感 |
| Reala Ace | 高級日常感 |
| Portra 400 | 女友感底片 |
| Kodak Gold | 夏日底片感 |
| Cinestill 800T | 夜晚電影感 |
| CCD | 復古辣妹感 |
| Samsung Ultra | 超清夜拍感 |
| iPhone | 清透日常感 |
| Insta360 | 廣角旅行感 |
| Korean Style | 韓系女神感 |
| Xiaohongshu Style | 奶油系網美感 |
| Vogue | 時尚雜誌感 |

---

# MVP 推薦首發組合

最建議先推出：

1. CCD 復古辣妹感
2. 女友感底片（Portra 400）
3. 韓系女神感
4. 奶油系網美感
5. 單眼高級人像
6. 高級空氣感（Leica）
7. 清透日常感（iPhone）
8. 超清夜拍感（Samsung Ultra）
9. 廣角旅行感（Insta360）
10. 東京街拍感

這 10 個風格基本已經涵蓋目前 IG、小紅書、Threads、TikTok 上大部分女生會搜尋的影像風格。

---

# Premium AI Camera Style App Mockup UI 規格

## UI 介面名稱

Premium AI Camera Style App Mockup

## 產品定位文案

```text
一張照片，變成不同器材的高級影像語言。
```

## 核心產品概念

```text
不是套廉價濾鏡，而是保留本人與構圖，重建鏡頭感、色彩科學、景深、顆粒與光線質地。
```

## App 英文名稱 / 品牌感名稱

```text
AI Camera Style Studio
CameraLab
Style Transfer
```

## Hero 區塊文案

### Badge

```text
AI Camera Style Studio
```

### 主標題

```text
一張照片，變成不同器材的高級影像語言。
```

### 副標題

```text
不是套廉價濾鏡，而是保留本人與構圖，重建鏡頭感、色彩科學、景深、顆粒與光線質地。
```

### CTA 按鈕

```text
Upload Photo
View Style Packs
```

## 核心賣點卡片

```text
01 Face Lock
02 Lens Engine
03 Style Mix
```

### Face Lock

確保改圖後還是同一個人，保留本人臉部特徵、五官比例與原始身份，不讓 AI 把臉改成另一個人。

### Lens Engine

模擬不同器材與鏡頭語言，例如單眼、CCD、iPhone、Samsung Ultra、Insta360、Leica、底片相機等。

### Style Mix

讓使用者可以混搭風格，例如 Leica 70% + Portra 30%，或 CCD 50% + 奶油系網美感 50%。

---

# Mobile App UI Flow

## 頂部導覽區

### App 標籤

```text
CameraLab
```

### 頁面標題

```text
Style Transfer
```

### 設定 / 微調入口

```text
Sliders / Adjustments
```

用途：讓使用者調整風格強度、顆粒、景深、銳利度、膚色保留程度等。

---

## 搜尋欄

### Placeholder

```text
搜尋 Leica、CCD、奶油風...
```

### 搜尋用途

讓使用者可以直接搜尋：

- Leica
- CCD
- 奶油風
- iPhone
- Samsung
- Insta360
- 韓系
- 底片
- 東京街拍
- 小紅書

---

## 分類 Tabs

```text
For You
相機感
底片感
社群感
復古感
```

### For You

AI 根據使用者上傳照片自動推薦最適合的風格。

### 相機感

包含 DSLR、Leica、Sony、Canon、Nikon、iPhone、Samsung、Insta360 等器材模擬風格。

### 底片感

包含 Portra 400、Kodak Gold、Cinestill 800T、Fujifilm Classic Negative 等底片風格。

### 社群感

包含韓系女神感、小紅書奶油風、Vogue 雜誌風、東京街拍風等。

### 復古感

包含 CCD、一次性底片機、傻瓜相機、MSN 相簿風、Y2K 等。

---

# Before / After Preview 區塊

## 預覽標籤

```text
Preview
```

## 切換狀態

```text
Before
After
```

## 預覽區主要文案

```text
Leica 高級空氣感
```

## 預覽區說明文案

```text
保留人臉與構圖，只轉換光線與鏡頭語言
```

## 主要生成按鈕

```text
Generate
```

## 功能目的

Before / After Preview 用來讓使用者清楚看見：

- 原圖與改圖後的差異
- 風格是否符合期待
- 人臉是否被保留
- 構圖是否被保留
- 光線、鏡頭感、色彩是否被轉換

---

# Style Selection UI

## 區塊標題

```text
選擇風格
```

## 目前選擇狀態

```text
目前：{selected_style_name}
```

範例：

```text
目前：Leica 高級空氣感
```

## Style Mix 入口

```text
Mix
```

用途：讓使用者混合兩種以上風格。

---

# 首頁 Style Cards

以下是目前 UI Mockup 中出現的 8 個首發風格卡片。

## 01. CCD 復古辣妹感

### Style ID

```text
ccd
```

### App 顯示名稱

```text
CCD 復古辣妹感
```

### 英文標籤

```text
Y2K Flash
```

### 卡片描述

```text
直閃、冷色、派對快照
```

### 視覺方向

- 直閃
- Y2K
- 冷色調
- 派對快照
- 復古數位相機
- 輕微過曝

---

## 02. Leica 高級空氣感

### Style ID

```text
leica
```

### App 顯示名稱

```text
Leica 高級空氣感
```

### 英文標籤

```text
Premium Air
```

### 卡片描述

```text
立體、低調、精品感
```

### 視覺方向

- 高級感
- 低飽和
- 立體感
- 精品生活感
- 空氣感
- 光線層次細膩

---

## 03. 女友感底片

### Style ID

```text
portra
```

### App 顯示名稱

```text
女友感底片
```

### 英文標籤

```text
Portra 400
```

### 卡片描述

```text
柔膚、粉彩、細顆粒
```

### 視覺方向

- 柔和膚色
- 粉彩色調
- 細顆粒
- 底片感
- 溫柔人像
- 女友視角

---

## 04. iPhone 清透日常感

### Style ID

```text
iphone
```

### App 顯示名稱

```text
iPhone 清透日常感
```

### 英文標籤

```text
Clean HDR
```

### 卡片描述

```text
自然 HDR、清透社群感
```

### 視覺方向

- 乾淨
- 明亮
- 自然 HDR
- 日常感
- 社群可用
- 真實膚色

---

## 05. Samsung 超清夜拍感

### Style ID

```text
samsung
```

### App 顯示名稱

```text
Samsung 超清夜拍感
```

### 英文標籤

```text
Ultra Night
```

### 卡片描述

```text
高解析、亮夜景、鮮明
```

### 視覺方向

- 超高解析
- 夜景明亮
- 色彩鮮明
- 高對比
- 手機旗艦感
- 智慧 HDR

---

## 06. Insta360 廣角旅行感

### Style ID

```text
insta360
```

### App 顯示名稱

```text
Insta360 廣角旅行感
```

### 英文標籤

```text
Wide Travel
```

### 卡片描述

```text
超廣角、旅行、沉浸感
```

### 視覺方向

- 超廣角
- 旅行感
- 沉浸感
- 戶外 Vlog
- 輕微魚眼
- 動態構圖

---

## 07. 韓系女神感

### Style ID

```text
korean
```

### App 顯示名稱

```text
韓系女神感
```

### 英文標籤

```text
Soft Luxe
```

### 卡片描述

```text
柔光、乾淨、精品日常
```

### 視覺方向

- 柔光
- 乾淨背景
- 精品日常
- 韓系社群照
- 明亮膚色
- 空氣感

---

## 08. 奶油系網美感

### Style ID

```text
xhs
```

### App 顯示名稱

```text
奶油系網美感
```

### 英文標籤

```text
Creamy Cafe
```

### 卡片描述

```text
奶油光、咖啡廳、暖白
```

### 視覺方向

- 奶油光
- 咖啡廳
- 暖白色調
- 小紅書感
- 精緻生活感
- 柔和陰影

---

# 底部操作列

## Reset Button

```text
重設
```

用途：清除目前套用風格，回到原始照片狀態。

## Fine Tune Button

```text
微調
```

用途：進入進階調整，例如：

- 風格強度
- 顆粒強度
- 景深強度
- 銳利度
- 膚色保留
- 閃光燈強度
- HDR 強度

## Save Button

```text
儲存
```

用途：下載或儲存產出的圖片。

---

# UI 對應資料結構

```json
[
  {
    "id": "ccd",
    "name": "CCD 復古辣妹感",
    "label": "Y2K Flash",
    "category": "復古感",
    "description": "直閃、冷色、派對快照"
  },
  {
    "id": "leica",
    "name": "Leica 高級空氣感",
    "label": "Premium Air",
    "category": "相機感",
    "description": "立體、低調、精品感"
  },
  {
    "id": "portra",
    "name": "女友感底片",
    "label": "Portra 400",
    "category": "底片感",
    "description": "柔膚、粉彩、細顆粒"
  },
  {
    "id": "iphone",
    "name": "iPhone 清透日常感",
    "label": "Clean HDR",
    "category": "相機感",
    "description": "自然 HDR、清透社群感"
  },
  {
    "id": "samsung",
    "name": "Samsung 超清夜拍感",
    "label": "Ultra Night",
    "category": "相機感",
    "description": "高解析、亮夜景、鮮明"
  },
  {
    "id": "insta360",
    "name": "Insta360 廣角旅行感",
    "label": "Wide Travel",
    "category": "相機感",
    "description": "超廣角、旅行、沉浸感"
  },
  {
    "id": "korean",
    "name": "韓系女神感",
    "label": "Soft Luxe",
    "category": "社群感",
    "description": "柔光、乾淨、精品日常"
  },
  {
    "id": "xhs",
    "name": "奶油系網美感",
    "label": "Creamy Cafe",
    "category": "社群感",
    "description": "奶油光、咖啡廳、暖白"
  }
]
```

---

# UI Prompt 組裝邏輯

當使用者在 UI 選擇一個 Style Card，系統可以將 UI 資料轉成 AI Prompt。

## Prompt Template

```text
User uploaded one photo.

Selected style:
{style_name}

Style label:
{style_label}

Style description:
{style_description}

Transform the uploaded photo into this visual style.

Preserve the original person's face, pose, outfit, hairstyle, composition, background layout, and scene content.

Only change the photographic rendering style, including color science, lens feeling, contrast, depth of field, grain, noise, sharpness, dynamic range, flash rendering, and mood.

The final image should look like a realistic photograph, not an illustration or AI-generated artwork.
```

## Example：Leica 高級空氣感

```text
User uploaded one photo.

Selected style:
Leica 高級空氣感

Style label:
Premium Air

Style description:
立體、低調、精品感

Transform the uploaded photo into a premium Leica-inspired photography style.

Preserve the original person's face, pose, outfit, hairstyle, composition, background layout, and scene content.

Only change the photographic rendering style, including natural contrast, elegant color transitions, rich tonal depth, soft highlight rolloff, realistic skin texture, subtle depth of field, and premium editorial mood.

The final image should look like a realistic photograph, not an illustration or AI-generated artwork.
```

---

# UI 文案總表

```text
AI Camera Style Studio
CameraLab
Style Transfer
一張照片，變成不同器材的高級影像語言。
不是套廉價濾鏡，而是保留本人與構圖，重建鏡頭感、色彩科學、景深、顆粒與光線質地。
Upload Photo
View Style Packs
Face Lock
Lens Engine
Style Mix
搜尋 Leica、CCD、奶油風...
For You
相機感
底片感
社群感
復古感
Preview
Before
After
Generate
選擇風格
目前：{selected_style_name}
Mix
重設
微調
儲存
```
