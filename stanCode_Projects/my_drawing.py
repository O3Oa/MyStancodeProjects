"""
File: 
Name:Jessica
----------------------
TODO:
Christmas is coming!
Dear Jerry, Dear AO, Dear All, wish you all have a 'Meowy Christmas!'
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLabel, GLine, GPolygon
from campy.graphics.gwindow import GWindow

CAT_COLOR = "cornsilk"

def main():
    """
    TODO: Draw a Christmas Card!
    """
    window = GWindow(900, 700, title='Meowy Christmas!')

    x = 150
    y = 150
    fw = 300
    fh = 320
    # Hat
    hat_top = GPolygon()
    hat_top.add_vertex((x + 230, y - 20))
    hat_top.add_vertex((x + 120, y - 115))
    hat_top.add_vertex((x + 110, y - 120))
    hat_top.add_vertex((x + 100, y - 123))
    hat_top.add_vertex((x + 90, y - 125))
    hat_top.add_vertex((x + 80, y - 120))
    hat_top.add_vertex((x + 70, y - 115))
    hat_top.add_vertex((x + 50, y - 95))
    hat_top.add_vertex((x - 50, y + 30))
    hat_top.filled = True
    hat_top.fill_color = "red"

    hat_ball = GOval(60, 60, x=x - 50 - 10, y=y + 30 - 30)
    hat_ball.filled = True
    hat_ball.fill_color = "snow"

    hat_bottom = GPolygon()
    hat_bottom.add_vertex((x + 33, y + 60))
    hat_bottom.add_vertex((x + fw - 100 + 59, y + 60))
    hat_bottom.add_vertex((x + fw - 100 + 59, y - 10))
    hat_bottom.add_vertex((x + fw - 100 + 40, y - 25))
    hat_bottom.add_vertex((x + 85, y - 20))
    hat_bottom.add_vertex((x + 60, y - 15))
    hat_bottom.add_vertex((x + 40, y - 10))
    hat_bottom.add_vertex((x + 20, y + 15))
    hat_bottom.filled = True
    hat_bottom.fill_color = "snow"

    hat_line = GLine(x + 30, y, x + 20, y - 20)
    hat_line.line_width = 5
    # Face
    face = GOval(fw, fh, x=x, y=y)
    face.filled = True
    face.fill_color = CAT_COLOR
    # Eyes 100, 75
    eye_left = GOval(15, 15, x=x + 100 - 4, y=y + 75 - 4)
    eye_left.filled = True
    eye_left.fill_color = "black"
    eye_right = GOval(15, 15, x=x + fw - 100 - 4, y=y + 75 - 4)
    eye_right.filled = True
    eye_right.fill_color = "black"
    # Nose / Mouth
    nose = GOval(10, 10, x=x + 150 - 5, y=y + 100 - 5)
    nose.filled = True
    nose.fill_color = "pink"
    mouth_left = GArc(300, 150, 270, 90, x=x + 150 - 150, y=y + 100 - 2.5 - 30)
    mouth_right = GArc(300, 150, 180, 90, x=x + 150, y=y + 100 - 2.5 - 30)
    # Ear
    ear_left = GPolygon()
    ear_left.add_vertex((x + 33, y + 60))  # left
    ear_left.add_vertex((x + 85, y + 15))  # right
    ear_left.add_vertex((x + 40, y + 5))  # top
    ear_left.filled = True
    ear_left.fill_color = CAT_COLOR

    ear_right = GPolygon()
    ear_right.add_vertex((x + fw - 100 + 15, y + 15))  # left
    ear_right.add_vertex((x + fw - 100 + 66, y + 60))  # right
    ear_right.add_vertex((x + fw - 100 + 59, y + 5))  # top
    ear_right.filled = True
    ear_right.fill_color = CAT_COLOR
    # Whiskers
    whisker1 = GLine(x - 5, y + 70, x + 60, y + 85)
    whisker2 = GLine(x - 10, y + 105, x + 60, y + 95)
    whisker3 = GLine(x + fw - 100 + 40, y + 85, x + fw - 100 + 40 + 65, y + 70)
    whisker4 = GLine(x + fw - 100 + 40, y + 95, x + fw - 100 + 40 + 70, y + 105)
    # Blush
    blush_left = GOval(40, 30, x=x + 20, y=y + 110)
    blush_left.filled = True
    blush_left.fill_color = "pink"
    blush_right = GOval(40, 30, x=x + fw - 100 + 40, y=y + 110)
    blush_right.filled = True
    blush_right.fill_color = "pink"
    blush_line1 = GLine(x + 30, y + 130, x + 35, y + 120)
    blush_line2 = GLine(x + 40, y + 130, x + 45, y + 120)
    blush_line3 = GLine(x + fw - 100 + 40 + 15, y + 130, x + fw - 100 + 40 + 20, y + 120)
    blush_line4 = GLine(x + fw - 100 + 40 + 25, y + 130, x + fw - 100 + 40 + 30, y + 120)
    # Eyebrow
    eyebrow_left = GLine(x + 75, y + 65, x + 95, y + 50)
    eyebrow_right = GLine(x + fw - 100 + 5, y + 50, x + fw - 100 + 25, y + 65)
    # Saliva
    saliva_x = x + 110
    saliva_y = y + 140
    saliva = GPolygon()
    saliva.add_vertex((saliva_x, saliva_y))
    saliva.add_vertex((saliva_x - 10, saliva_y + 60))
    saliva.add_vertex((saliva_x + 10, saliva_y + 60))
    saliva.filled = True
    saliva.color = "skyblue"
    saliva.fill_color = "skyblue"
    saliva_tail = GOval(20, 20, x=saliva_x - 10, y=saliva_y + 60 - 10)
    saliva_tail.filled = True
    saliva_tail.color = "skyblue"
    saliva_tail.fill_color = "skyblue"

    # Cheek
    cheek = GArc(130, 65, 190, 160, x + 85, y + fh - 60)

    # Scarf
    scarf = GPolygon()
    scarf.add_vertex((x + 30, y + fh - 70))
    scarf.add_vertex((x + 20, y + fh))
    scarf.add_vertex((x + 22, y + fh + 10))
    scarf.add_vertex((x + 22, y + fh + 20))
    scarf.add_vertex((x + 25, y + fh + 30))
    scarf.add_vertex((x + 30, y + fh + 35))
    scarf.add_vertex((x + 100, y + fh + 40))
    scarf.add_vertex((x + 170, y + fh + 45))
    scarf.add_vertex((x + 200, y + fh + 43))
    scarf.add_vertex((x + fw - 30, y + fh + 25))
    scarf.add_vertex((x + fw - 30, y + fh - 70))
    scarf.filled = True
    scarf.fill_color = "rosybrown"

    scarf_tail = GPolygon()
    scarf_tail.add_vertex((x + fw - 80, y + fh - 70))
    scarf_tail.add_vertex((x + fw - 80, y + fh + 70))
    scarf_tail.add_vertex((x + fw - 20, y + fh + 70))
    scarf_tail.add_vertex((x + fw - 15, y + fh + 60))
    scarf_tail.add_vertex((x + fw - 10, y + fh + 30))
    scarf_tail.add_vertex((x + fw - 15, y + fh))
    scarf_tail.add_vertex((x + fw - 30, y + fh - 70))
    scarf_tail.filled = True
    scarf_tail.fill_color = "rosybrown"

    scarf_ball = GOval(70, 70, x=x + fw - 85, y=y + fh + 60)
    scarf_ball.filled = True
    scarf_ball.fill_color = "lavender"

    window.add(hat_top)
    window.add(hat_ball)
    window.add(hat_bottom)
    window.add(hat_line)
    window.add(ear_left)
    window.add(ear_right)
    window.add(scarf)
    window.add(scarf_tail)
    window.add(face)
    window.add(eye_left)
    window.add(eye_right)
    window.add(nose)
    window.add(mouth_left)
    window.add(mouth_right)
    window.add(whisker1)
    window.add(whisker2)
    window.add(whisker3)
    window.add(whisker4)
    window.add(blush_left)
    window.add(blush_right)
    window.add(blush_line1)
    window.add(blush_line2)
    window.add(blush_line3)
    window.add(blush_line4)
    window.add(eyebrow_left)
    window.add(eyebrow_right)

    window.add(saliva)
    window.add(saliva_tail)
    window.add(cheek)
    window.add(scarf_ball)

    # words
    xmas = GLabel('Meowy  Christmas', x=480, y=480)
    xmas.color = 'green'
    xmas.font = 'Courier-40-bold'
    window.add(xmas)

    # heart
    heart = GLabel('♥', x=607, y=490)
    heart.color = 'tomato'
    heart.font = 'Courier-60-bold'
    window.add(heart)

    # bowl
    bowl_1 = GArc(70, 50, 0, 180, 700, 350)
    bowl_2 = GArc(70, 50, 180, 180, 700, 350)
    bowl_3 = GArc(90, 55, 180, 180, 690, 375)
    bowl_4 = GLine(700, 360, 690, 389)
    bowl_5 = GLine(770, 360, 780, 389)
    window.add(bowl_1)
    window.add(bowl_2)
    window.add(bowl_3)
    window.add(bowl_4)
    window.add(bowl_5)

    # bowl name
    jessica = GLabel('Jessica', x=703, y=400)
    jessica.color = 'steelblue'
    jessica.font = 'Dialog-18'
    window.add(jessica)

    #tree
    tree3 = GPolygon()
    tree3.add_vertex((610, 190))
    tree3.add_vertex((510, 300))
    tree3.add_vertex((710, 300))
    tree3.filled = True
    tree3.fill_color = 'darkolivegreen'
    window.add(tree3)

    tree2 = GPolygon()
    tree2.add_vertex((610, 130))
    tree2.add_vertex((530, 220))
    tree2.add_vertex((690, 220))
    tree2.filled = True
    tree2.fill_color = 'olivedrab'
    window.add(tree2)

    tree1 = GPolygon()
    tree1.add_vertex((610, 80))
    tree1.add_vertex((540, 150))
    tree1.add_vertex((680, 150))
    tree1.filled = True
    tree1.fill_color = 'olive'
    window.add(tree1)

    tree4 = GRect(60, 100, x=580, y=300)
    tree4.filled = True
    tree4.fill_color = 'sienna'
    window.add(tree4)

    tree5 = GOval(15, 15, x=528, y=150)
    tree5.filled = True
    tree5.fill_color = 'lightpink'
    tree6 = GOval(15, 15, x=677, y=150)
    tree6.filled = True
    tree6.fill_color = 'khaki'
    tree7 = GOval(15, 15, x=518, y=220)
    tree7.filled = True
    tree7.fill_color = 'deepskyblue'
    tree8 = GOval(15, 15, x=687, y=220)
    tree8.filled = True
    tree8.fill_color = 'fuchsia'
    tree9 = GOval(15, 15, x=498, y=300)
    tree9.filled = True
    tree9.fill_color = 'lavender'
    tree10 = GOval(15, 15, x=707, y=300)
    tree10.filled = True
    tree10.fill_color = 'yellow'
    window.add(tree5)
    window.add(tree6)
    window.add(tree7)
    window.add(tree8)
    window.add(tree9)
    window.add(tree10)

    # point = GRect(60, 60, x=580, y=50)
    # window.add(point)

    star = GPolygon()
    star.add_vertex((610, 50))
    star.add_vertex((602, 72))
    star.add_vertex((580, 72))
    star.add_vertex((595, 85))
    star.add_vertex((588, 110))
    star.add_vertex((610, 92))
    star.add_vertex((632, 110))
    star.add_vertex((625, 85))
    star.add_vertex((640, 72))
    star.add_vertex((618, 72))
    star.filled = True
    star.fill_color = 'gold'
    window.add(star)



if __name__ == '__main__':
    main()
