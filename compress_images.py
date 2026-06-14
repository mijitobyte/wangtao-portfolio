from PIL import Image
import os

def compress_image(input_path, output_path, quality=80, max_size=(1920, 1080)):
    """压缩图片"""
    try:
        with Image.open(input_path) as img:
            # 转换为RGB（如果是RGBA）
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # 调整尺寸
            if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # 保存压缩后的图片
            if output_path.endswith('.png'):
                img.save(output_path, 'PNG', optimize=True)
            else:
                img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            # 返回压缩后的大小
            return os.path.getsize(output_path)
    except Exception as e:
        print(f"压缩失败 {input_path}: {e}")
        return 0

def batch_compress(directory, quality=75, max_size=(1920, 1080)):
    """批量压缩目录中的图片"""
    total_before = 0
    total_after = 0
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(directory, filename)
            original_size = os.path.getsize(filepath)
            total_before += original_size
            
            # 压缩图片
            new_size = compress_image(filepath, filepath, quality, max_size)
            total_after += new_size
            
            if new_size > 0:
                reduction = (1 - new_size / original_size) * 100
                print(f"{filename}: {original_size/1024:.1f}KB → {new_size/1024:.1f}KB (减少 {reduction:.1f}%)")
    
    print(f"\n总计: {total_before/1024/1024:.2f}MB → {total_after/1024/1024:.2f}MB")
    print(f"减少: {(1-total_after/total_before)*100:.1f}%")

if __name__ == "__main__":
    print("=== 压缩旅记项目图片 ===")
    batch_compress("E:/汪涛/portfolio/旅记", quality=70, max_size=(1600, 1200))
    
    print("\n=== 压缩运河项目图片 ===")
    batch_compress("E:/汪涛/portfolio/运河", quality=70, max_size=(1600, 1200))
    
    print("\n压缩完成！")