"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Jessica
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    vx = 0
    vy = 0
    count = 0
    while graphics.counter < graphics.bricks_num:
        # update
        if vx == 0 and vy == 0:
            vx = graphics.get___dx()
            vy = graphics.get___dy()
        graphics.ball.move(vx, vy)
        # check
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
            vx = -vx
        if graphics.ball.y <= 0:
            vy = -vy
        if graphics.ball.y+graphics.ball.height > graphics.window.height:
            graphics.back_to_start()
            vx = 0
            vy = 0
            count += 1
            if count >= NUM_LIVES:

                break
        if bouncing(graphics):
            vx = -vx
            vy = -vy
        # pause
        pause(FRAME_RATE)
    if graphics.counter == graphics.bricks_num:
        graphics.win()
    else:
        game_over = GLabel('Game over', x=300, y=300)
        graphics.window.add(game_over)


def bouncing(g):
    r = g.ball_radius
    for i in [0, 2*r]:
        for j in [0, 2*r]:
            ball_detector = g.window.get_object_at(g.ball.x + i, g.ball.y + j)
            # print(ball_detector)
            if ball_detector in g.bricks:
                # print("Remove", ball_detector)
                g.window.remove(ball_detector)
                g.counter += 1
                return True
            elif ball_detector is g.paddle:
                return True
    return False


if __name__ == '__main__':
    main()
