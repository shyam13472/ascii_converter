from PIL import Image, ImageDraw, ImageFont

def auto_dimming_intensity(pixels, dsize):
    avg = 0
    count = 0
    for row in range(0, dsize[1], 3):
        for col in range(0, dsize[0], 3):
            rgb = pixels[col, row]
            r, g, b = rgb[0], rgb[1], rgb[2]
            brightness = 0.299 * r + 0.587 * g + 0.114 * b
            avg += brightness
            count += 1
    avg /= count
    return 4.5 + avg / 90

print('Enter the photo name:')
name = input()

try:
    image = Image.open(name)
    print('Successfully opened.')
except FileNotFoundError:
    print('File not found.')
    exit()

print('Enter how many times you want to compress the image:')
dratio = int(input())

size = image.size
image.thumbnail((size[0] // dratio, size[1] // dratio))
dsize = image.size

pixels = image.load()

print('Enter the dimming intensity (4.5 - 255.0) or write "auto" to choose it automaticly:')
dimming_intensity = input()
if dimming_intensity == 'auto':
    dimming_intensity = auto_dimming_intensity(pixels, dsize)
    print(f'Dimming intensity chosen: {dimming_intensity}')
else:
    dimming_intensity = float(dimming_intensity)
    if dimming_intensity < 4.5 or dimming_intensity > 255.0:
        print('Value is incorrect.')
        exit()

font = ImageFont.truetype('lucidaconsole.ttf', 8)
ascii_img = Image.new('RGB', (dsize[0] * 6, dsize[1] * 6), color='white')
colour_img = Image.new('RGB', (dsize[0] * 6, dsize[1] * 6), color='white')
drawing = ImageDraw.Draw(ascii_img)
drawing_colour = ImageDraw.Draw(colour_img)

f = open(f'{name.split(".")[-2]}_ascii.txt', 'wb')
ascii_symbols = 'Ñ@#W9876543210!abc;:+=-,._                               '
w, h = 0, 0
for row in range(dsize[1]):
    for col in range(dsize[0]):
        rgb = pixels[col, row]
        r, g, b = rgb[0], rgb[1], rgb[2]
        brightness = 0.299 * r + 0.587 * g + 0.114 * b

        symbol = ascii_symbols[int(brightness / dimming_intensity)]

        drawing.text((w, h), symbol, font=font, fill='black')
        drawing_colour.text((w, h), symbol, font=font, fill=rgb)
        w += 6

        f.write(f'{symbol} '.encode('utf-8'))
    f.write('\n'.encode('utf-8'))
    h += 6
    w = 0

f.close()

ascii_img.save(f'{name.split(".")[-2]}_ascii.png')
colour_img.save(f'{name.split(".")[-2]}_ascii_coloured.png')
