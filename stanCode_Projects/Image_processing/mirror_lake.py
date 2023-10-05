"""
File: mirror_lake.py
Name: Jessica
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: Image of lake
    :return: mirror lake image, symmetrical up and down.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    b_img = SimpleImage.blank(original_mt.width, original_mt.height*2)
    b_img.show()

    for x in range(original_mt.width):
        for y in range(original_mt.height):
            colored_pixel = original_mt.get_pixel(x, y)

            blank_pixel1 = b_img.get_pixel(x, y)
            blank_pixel1.red = colored_pixel.red
            blank_pixel1.green = colored_pixel.green
            blank_pixel1.blue = colored_pixel.blue

            blank_pixel2 = b_img.get_pixel(x, b_img.height-1-y)
            blank_pixel2.red = colored_pixel.red
            blank_pixel2.green = colored_pixel.green
            blank_pixel2.blue = colored_pixel.blue
    return b_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
