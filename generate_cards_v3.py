from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math
import random

def create_glass_effect(draw, bbox, radius, color, opacity=60):
    """创建玻璃态效果"""
    x1, y1, x2, y2 = bbox
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, 
                          fill=(*color, opacity), outline=(255, 255, 255, 40), width=1)

def create_soft_shadow(img, x, y, width, height, radius=20, blur=15, opacity=40):
    """创建柔和阴影"""
    shadow = Image.new('RGBA', img.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle([x + 4, y + 4, x + width + 4, y + height + 4], 
                                 radius=radius, fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    return Image.alpha_composite(img.convert('RGBA'), shadow)

def draw_modern_phone(draw, x, y, width, height, screen_color):
    """绘制现代手机mockup"""
    # 手机阴影
    draw.rounded_rectangle([x + 3, y + 3, x + width + 3, y + height + 3], 
                          radius=28, fill=(0, 0, 0, 40))
    
    # 手机外壳
    draw.rounded_rectangle([x, y, x + width, y + height], 
                          radius=28, fill=(50, 50, 55), outline=(80, 80, 85), width=1)
    
    # 屏幕
    screen_margin = 8
    draw.rounded_rectangle([x + screen_margin, y + screen_margin, 
                           x + width - screen_margin, y + height - screen_margin],
                          radius=22, fill=screen_color)
    
    # 灵动岛
    island_width = 90
    island_x = x + (width - island_width) // 2
    draw.rounded_rectangle([island_x, y + 8, island_x + island_width, y + 24], 
                          radius=8, fill=(30, 30, 35))
    
    # 底部指示条
    bar_width = 50
    bar_x = x + (width - bar_width) // 2
    draw.rounded_rectangle([bar_x, y + height - 16, bar_x + bar_width, y + height - 10], 
                          radius=3, fill=(120, 120, 125))

def draw_modern_tablet(draw, x, y, width, height, screen_color):
    """绘制现代平板mockup"""
    # 阴影
    draw.rounded_rectangle([x + 4, y + 4, x + width + 4, y + height + 4], 
                          radius=22, fill=(0, 0, 0, 35))
    
    # 外壳
    draw.rounded_rectangle([x, y, x + width, y + height], 
                          radius=22, fill=(240, 240, 245), outline=(200, 200, 210), width=1)
    
    # 屏幕
    screen_margin = 12
    draw.rounded_rectangle([x + screen_margin, y + screen_margin, 
                           x + width - screen_margin, y + height - screen_margin],
                          radius=16, fill=screen_color)
    
    # 前置摄像头
    camera_x = x + width // 2
    camera_y = y + 6
    draw.ellipse([camera_x - 3, camera_y - 3, camera_x + 3, camera_y + 3], 
                fill=(180, 180, 185))

def create_travel_card():
    """旅记卡片 - 高级版"""
    width, height = 1200, 630
    
    # 创建渐变背景 - 温暖的珊瑚橙
    img = Image.new('RGBA', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 多层渐变
    for y in range(height):
        ratio = y / height
        # 主渐变：珊瑚色到桃色
        r = int(255 - 30 * ratio)
        g = int(120 + 60 * ratio)
        b = int(80 + 80 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
    
    # 添加柔和的圆形装饰
    circles = [
        (150, 100, 180, (255, 255, 255, 8)),
        (300, 400, 120, (255, 255, 255, 6)),
        (900, 150, 200, (255, 255, 255, 5)),
        (1050, 450, 150, (255, 255, 255, 7)),
    ]
    
    for x, y, radius, color in circles:
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)
    
    # 添加网格纹理
    for i in range(0, width, 40):
        draw.line([(i, 0), (i, height)], fill=(255, 255, 255, 5), width=1)
    for i in range(0, height, 40):
        draw.line([(0, i), (width, i)], fill=(255, 255, 255, 5), width=1)
    
    # 加载字体
    try:
        title_font = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", 52)
        subtitle_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 24)
        desc_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 16)
        tag_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 14)
        icon_font = ImageFont.truetype("C:/Windows/Fonts/seguisym.ttf", 28)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
        tag_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()
    
    # ========== 左侧内容 ==========
    left_x = 80
    
    # 顶部标签
    draw.rounded_rectangle([left_x, 120, left_x + 100, 145], radius=12, fill=(255, 255, 255, 50))
    draw.text((left_x + 12, 123), "社交应用", fill=(255, 255, 255, 200), font=tag_font)
    
    # 主标题
    draw.text((left_x, 170), "旅记", fill="white", font=title_font)
    
    # 英文副标题
    draw.text((left_x, 240), "Travel Notes", fill=(255, 255, 255, 180), font=subtitle_font)
    
    # 中文描述
    draw.text((left_x, 280), "旅行生活社交分享平台", fill=(255, 255, 255, 220), font=subtitle_font)
    
    # 详细描述
    draw.text((left_x, 325), "专为Z世代打造的轻量化旅行社交体验", fill=(255, 255, 255, 150), font=desc_font)
    
    # 功能标签组
    tags = ["旅伴匹配", "内容分享", "探索发现", "个人中心"]
    tag_x = left_x
    tag_y = 370
    
    # 标签背景容器
    draw.rounded_rectangle([tag_x - 10, tag_y - 10, tag_x + 370, tag_y + 90], 
                          radius=16, fill=(255, 255, 255, 25))
    
    for i, tag in enumerate(tags):
        x = tag_x + (i % 2) * 185
        y = tag_y + (i // 2) * 45
        
        # 标签
        draw.rounded_rectangle([x, y, x + 170, y + 35], radius=18, fill=(255, 255, 255, 40))
        
        # 图标点
        draw.ellipse([x + 12, y + 12, x + 20, y + 20], fill=(255, 255, 255, 180))
        
        # 文字
        draw.text((x + 28, y + 8), tag, fill="white", font=tag_font)
    
    # 设计规范标签
    specs = ["Figma", "用户研究", "交互设计", "视觉规范"]
    spec_y = 480
    
    for i, spec in enumerate(specs):
        x = left_x + i * 95
        draw.rounded_rectangle([x, spec_y, x + 85, spec_y + 28], radius=14, 
                              fill=(255, 255, 255, 20), outline=(255, 255, 255, 40))
        draw.text((x + 10, spec_y + 5), spec, fill=(255, 255, 255, 160), font=tag_font)
    
    # ========== 右侧设备展示 ==========
    # 主手机 - 首页
    phone1_x = 620
    phone1_y = 70
    phone1_w = 220
    phone1_h = 450
    
    draw_modern_phone(draw, phone1_x, phone1_y, phone1_w, phone1_h, (255, 250, 245))
    
    # 首页内容
    # 顶部导航
    draw.rectangle([phone1_x + 16, phone1_y + 35, phone1_x + phone1_w - 16, phone1_y + 75], 
                  fill=(255, 120, 80))
    draw.text((phone1_x + 26, phone1_y + 42), "旅记", fill="white", font=tag_font)
    
    # 搜索框
    draw.rounded_rectangle([phone1_x + 20, phone1_y + 85, phone1_x + phone1_w - 20, phone1_y + 110], 
                          radius=20, fill=(245, 245, 245))
    draw.text((phone1_x + 35, phone1_y + 90), "🔍 搜索旅行目的地...", fill=(180, 180, 180), font=tag_font)
    
    # 故事卡片
    card_colors = [(255, 200, 160), (255, 180, 140), (255, 220, 180)]
    for i in range(3):
        card_y = phone1_y + 125 + i * 100
        
        # 卡片背景
        draw.rounded_rectangle([phone1_x + 16, card_y, phone1_x + phone1_w - 16, card_y + 85], 
                              radius=12, fill="white")
        
        # 图片区域
        draw.rounded_rectangle([phone1_x + 20, card_y + 5, phone1_x + 75, card_y + 80], 
                              radius=8, fill=card_colors[i])
        
        # 装饰元素
        draw.ellipse([phone1_x + 35, card_y + 20, phone1_x + 55, card_y + 40], 
                    fill=(255, 255, 255, 80))
        
        # 标题
        draw.text((phone1_x + 85, card_y + 15), "旅行故事", fill=(60, 60, 60), font=tag_font)
        
        # 描述
        draw.text((phone1_x + 85, card_y + 40), "探索世界的美好", fill=(150, 150, 150), font=tag_font)
        
        # 点赞
        draw.text((phone1_x + 175, card_y + 55), "♡ 128", fill=(255, 120, 80), font=tag_font)
    
    # 第二个手机 - 匹配页
    phone2_x = 870
    phone2_y = 110
    phone2_w = 200
    phone2_h = 410
    
    draw_modern_phone(draw, phone2_x, phone2_y, phone2_w, phone2_h, (255, 245, 240))
    
    # 匹配页内容
    draw.rectangle([phone2_x + 14, phone2_y + 35, phone2_x + phone2_w - 14, phone2_y + 65], 
                  fill=(255, 120, 80))
    draw.text((phone2_x + 24, phone2_y + 40), "旅伴匹配", fill="white", font=tag_font)
    
    # 用户卡片
    draw.rounded_rectangle([phone2_x + 18, phone2_y + 80, phone2_x + phone2_w - 18, phone2_y + 230], 
                          radius=16, fill="white")
    
    # 头像
    avatar_x = phone2_x + (phone2_w // 2)
    avatar_y = phone2_y + 120
    draw.ellipse([avatar_x - 30, avatar_y - 30, avatar_x + 30, avatar_y + 30], 
                fill=(255, 200, 160))
    draw.ellipse([avatar_x - 20, avatar_y - 20, avatar_x + 20, avatar_y + 20], 
                fill=(255, 160, 120))
    draw.text((avatar_x - 8, avatar_y - 12), "👤", fill="white", font=tag_font)
    
    # 用户信息
    draw.text((avatar_x - 40, avatar_y + 40), "旅行爱好者", fill=(60, 60, 60), font=tag_font)
    draw.text((avatar_x - 50, avatar_y + 65), "喜欢探索新地方", fill=(150, 150, 150), font=tag_font)
    
    # 匹配按钮
    btn_x = phone2_x + 40
    btn_y = phone2_y + 245
    draw.rounded_rectangle([btn_x, btn_y, btn_x + 120, btn_y + 38], 
                          radius=19, fill=(255, 120, 80))
    draw.text((btn_x + 25, btn_y + 9), "开始匹配", fill="white", font=tag_font)
    
    # 推荐列表
    for i in range(2):
        list_y = phone2_y + 300 + i * 55
        draw.rounded_rectangle([phone2_x + 18, list_y, phone2_x + phone2_w - 18, list_y + 45], 
                              radius=10, fill=(255, 255, 255, 200))
        
        # 小头像
        draw.ellipse([phone2_x + 28, list_y + 10, phone2_x + 52, list_y + 34], 
                    fill=(200, 180, 160))
        
        draw.text((phone2_x + 60, list_y + 8), "旅伴推荐", fill=(80, 80, 80), font=tag_font)
        draw.text((phone2_x + 60, list_y + 28), "志同道合的旅伴", fill=(150, 150, 150), font=tag_font)
    
    # 底部品牌
    draw.rounded_rectangle([left_x, height - 55, left_x + 200, height - 30], 
                          radius=12, fill=(255, 255, 255, 30))
    draw.text((left_x + 15, height - 50), "UI/UX Design by 汪涛", fill=(255, 255, 255, 180), font=tag_font)
    
    # 保存
    img = img.convert('RGB')
    img.save("E:/汪涛/portfolio/旅记/卡片展示.png", quality=95, dpi=(300, 300))
    print("旅记卡片已生成 - 高级版")

def create_canal_card():
    """运河卡片 - 高级版"""
    width, height = 1200, 630
    
    # 创建渐变背景 - 深邃蓝
    img = Image.new('RGBA', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 多层渐变
    for y in range(height):
        ratio = y / height
        # 深蓝到靛蓝
        r = int(15 + 20 * ratio)
        g = int(40 + 50 * ratio)
        b = int(100 + 60 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
    
    # 添加装饰性水波纹
    for _ in range(30):
        cx = random.randint(0, width)
        cy = random.randint(0, height)
        max_radius = random.randint(50, 150)
        opacity = random.randint(3, 12)
        
        for r in range(0, max_radius, 12):
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], 
                        outline=(255, 255, 255, opacity), width=1)
    
    # 添加古典边框
    border_margin = 25
    # 外边框
    draw.rounded_rectangle([border_margin, border_margin, width - border_margin, height - border_margin],
                          radius=12, outline=(255, 255, 255, 20), width=2)
    # 内边框
    draw.rounded_rectangle([border_margin + 8, border_margin + 8, 
                           width - border_margin - 8, height - border_margin - 8],
                          radius=10, outline=(255, 255, 255, 10), width=1)
    
    # 角落装饰
    corner_size = 30
    corners = [
        (border_margin + 15, border_margin + 15),
        (width - border_margin - 15 - corner_size, border_margin + 15),
        (border_margin + 15, height - border_margin - 15 - corner_size),
        (width - border_margin - 15 - corner_size, height - border_margin - 15 - corner_size)
    ]
    
    for cx, cy in corners:
        draw.rectangle([cx, cy, cx + corner_size, cy + 3], fill=(255, 255, 255, 30))
        draw.rectangle([cx, cy, cx + 3, cy + corner_size], fill=(255, 255, 255, 30))
    
    # 加载字体
    try:
        title_font = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", 52)
        english_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)
        subtitle_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 24)
        desc_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 16)
        tag_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 14)
        small_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 12)
    except:
        title_font = ImageFont.load_default()
        english_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
        tag_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # ========== 左侧 - 平板设备 ==========
    tab_x = 70
    tab_y = 75
    tab_w = 440
    tab_h = 490
    
    draw_modern_tablet(draw, tab_x, tab_y, tab_w, tab_h, (255, 255, 255))
    
    # 顶部导航栏
    nav_h = 55
    draw.rectangle([tab_x + 18, tab_y + 18, tab_x + tab_w - 18, tab_y + 18 + nav_h], 
                  fill=(20, 60, 140))
    
    # Logo和标题
    draw.text((tab_x + 28, tab_y + 28), "🏛️", fill="white", font=desc_font)
    draw.text((tab_x + 55, tab_y + 30), "大运河文化", fill="white", font=desc_font)
    
    # 地图区域
    map_y = tab_y + 18 + nav_h + 15
    map_h = 200
    
    # 地图背景
    draw.rounded_rectangle([tab_x + 25, map_y, tab_x + tab_w - 25, map_y + map_h], 
                          radius=12, fill=(235, 242, 250))
    
    # 绘制运河线路 - 平滑曲线
    canal_points = []
    for i in range(60):
        x = tab_x + 40 + i * 6.5
        y = map_y + 100 + math.sin(i * 0.25) * 40 + math.cos(i * 0.15) * 25
        canal_points.append((int(x), int(y)))
    
    # 绘制运河主体
    for offset in [-3, -1, 1, 3]:
        points = [(x, y + offset) for x, y in canal_points]
        if len(points) > 1:
            draw.line(points, fill=(30, 100, 200, 100 + abs(offset) * 20), width=3)
    
    # 运河中心线
    if len(canal_points) > 1:
        draw.line(canal_points, fill=(40, 120, 220), width=5)
    
    # 城市标记
    cities = [
        (tab_x + 60, map_y + 70, "北京", (220, 60, 60)),
        (tab_x + 150, map_y + 100, "天津", (220, 60, 60)),
        (tab_x + 250, map_y + 65, "济宁", (220, 60, 60)),
        (tab_x + 350, map_y + 110, "扬州", (220, 60, 60)),
        (tab_x + 400, map_y + 85, "杭州", (220, 60, 60))
    ]
    
    for cx, cy, name, color in cities:
        # 外圈
        draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=color, outline="white", width=2)
        # 内圈
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill="white")
        # 名称
        draw.text((cx + 12, cy - 7), name, fill=(60, 60, 60), font=small_font)
    
    # 运河标注
    draw.text((tab_x + 150, map_y + 160), "京杭大运河", fill=(20, 60, 140), font=desc_font)
    draw.text((tab_x + 280, map_y + 160), "1794公里", fill=(100, 100, 100), font=small_font)
    
    # 内容卡片
    cards_y = map_y + map_h + 20
    card_h = 60
    
    content_items = [
        ("🏛️", "历史遗迹", "探访运河沿岸古迹"),
        ("🎭", "文化体验", "感受千年运河文化"),
        ("🚢", "游船之旅", "沉浸式运河游览"),
        ("📚", "知识图谱", "趣味文化学习")
    ]
    
    for i, (icon, title, desc) in enumerate(content_items):
        card_y = cards_y + i * (card_h + 8)
        
        # 卡片背景
        draw.rounded_rectangle([tab_x + 25, card_y, tab_x + tab_w - 25, card_y + card_h], 
                              radius=10, fill=(248, 250, 255))
        
        # 图标背景
        draw.rounded_rectangle([tab_x + 35, card_y + 10, tab_x + 65, card_y + 50], 
                              radius=8, fill=(230, 240, 255))
        draw.text((tab_x + 40, card_y + 15), icon, fill=(20, 60, 140), font=desc_font)
        
        # 标题
        draw.text((tab_x + 80, card_y + 10), title, fill=(40, 40, 40), font=desc_font)
        
        # 描述
        draw.text((tab_x + 80, card_y + 35), desc, fill=(120, 120, 120), font=tag_font)
    
    # ========== 右侧内容 ==========
    content_x = 570
    
    # 品牌标签
    draw.rounded_rectangle([content_x, 100, content_x + 140, 128], radius=14, 
                          fill=(255, 255, 255, 20), outline=(255, 255, 255, 30))
    draw.text((content_x + 15, 104), "CULTURAL APP", fill=(200, 220, 255), font=tag_font)
    
    # 主标题
    draw.text((content_x, 155), "运河", fill="white", font=title_font)
    
    # 英文
    draw.text((content_x, 225), "Grand Canal Heritage", fill=(180, 200, 240), font=english_font)
    
    # 副标题
    draw.text((content_x, 260), "大运河文化主题应用", fill=(255, 255, 255, 220), font=subtitle_font)
    
    # 描述
    draw.text((content_x, 305), "融合传统与现代，探索千年运河文化", fill=(200, 220, 255, 150), font=desc_font)
    
    # 特性列表
    features = [
        ("🌊", "文化探索", "沉浸式运河历史体验"),
        ("📍", "景点导览", "智能路线规划推荐"),
        ("📖", "知识图谱", "趣味文化知识学习"),
        ("🎨", "视觉叙事", "精美插画与动效")
    ]
    
    feature_y = 350
    for i, (icon, title, desc) in enumerate(features):
        y = feature_y + i * 55
        
        # 图标容器
        draw.rounded_rectangle([content_x, y, content_x + 40, y + 40], radius=10, 
                              fill=(255, 255, 255, 15), outline=(255, 255, 255, 25))
        draw.text((content_x + 8, y + 6), icon, fill="white", font=desc_font)
        
        # 标题
        draw.text((content_x + 50, y + 2), title, fill="white", font=desc_font)
        
        # 描述
        draw.text((content_x + 50, y + 25), desc, fill=(200, 220, 255, 130), font=tag_font)
    
    # 设计规范标签
    specs = ["UI设计", "文化融合", "视觉设计", "交互体验"]
    spec_y = 575
    
    for i, spec in enumerate(specs):
        x = content_x + i * 100
        draw.rounded_rectangle([x, spec_y, x + 90, spec_y + 28], radius=14, 
                              fill=(255, 255, 255, 15), outline=(255, 255, 255, 30))
        draw.text((x + 12, spec_y + 5), spec, fill=(200, 220, 255, 160), font=tag_font)
    
    # 底部品牌
    draw.rounded_rectangle([content_x, height - 55, content_x + 200, height - 30], 
                          radius=12, fill=(255, 255, 255, 15))
    draw.text((content_x + 15, height - 50), "UI/UX Design by 汪涛", fill=(200, 220, 255, 180), font=tag_font)
    
    # 保存
    img = img.convert('RGB')
    img.save("E:/汪涛/portfolio/运河/卡片展示.png", quality=95, dpi=(300, 300))
    print("运河卡片已生成 - 高级版")

if __name__ == "__main__":
    random.seed(42)
    create_travel_card()
    create_canal_card()
    print("所有高级版卡片生成完成！")