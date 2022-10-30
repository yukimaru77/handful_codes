from PIL import Image

img = Image.open('無題.png')
#box=(left, upper, right, lower)でcropの引数に指定
img.crop((60, 20, 400, 200)).show()


