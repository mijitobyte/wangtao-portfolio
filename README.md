# UI/UX 作品集网站

这是汪涛的UI/UX设计师求职作品集网站，展示了两个UI设计项目：

1. **旅记** - 旅行生活社交分享平台
2. **运河** - 大运河文化主题应用

## 如何运行

### 方法一：直接打开HTML文件
1. 双击 `index.html` 文件
2. 在浏览器中查看网站

### 方法二：使用本地服务器（推荐）
1. 确保已安装Python
2. 在终端中运行：
   ```bash
   python server.py
   ```
3. 在浏览器中访问 `http://localhost:8080`

## 文件结构

```
portfolio/
├── index.html          # 主页面
├── styles.css          # 自定义样式
├── script.js           # JavaScript交互
├── server.py           # 本地服务器脚本
├── 旅记/               # 旅记项目图片
│   ├── 主页.jpg
│   ├── 全部.jpg
│   ├── 09-访客身份登录.jpg
│   ├── 14-个人首页.jpg
│   ├── 49-发现-短途游.jpg
│   └── 55-设置.jpg
└── 运河/               # 运河项目图片
    ├── 0C8C65A9F02874A642B78D62080F42D6.png
    ├── 0D1B38E943D61D705349B92281D017A4.png
    ├── 416B7B095847CF2049CD9187B1408970.png
    ├── 5CFA9DD6839037A6DFFEA025287C71A5.png
    └── C29A2253AB11B796EFD62E8D0B60ADF9.png
```

## 设计系统

- **风格**: Motion-Driven（动画驱动）
- **配色**: 单色 + 蓝色强调色
- **字体**: Archivo / Space Grotesk
- **布局**: Portfolio Grid（作品集网格）

## 功能特性

- 响应式设计，支持移动端和桌面端
- 项目详情弹窗展示
- 平滑滚动动画
- 移动端菜单
- 键盘导航支持（ESC关闭弹窗）

## 技术栈

- HTML5
- Tailwind CSS（通过CDN）
- 原生JavaScript
- Google Fonts

## 浏览器支持

- Chrome（推荐）
- Firefox
- Safari
- Edge

## 注意事项

- 图片路径已配置为相对路径
- 建议使用本地服务器运行以获得最佳体验
- 网站支持键盘导航（Tab键切换，ESC键关闭弹窗）