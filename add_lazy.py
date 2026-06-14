import re

# 读取HTML文件
with open('E:/汪涛/portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 给所有img标签添加loading="lazy"（如果没有的话）
# 匹配所有img标签，但排除已经有loading属性的
def add_lazy(match):
    tag = match.group(0)
    if 'loading=' not in tag:
        # 在class属性前添加loading="lazy"
        tag = tag.replace('class="', 'loading="lazy" class="')
    return tag

# 匹配所有img标签
content_new = re.sub(r'<img[^>]*>', add_lazy, content)

# 写回文件
with open('E:/汪涛/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content_new)

# 统计懒加载数量
lazy_count = content_new.count('loading="lazy"')
print(f'已添加 {lazy_count} 个懒加载属性')