'''
-------------------- DESCRIPTION ------------------
This code takes an input image, and saves a cropped version.

------------------- HELPFUL LINKS -----------------
https://pillow.readthedocs.io/en/latest/index.html
https://jdhao.github.io/2019/07/20/pil_jpeg_image_quality/

---------------------------------------------------
'''

from PIL import Image

im = Image.open(r"C:\Users\tbart\Desktop\1past file\Dragon.jpg")
#im.show() #for testing only

(left, upper, right, lower) = (720, 720, 1440, 1440)

im_crop = im.crop((left, upper, right, lower))

#im_crop.show() #for testing only
im_crop.save(r"C:\Users\tbart\Desktop\1past file\Dragon_x.jpg", quality=95)