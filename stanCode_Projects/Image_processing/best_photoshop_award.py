"""
File: best_photoshop_award.py
Name: Jessica
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def combine(m, bg):
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = m.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green)//3
            if avg == 255:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return m


def main():
    """
    創作理念：Elephant King🐘
    """
    m = SimpleImage('image_contest/masu.jpg')
    bg = SimpleImage('image_contest/lionking.jpg')
    b_bg = SimpleImage.blank(bg.width, bg.height)

    for x in range(m.width):
        for y in range(m.height):
            blank = b_bg.get_pixel(x, y)
            colored_pixel = m.get_pixel(x, y)
            avg = (colored_pixel.red + colored_pixel.green + colored_pixel.blue) // 3
            is_pink = avg >= 150 and (colored_pixel.red > (colored_pixel.green + colored_pixel.blue) // 1.9)
            is_pink_wall = colored_pixel.red < 245 and colored_pixel.green > 150 and (colored_pixel.green - colored_pixel.blue > 5)
            if is_pink and not is_pink_wall:
                is_masu = True  # masu is my pink elephant's name, 麻糬 in Chinese
            else: # pick well
                is_masu = False  # masu is 5 years old, masu's birthday is same with me at Sep 4th
            # is_masu = colored_pixel.red > (colored_pixel.green+colored_pixel.blue)//1.75 or (colored_pixel.red > 200 and (colored_pixel.blue - colored_pixel.green > 10))
            if avg < 150 or is_masu:
            # if is_masu:
                blank.red = colored_pixel.red
                blank.green = colored_pixel.green
                blank.blue = colored_pixel.blue
    # b_bg.show()
    combined_img = combine(b_bg, bg)
    combined_img.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
