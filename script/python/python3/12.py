#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
	return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/usr/share/wine/fonts/arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)		# draw over this image
# 填充每个像素:
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())
# 输出文字:
imageName = ''
for t in range(4):
	imageNameChar = rndChar()
	imageName += imageNameChar
	# PIL.ImageDraw.Draw.text(x, y, text, fill=None, font=None, anchor=None)
	draw.text((60 * t + random.randint(5,35), random.randint(5,25)), imageNameChar, font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save(imageName+'.png', 'png')
