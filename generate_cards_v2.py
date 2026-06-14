from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random

def add_shadow(img, offset=5, blur=10):
    """添加阴影效果"""
    shadow = Image.new('RGBA', (img.width + 20, img.height + 20), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rectangle([10, 10, img.width + 10, img.height + 10], fill=(0, 0, 0, 80))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    result = Image.new('RGBA', shadow.size, (0, 0, 0, 0))
    result.paste(shadow, (0, 0))
    result.paste(img, (10 - offset, 10 - offset), img if img.mode == 'RGBA' else None)
    return result

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = bbox
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill, outline=outline, width=width)

def create_gradient(width, height, color1, color2, direction='vertical'):
    """创建渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    for i in range(height if direction == 'vertical' else width):
        ratio = i / (height if direction == 'vertical' else width)
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        
        if direction == 'vertical':
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        else:
            draw.line([(i, 0), (i, height)], fill=(r, g, b))
    
    return img

def create_travel_card():
    """创建旅记项目卡片 - 精美版"""
    width, height = 1200, 630
    
    # 渐变背景 - 温暖的橙色到珊瑚色
    img = create_gradient(width, height, (255, 107, 53), (255, 166, 100))
    draw = ImageDraw.Draw(img)
    
    # 添加装饰性几何元素
    for _ in range(15):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(20, 80)
        opacity = random.randint(10, 40)
        draw.ellipse([x, y, x+size, y+size], fill=(255, 255, 255, opacity))
    
    # 添加斜线纹理
    for i in range(-height, width + height, 30):
        draw.line([(i, 0), (i + height, height)], fill=(255, 255, 255, 15), width=1)
    
    try:
        # 尝试加载字体
        title_font = ImageFont.truetype("msyhbd.ttc", 56)  # 粗体
        subtitle_font = ImageFont.truetype("msyh.ttc", 28)
        feature_font = ImageFont.truetype("msyh.ttc", 18)
        small_font = ImageFont.truetype("msyh.ttc", 14)
        icon_font = ImageFont.truetype("seguisym.ttf", 32)  # 图标字体
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        feature_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()
    
    # 左侧内容区域
    left_margin = 80
    
    # 品牌标识小图标
    draw.rounded_rectangle([left_margin, 120, left_margin + 50, 155], radius=10, fill=(255, 255, 255, 200))
    draw.text((left_margin + 10, 125), "✈", fill=(255, 107, 53), font=feature_font)
    draw.text((left_margin + 65, 125), "旅行社交", fill=(255, 255, 255, 200), font=feature_font)
    
    # 主标题
    draw.text((left_margin, 180), "旅记", fill="white", font=title_font)
    
    # 副标题
    draw.text((left_margin, 260), "旅行生活社交分享平台", fill=(255, 255, 255, 230), font=subtitle_font)
    
    # 描述文字
    draw.text((left_margin, 310), "专为Z世代打造的轻量化旅行社交体验", fill=(255, 255, 255, 180), font=small_font)
    
    # 功能标签
    features = [
        ("🎯", "旅伴匹配"),
        ("📸", "内容分享"),
        ("🔍", "探索发现"),
        ("👤", "个人中心")
    ]
    
    # 标签背景
    tag_y = 360
    draw.rounded_rectangle([left_margin, tag_y, left_margin + 380, tag_y + 120], 
                          radius=15, fill=(255, 255, 255, 40))
    
    for i, (icon, text) in enumerate(features):
        x = left_margin + 20 + (i % 2) * 190
        y = tag_y + 15 + (i // 2) * 55
        
        # 标签
        draw.rounded_rectangle([x, y, x + 160, y + 40], radius=20, fill=(255, 255, 255, 60))
        draw.text((x + 10, y + 8), f"{icon} {text}", fill="white", font=feature_font)
    
    # 右侧 - 手机mockup
    phone_x = 650
    phone_y = 60
    
    # 第一个手机 - 主界面
    draw_phone_mockup(draw, phone_x, phone_y, 220, 440, "white", (255, 245, 237))
    
    # 状态栏
    draw.rectangle([phone_x + 15, phone_y + 15, phone_x + 205, phone_y + 45], fill=(255, 107, 53))
    draw.text((phone_x + 25, phone_y + 18), "旅记", fill="white", font=feature_font)
    draw.text((phone_x + 150, phone_y + 22), "9:41", fill="white", font=small_font)
    
    # 搜索栏
    draw.rounded_rectangle([phone_x + 20, phone_y + 55, phone_x + 200, phone_y + 85], 
                          radius=20, fill=(245, 245, 245))
    draw.text((phone_x + 35, phone_y + 62), "搜索旅行目的地...", fill=(180, 180, 180), font=small_font)
    
    # 卡片内容
    card_colors = [(255, 200, 150), (255, 180, 120), (255, 160, 100)]
    for i in range(3):
        card_y = phone_y + 100 + i * 100
        draw.rounded_rectangle([phone_x + 15, card_y, phone_x + 205, card_y + 85], 
                              radius=12, fill="white")
        # 图片占位
        draw.rounded_rectangle([phone_x + 20, card_y + 5, phone_x + 80, card_y + 80], 
                              radius=8, fill=card_colors[i])
        # 文字
        draw.text((phone_x + 90, card_y + 15), "旅行故事", fill=(80, 80, 80), font=feature_font)
        draw.text((phone_x + 90, card_y + 40), "发现美好旅程", fill=(150, 150, 150), font=small_font)
        # 点赞图标
        draw.text((phone_x + 170, card_y + 55), "♡", fill=(255, 107, 53), font=feature_font)
    
    # 第二个手机 - 匹配界面
    phone_x2 = 900
    phone_y2 = 100
    
    draw_phone_mockup(draw, phone_x2, phone_y2, 200, 400, "white", (255, 240, 230))
    
    # 匹配界面内容
    draw.rectangle([phone_x2 + 15, phone_y2 + 15, phone_x2 + 185, phone_y2 + 45], fill=(255, 107, 53))
    draw.text((phone_x2 + 25, phone_y2 + 18), "旅伴匹配", fill="white", font=feature_font)
    
    # 用户卡片
    draw.rounded_rectangle([phone_x2 + 20, phone_y2 + 60, phone_x2 + 180, phone_y2 + 200], 
                          radius=15, fill="white")
    
    # 头像占位
    draw.ellipse([phone_x2 + 60, phone_y2 + 75, phone_x2 + 140, phone_y2 + 155], 
                fill=(255, 200, 150))
    draw.text((phone_x2 + 80, phone_y2 + 100), "👤", fill=(255, 107, 53), font=icon_font)
    
    draw.text((phone_x2 + 50, phone_y2 + 165), "旅行爱好者", fill=(80, 80, 80), font=feature_font)
    draw.text((phone_x2 + 45, phone_y2 + 185), "喜欢探索新地方", fill=(150, 150, 150), font=small_font)
    
    # 匹配按钮
    draw.rounded_rectangle([phone_x2 + 40, phone_y2 + 220, phone_x2 + 160, phone_y2 + 250], 
                          radius=25, fill=(255, 107, 53))
    draw.text((phone_x2 + 65, phone_y2 + 228), "开始匹配", fill="white", font=feature_font)
    
    # 底部导航栏
    draw.rectangle([phone_x2 + 15, phone_y2 + 350, phone_x2 + 185, phone_y2 + 385], fill=(250, 250, 250))
    nav_items = ["首页", "发现", "消息", "我的"]
    for i, item in enumerate(nav_items):
        x = phone_x2 + 25 + i * 42
        draw.text((x, phone_y2 + 358), item, fill=(150, 150, 150) if i > 0 else (255, 107, 53), font=small_font)
    
    # 底部品牌信息
    draw.rounded_rectangle([left_margin, height - 60, left_margin + 250, height - 30], 
                          radius=15, fill=(255, 255, 255, 40))
    draw.text((left_margin + 15, height - 55), "UI/UX Design by 汪涛", fill="white", font=feature_font)
    
    # 保存图片
    img = img.convert('RGB')
    img.save("E:/汪涛/portfolio/旅记/卡片展示.png", quality=95, dpi=(300, 300))
    print("旅记卡片已生成 - 精美版")

def draw_phone_mockup(draw, x, y, width, height, border_color, screen_color):
    """绘制手机mockup"""
    # 手机外壳 - 圆角矩形
    draw.rounded_rectangle([x, y, x + width, y + height], 
                          radius=25, fill=border_color, outline=(220, 220, 220), width=2)
    
    # 屏幕区域
    screen_margin = 12
    draw.rounded_rectangle([x + screen_margin, y + screen_margin, 
                           x + width - screen_margin, y + height - screen_margin],
                          radius=18, fill=screen_color)
    
    # 刘海屏
    notch_width = 80
    notch_x = x + (width - notch_width) // 2
    draw.rounded_rectangle([notch_x, y, notch_x + notch_width, y + 12],
                          radius=6, fill=(50, 50, 50))
    
    # 底部横条
    bar_width = 60
    bar_x = x + (width - bar_width) // 2
    draw.rounded_rectangle([bar_x, y + height - 15, bar_x + bar_width, y + height - 8],
                          radius=4, fill=(180, 180, 180))

def create_canal_card():
    """创建运河项目卡片 - 精美版"""
    width, height = 1200, 630
    
    # 渐变背景 - 深蓝到青色，文化感
    img = create_gradient(width, height, (15, 50, 120), (30, 100, 160))
    draw = ImageDraw.Draw(img)
    
    # 添加古典装饰元素 - 水波纹效果
    for _ in range(20):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(30, 100)
        opacity = random.randint(5, 25)
        
        # 绘制水波纹
        for r in range(0, size, 8):
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(255, 255, 255, opacity), width=1)
    
    # 添加古典边框装饰
    border_margin = 30
    draw.rounded_rectangle([border_margin, border_margin, width - border_margin, height - border_margin],
                          radius=10, outline=(255, 255, 255, 30), width=2)
    
    # 内部装饰线
    inner_margin = 40
    draw.rounded_rectangle([inner_margin, inner_margin, width - inner_margin, height - inner_margin],
                          radius=8, outline=(255, 255, 255, 15), width=1)
    
    try:
        title_font = ImageFont.truetype("msyhbd.ttc", 56)
        subtitle_font = ImageFont.truetype("msyh.ttc", 28)
        feature_font = ImageFont.truetype("msyh.ttc", 18)
        small_font = ImageFont.truetype("msyh.ttc", 14)
        english_font = ImageFont.truetype("segoeui.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        feature_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        english_font = ImageFont.load_default()
    
    # 左侧 - 平板设备展示
    tab_x = 80
    tab_y = 80
    tab_w = 420
    tab_h = 480
    
    # 平板外壳阴影
    draw.rounded_rectangle([tab_x + 5, tab_y + 5, tab_x + tab_w + 5, tab_y + tab_h + 5],
                          radius=20, fill=(0, 0, 0, 50))
    
    # 平板外壳
    draw.rounded_rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h],
                          radius=20, fill=(245, 248, 255), outline=(200, 210, 220), width=2)
    
    # 屏幕区域
    screen_margin = 15
    draw.rounded_rectangle([tab_x + screen_margin, tab_y + screen_margin,
                           tab_x + tab_w - screen_margin, tab_y + tab_h - screen_margin],
                          radius=15, fill=(255, 255, 255))
    
    # 顶部导航栏
    nav_height = 50
    draw.rectangle([tab_x + screen_margin, tab_y + screen_margin,
                   tab_x + tab_w - screen_margin, tab_y + screen_margin + nav_height],
                  fill=(20, 60, 140))
    
    # Logo 和标题
    draw.text((tab_x + screen_margin + 15, tab_y + screen_margin + 12), "🏛️", fill="white", font=feature_font)
    draw.text((tab_x + screen_margin + 45, tab_y + screen_margin + 12), "大运河文化", fill="white", font=feature_font)
    
    # 地图区域
    map_y = tab_y + screen_margin + nav_height + 10
    map_height = 180
    draw.rectangle([tab_x + screen_margin + 10, map_y,
                   tab_x + tab_w - screen_margin - 10, map_y + map_height],
                  fill=(230, 240, 250))
    
    # 绘制运河线路 - 曲线效果
    canal_points = []
    for i in range(50):
        x = tab_x + screen_margin + 20 + i * 7.5
        y = map_y + 80 + math.sin(i * 0.3) * 30 + math.cos(i * 0.2) * 20
        canal_points.append((x, y))
    
    # 绘制运河（多条线增加效果）
    for offset in [-2, 0, 2]:
        points = [(x, y + offset) for x, y in canal_points]
        if len(points) > 1:
            draw.line(points, fill=(20, 100, 180, 180), width=4)
    
    # 绘制城市标记
    cities = [
        (tab_x + screen_margin + 50, map_y + 60, "北京"),
        (tab_x + screen_margin + 150, map_y + 90, "天津"),
        (tab_x + screen_margin + 250, map_y + 50, "济宁"),
        (tab_x + screen_margin + 320, map_y + 100, "杭州")
    ]
    
    for cx, cy, name in cities:
        # 城市点
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(220, 50, 50), outline="white", width=2)
        # 城市名
        draw.text((cx + 10, cy - 8), name, fill=(80, 80, 80), font=small_font)
    
    # 运河名称标注
    draw.text((tab_x + screen_margin + 100, map_y + 140), "京杭大运河", fill=(20, 60, 140), font=feature_font)
    
    # 内容卡片区域
    cards_y = map_y + map_height + 20
    card_height = 65
    
    content_cards = [
        ("🏛️", "历史遗迹", "探访运河沿岸古迹"),
        ("🎭", "文化体验", "感受千年运河文化"),
        ("🚢", "游船之旅", "沉浸式运河游览")
    ]
    
    for i, (icon, title, desc) in enumerate(content_cards):
        card_y = cards_y + i * (card_height + 8)
        draw.rounded_rectangle([tab_x + screen_margin + 10, card_y,
                               tab_x + tab_w - screen_margin - 10, card_y + card_height],
                              radius=10, fill=(248, 250, 255))
        
        # 图标背景
        draw.rounded_rectangle([tab_x + screen_margin + 20, card_y + 10,
                               tab_x + screen_margin + 55, card_y + 50],
                              radius=8, fill=(230, 240, 255))
        draw.text((tab_x + screen_margin + 28, card_y + 15), icon, fill=(20, 60, 140), font=feature_font)
        
        # 文字
        draw.text((tab_x + screen_margin + 70, card_y + 12), title, fill=(40, 40, 40), font=feature_font)
        draw.text((tab_x + screen_margin + 70, card_y + 38), desc, fill=(120, 120, 120), font=small_font)
    
    # 右侧内容区域
    content_x = 560
    
    # 品牌标识
    draw.rounded_rectangle([content_x, 100, content_x + 120, 130], radius=15, fill=(255, 255, 255, 30))
    draw.text((content_x + 15, 105), "CULTURAL APP", fill=(200, 220, 255), font=english_font)
    
    # 主标题
    draw.text((content_x, 160), "运河", fill="white", font=title_font)
    
    # 英文副标题
    draw.text((content_x, 240), "Grand Canal Heritage", fill=(200, 220, 255), font=english_font)
    
    # 中文副标题
    draw.text((content_x, 275), "大运河文化主题应用", fill=(255, 255, 255, 230), font=subtitle_font)
    
    # 描述
    draw.text((content_x, 325), "融合传统与现代，探索千年运河文化", fill=(200, 220, 255, 180), font=small_font)
    
    # 特性列表
    features = [
        ("🌊", "文化探索", "沉浸式运河历史体验"),
        ("📍", "景点导览", "智能路线规划推荐"),
        ("📖", "知识图谱", "趣味文化知识学习"),
        ("🎨", "视觉叙事", "精美插画与动效")
    ]
    
    feature_y = 370
    for i, (icon, title, desc) in enumerate(features):
        y = feature_y + i * 50
        
        # 图标
        draw.rounded_rectangle([content_x, y, content_x + 35, y + 35], radius=8, fill=(255, 255, 255, 20))
        draw.text((content_x + 7, y + 5), icon, fill="white", font=feature_font)
        
        # 文字
        draw.text((content_x + 45, y + 2), title, fill="white", font=feature_font)
        draw.text((content_x + 45, y + 25), desc, fill=(200, 220, 255, 150), font=small_font)
    
    # 底部品牌信息
    draw.rounded_rectangle([content_x, height - 60, content_x + 250, height - 30],
                          radius=15, fill=(255, 255, 255, 20))
    draw.text((content_x + 15, height - 55), "UI/UX Design by 汪涛", fill=(200, 220, 255), font=feature_font)
    
    # 保存图片
    img = img.convert('RGB')
    img.save("E:/汪涛/portfolio/运河/卡片展示.png", quality=95, dpi=(300, 300))
    print("运河卡片已生成 - 精美版")

if __name__ == "__main__":
    random.seed(42)  # 固定随机种子，保证每次生成一致
    create_travel_card()
    create_canal_card()
    print("所有精美卡片生成完成！")