#!/bin/bash

# 部署脚本 - 将作品集网站部署到GitHub Pages

echo "准备部署UI/UX作品集网站..."

# 检查是否安装了git
if ! command -v git &> /dev/null; then
    echo "错误：未安装Git。请先安装Git。"
    exit 1
fi

# 初始化Git仓库（如果尚未初始化）
if [ ! -d ".git" ]; then
    echo "初始化Git仓库..."
    git init
fi

# 添加所有文件
echo "添加文件到Git..."
git add .

# 提交更改
echo "提交更改..."
git commit -m "更新UI/UX作品集网站"

# 检查是否设置了远程仓库
if ! git remote get-url origin &> /dev/null; then
    echo "提示：请设置远程仓库以部署到GitHub Pages"
    echo "运行：git remote add origin <你的GitHub仓库URL>"
    echo "然后运行：git push -u origin main"
    echo ""
    echo "或者，你可以手动将文件上传到任何静态托管服务。"
else
    # 推送到远程仓库
    echo "推送到远程仓库..."
    git push origin main
    
    echo ""
    echo "部署完成！"
    echo "请在GitHub仓库设置中启用GitHub Pages。"
    echo "网站将在几分钟后上线。"
fi

echo ""
echo "本地预览："
echo "1. 运行 'python server.py' 启动本地服务器"
echo "2. 在浏览器中访问 http://localhost:8080"