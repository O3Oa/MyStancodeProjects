from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics()
    # window, ball, zone, score_label
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    while True:
        # update
        graphics.ball.move(vx, vy)
        # check
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
            vx = -vx
        if graphics.ball.y <= 0 or graphics.ball.y+graphics.ball.height > graphics.window.height:
            vy = -vy
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
