"""
File: blur.py
Name: Jessica
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def min(a, b):
    if a <= b:
        return a
    else:
        return b


def max(a, b):
    if a >= b:
        return a
    else:
        return b


def blur(img):
    """
    Blur the image with 4 for loop
    """
    new_img = img.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = new_img.get_pixel(x, y)
            count = 0  # neighbor number
            r = 0
            g = 0
            b = 0
            # Check boundary to avoid accessing non-existing pixels
            for i in range(max(0, x - 1), min(img.width, x + 1)):
                for j in range(max(0, y - 1), min(img.height, y + 1)):
                    neighbor_pixel = img.get_pixel(i, j)
                    r += neighbor_pixel.red
                    g += neighbor_pixel.green
                    b += neighbor_pixel.blue
                    count += 1
            new_pixel.red = r / count
            new_pixel.green = g / count
            new_pixel.blue = b / count

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
