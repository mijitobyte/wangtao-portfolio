from PIL import Image, ImageDraw, ImageFont
import math

def create_travel_card():
    """创建旅记项目卡片"""
    width, height = 1200, 630
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 暖橙色
    for y in range(height):
        r = int(249 + (255 - 249) * y / height)
        g = int(115 + (237 - 115) * y / height)
        b = int(22 + (213 - 22) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 装饰元素 - 圆形
    for i in range(5):
        x = 100 + i * 250
        y = 150 + (i % 2) * 80
        radius = 60 + i * 10
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                     fill=(255, 255, 255, 30), outline=None)
    
    # 左侧内容区域
    # 项目名称
    try:
        title_font = ImageFont.truetype("msyh.ttc", 48)
        subtitle_font = ImageFont.truetype("msyh.ttc", 24)
        feature_font = ImageFont.truetype("msyh.ttc", 20)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        feature_font = ImageFont.load_default()
    
    # 标题
    draw.text((80, 180), "旅记", fill="white", font=title_font)
    draw.text((80, 250), "旅行生活社交分享平台", fill="white", font=subtitle_font)
    
    # 特性标签
    features = ["旅伴匹配", "内容分享", "探索发现", "个人中心"]
    for i, feature in enumerate(features):
        x = 80 + (i % 2) * 180
        y = 320 + (i // 2) * 50
        # 标签背景
        draw.rounded_rectangle([x, y, x+150, y+35], radius=15, 
                              fill=(255, 255, 255, 60))
        draw.text((x+15, y+7), feature, fill="white", font=feature_font)
    
    # 右侧 - 手机mockup效果
    phone_x = 700
    phone_y = 80
    phone_w = 200
    phone_h = 400
    
    # 手机外壳
    draw.rounded_rectangle([phone_x, phone_y, phone_x+phone_w, phone_y+phone_h], 
                          radius=20, fill=(255, 255, 255), outline=(200, 200, 200))
    # 屏幕
    screen_margin = 10
    draw.rectangle([phone_x+screen_margin, phone_y+screen_margin+30, 
                   phone_x+phone_w-screen_margin, phone_y+phone_h-screen_margin],
                  fill=(255, 247, 237))
    
    # 屏幕内容模拟
    draw.rectangle([phone_x+20, phone_y+50, phone_x+phone_w-20, phone_y+90], 
                  fill=(249, 115, 22))
    draw.text((phone_x+30, phone_y+55), "旅记", fill="white", font=feature_font)
    
    # 模拟卡片
    for i in range(3):
        card_y = phone_y + 110 + i * 85
        draw.rounded_rectangle([phone_x+15, card_y, phone_x+phone_w-15, card_y+70],
                              radius=8, fill=(255, 255, 255))
        draw.rectangle([phone_x+20, card_y+5, phone_x+60, card_y+65], 
                      fill=(255, 200, 150))
        draw.text((phone_x+70, card_y+15), "旅行故事", fill=(100, 100, 100), font=feature_font)
    
    # 第二个手机
    phone_x2 = 920
    draw.rounded_rectangle([phone_x2, phone_y+40, phone_x2+phone_w, phone_y+phone_h+40],
                          radius=20, fill=(255, 255, 255), outline=(200, 200, 200))
    draw.rectangle([phone_x2+screen_margin, phone_y+70, 
                   phone_x2+phone_w-screen_margin, phone_y+phone_h+40-screen_margin],
                  fill=(255, 240, 230))
    
    # 匹配功能模拟
    draw.rounded_rectangle([phone_x2+20, phone_y+90, phone_x2+phone_w-20, phone_y+130],
                          radius=10, fill=(249, 115, 22))
    draw.text((phone_x2+50, phone_y+95), "旅伴匹配", fill="white", font=feature_font)
    
    # 用户头像模拟
    for i in range(2):
        cx = phone_x2 + 50 + i * 100
        cy = phone_y + 200
        draw.ellipse([cx-25, cy-25, cx+25, cy+25], fill=(255, 200, 150))
        draw.ellipse([cx-15, cy-15, cx+15, cy+15], fill=(249, 115, 22))
    
    # 底部品牌标识
    draw.text((80, height-60), "UI/UX Design by 汪涛", fill=(255, 255, 255, 180), font=feature_font)
    
    img.save("E:/汪涛/portfolio/旅记/卡片展示.png", quality=95)
    print("旅记卡片已生成")

def create_canal_card():
    """创建运河项目卡片"""
    width, height = 1200, 630
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 蓝色系（文化感）
    for y in range(height):
        r = int(30 + (15 - 30) * y / height)
        g = int(64 + (82 - 64) * y / height)
        b = int(175 + (160 - 175) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 装饰元素 - 古典纹样效果
    for i in range(8):
        x = 50 + i * 150
        y = 50 + (i % 3) * 30
        # 波浪线条效果
        points = []
        for j in range(20):
            px = x + j * 7
            py = y + int(math.sin(j * 0.5) * 15)
            points.append((px, py))
        if len(points) > 1:
            draw.line(points, fill=(255, 255, 255, 40), width=2)
    
    try:
        title_font = ImageFont.truetype("msyh.ttc", 48)
        subtitle_font = ImageFont.truetype("msyh.ttc", 24)
        feature_font = ImageFont.truetype("msyh.ttc", 20)
        small_font = ImageFont.truetype("msyh.ttc", 16)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        feature_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # 左侧 - 设备展示
    # 平板设备
    tab_x = 80
    tab_y = 100
    tab_w = 350
    tab_h = 450
    
    draw.rounded_rectangle([tab_x, tab_y, tab_x+tab_w, tab_y+tab_h],
                          radius=15, fill=(255, 255, 255), outline=(180, 190, 200))
    # 屏幕区域
    draw.rectangle([tab_x+10, tab_y+10, tab_x+tab_w-10, tab_y+tab_h-10],
                  fill=(240, 245, 255))
    
    # 顶部导航栏
    draw.rectangle([tab_x+10, tab_y+10, tab_x+tab_w-10, tab_y+50],
                  fill=(30, 64, 175))
    draw.text((tab_x+20, tab_y+15), "大运河文化", fill="white", font=feature_font)
    
    # 地图区域模拟
    draw.rectangle([tab_x+20, tab_y+60, tab_x+tab_w-20, tab_y+200],
                  fill=(200, 220, 240))
    # 运河线路
    points = [(tab_x+40, tab_y+100), (tab_x+100, tab_y+80), 
              (tab_x+180, tab_y+120), (tab_x+260, tab_y+90),
              (tab_x+320, tab_y+140)]
    draw.line(points, fill=(30, 64, 175), width=3)
    
    # 景点标记
    for px, py in [(tab_x+100, tab_y+80), (tab_x+180, tab_y+120), (tab_x+260, tab_y+90)]:
        draw.ellipse([px-8, py-8, px+8, py+8], fill=(200, 50, 50))
        draw.ellipse([px-4, py-4, px+4, py+4], fill=(255, 255, 255))
    
    # 内容卡片
    for i in range(3):
        card_y = tab_y + 220 + i * 70
        draw.rounded_rectangle([tab_x+20, card_y, tab_x+tab_w-20, card_y+55],
                              radius=8, fill=(255, 255, 255))
        draw.rectangle([tab_x+25, card_y+5, tab_x+75, card_y+50],
                      fill=(200, 210, 230))
        draw.text((tab_x+85, card_y+15), "历史文化景点", fill=(80, 80, 80), font=feature_font)
    
    # 右侧内容
    content_x = 500
    
    # 项目名称
    draw.text((content_x, 180), "运河", fill="white", font=title_font)
    draw.text((content_x, 250), "大运河文化主题应用", fill="white", font=subtitle_font)
    draw.text((content_x, 290), "千年运河的文化魅力", fill=(200, 210, 230), font=small_font)
    
    # 特性展示
    features = [
        ("文化探索", "沉浸式体验运河历史"),
        ("景点导览", "智能路线推荐"),
        ("互动体验", "趣味文化知识"),
        ("视觉叙事", "精美的视觉设计")
    ]
    
    for i, (title, desc) in enumerate(features):
        y = 350 + i * 55
        # 图标圆点
        draw.ellipse([content_x, y+5, content_x+12, y+17], fill=(100, 180, 255))
        draw.text((content_x+25, y), title, fill="white", font=feature_font)
        draw.text((content_x+25, y+25), desc, fill=(200, 210, 230), font=small_font)
    
    # 底部品牌标识
    draw.text((content_x, height-60), "UI/UX Design by 汪涛", fill=(200, 210, 230), font=feature_font)
    
    img.save("E:/汪涛/portfolio/运河/卡片展示.png", quality=95)
    print("运河卡片已生成")

if __name__ == "__main__":
    create_travel_card()
    create_canal_card()
    print("所有卡片生成完成！")