from simpleimage import SimpleImage

def main():
    image_name = input('enter an image name: ')
    image = SimpleImage('images/' + image_name)
    image.show()
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            sepia_pixel(pixel)
    image.show()

def sepia_pixel(pixel):
    red = pixel.red
    green = pixel.green
    blue = pixel.blue
    pixel.red = 0.393 * red + 0.769 * green + 0.189 * blue
    pixel.green = 0.349 * red + 0.686 * green + 0.168 * blue
    pixel.blue = 0.272 * red + 0.534 * green + 0.131 * blue

if __name__ == '__main__':
    main()
