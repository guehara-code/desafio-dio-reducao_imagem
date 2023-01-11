from PIL import Image

im = Image.open('tiger-jpg.jpg')

print(im)
print(im.height)
print(im.width)

im_gray = Image.new(mode="RGB", size=(im.width, im.height))
im_gray.save("im_gray.png", "PNG")
gray_pixels = []

im_black_white = Image.new(mode="RGB", size=(im.width, im.height))
im_black_white.save("im_black_white.png", "PNG")
black_white_pixels = []

for index, color in enumerate(im.getdata(band=None)):
    #print("index:" + str(index))
    #print(color)
    #print(color[0])
    gray = int((color[0] + color[1] + color[2])/3)
    gray_pixels.append((gray, gray, gray))
    if gray > 128:
        gray = 255
    else:
        gray = 0
    black_white_pixels.append((gray, gray, gray))
    #print(gray_pixels[index])

im_gray.putdata(gray_pixels, scale=1.0, offset=0.0)
im_gray.save("im_gray.png", "PNG")

im_black_white.putdata(black_white_pixels, scale=1.0, offset=0.0)
im_black_white.save("im_black_white.png", "PNG")
    


