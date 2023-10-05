"""
File:  deaw_line
Name:Jessica
-------------------------
TODO:
1st click draw a circle
2nd click draw a line from 1st point to 2nd point and remove the circle which been drawn when 1st click
2 clicks are one round and keep this mode when mouse click!
"""

from campy.graphics.gobjects import GOval, GLine, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
Circle = GOval(SIZE, SIZE)
TIMES = 0
CIRCLE = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(two_point_one_line)


def two_point_one_line(event):
    global TIMES, CIRCLE
    if TIMES == 0:  # odd click
        CIRCLE = GOval(SIZE, SIZE)
        window.add(CIRCLE, event.x-SIZE/2, event.y-SIZE/2)
        TIMES = 1  # even click
    else:
        line = GLine(CIRCLE.x, CIRCLE.y, event.x, event.y)
        window.add(line)
        window.remove(CIRCLE)
        TIMES = 0


if __name__ == "__main__":
    main()
