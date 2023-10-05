"""
File: bouncing_ball
Name:Jessica
-------------------------
TODO:
When mouse click, the ball fall until the floor and rebound up
The speed after strike reduce to 90% and of course be reversed
Repeat falling and rebound until the ball outsize the window
First three clicks can trigger this event
When mouseclick more then three times, the ball won't do anything
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
ball = GOval(SIZE, SIZE)
COUNT = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'blue'
    window.add(ball, START_X, START_Y)
    onmouseclicked(bouncing)


def bouncing(event):
    vy = 0
    global GRAVITY, REDUCE, COUNT
    if COUNT < 3:
        while True:
            ball.move(VX, vy)
            if ball.x < window.width:
                if ball.y+SIZE > window.height:
                    vy = -vy * REDUCE
                vy += GRAVITY
                pause(10)
            else:
                COUNT += 1
                break
        window.remove(ball)
        window.add(ball, START_X, START_Y)


if __name__ == "__main__":
    main()
