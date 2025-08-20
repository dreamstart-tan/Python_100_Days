from PIL import Image,ImageFilter

im = Image.open(r'D:\Py100\Python_100_Days\Week4_LXF\res\packages\PIL\test.jpg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpg')










