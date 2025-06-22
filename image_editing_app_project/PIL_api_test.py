from PIL import Image, ImageFilter, ImageEnhance
with Image.open("image_editing_app_project/test_image.png") as pic:
    pic.show()
    
    saturate = ImageEnhance.Color(pic)
    saturate = saturate.enhance(1.2)
    saturate.show()
    
    black_white = pic.convert("L")
    black_white.save("image_editing_app_project/gray_pic.png")
    black_white.show()
    
    mirror = pic.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.show()