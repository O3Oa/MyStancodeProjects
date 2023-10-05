"""
File: img_processing_2.py
Name: Jessica
-------------------------------
This file contains 2 image processing algorithms:
(1.) left_half_darken
(2.) gray_scale
"""


from simpleimage import SimpleImage


def main():
    """
    This file contains 2 image processing algorithms:
    left_half_darken and gray_scale
    """
    img = SimpleImage('images/stop.png')
    img.show()

    gray_scale_img = gray_scale('images/stop.png')
    gray_scale_img.show()


def left_half_darken(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return img: SimpleImage, the image with half horizontal area darken
    """
    darken_img = SimpleImage(filepath)
    for x in range(darken_img.width):
        for y in range(darken_img.height):
            pixel = darken_img.get_pixel(x, y)
            if x < darken_img.width//2:
                pixel.red //= 2
                pixel.green //= 2
                pixel.blue //=2
    return darken_img


def quarter(filepath):
    quarter_img = SimpleImage(filepath)
    for x in range(quarter_img.width):
        for y in range(quarter_img.height):
            pixel = quarter_img.get_pixel(x, y)
            if x < quarter_img.width//2 and y < quarter_img.height//2:
                pixel.red //= 2
                pixel.green //= 2
                pixel.red //= 2
            elif x > quarter_img.width//2 and y > quarter_img.height//2:
                pixel.red //= 2
                pixel.green //= 2
                pixel.red //= 2
            else:
                pixel.red *= 2
                pixel.green *= 2
                pixel.blue *= 2


def gray_scale(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return: SimpleImage, gray scaled image
    """
    gray_image = SimpleImage(filepath)
    for pixel in gray_image:
        avg = (pixel.red+pixel.green+pixel.blue)//3
        pixel.red = avg
        pixel.blue = avg
        pixel.green = avg
    return gray_image


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
