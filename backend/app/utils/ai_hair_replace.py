from PIL import Image, ImageDraw, ImageFont
import os

def replace_hair(image_path):
    img = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Dummy effect — real case would use a deep learning model
    draw.rectangle([50, 20, 250, 150], fill=(60, 50, 50, 200))
    
    result = Image.alpha_composite(img, overlay)
    result_path = os.path.join("results", os.path.basename(image_path))
    result.convert("RGB").save(result_path)
    return result_path