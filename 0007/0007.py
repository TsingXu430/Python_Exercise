from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

image = Image.new('RGB', (50 * 4, 50), (255, 255, 255))

font = ImageFont.truetype('times.ttf', 24)

draw = ImageDraw.Draw(image)


def rand_char():
    return chr(random.randint(65, 90))


def rand_color():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


for x in range(4):
    draw.text((50 * x + 10, 10), rand_char(), rand_color(), font)

image = image.filter(ImageFilter.BLUR)
image.save('result.jpg')
image.show()
