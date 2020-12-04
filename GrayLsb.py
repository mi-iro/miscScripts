import PIL.Image as Image

path='low.bmp'

img = Image.open(path)
img_tmp = img.copy()
pix = img_tmp.load()
width,height = img_tmp.size
for w in range(width):
   for h in range(height):
      if pix[w,h]&1 == 0:
         pix[w,h] = 0
      else:
         pix[w,h] = 255
img_tmp.save('ans.jpg')
#inplace