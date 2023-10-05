from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

 # 常數常常扮演 keyword argument的初始值
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(width=window_width, height=window_height)
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.set_ball_position()
        self.window.add(self.ball)

        self.zone = GRect(zone_width, zone_height,
                          x=(self.window.width-zone_width)/2, y=(self.window.height-zone_height)/2)
        self.zone.color = 'blue'
        self.window.add(self.zone)

    def get_vx(self):
        return random.randint(0, MAX_SPEED)

    def get_vy(self):
        return random.randint(MIN_Y_SPEED, MAX_SPEED)

    #重置球的初始位置
    #class要呼叫自己的method要加self.method
    def set_ball_position(self):
        self.ball.x = random.randint(0, self.window.width-self.ball.width)
        self.ball.y = random.randint(0, self.window.height-self.ball.height)


        # Create zone

        # Create ball and initialize velocity/position

        # Initialize mouse listeners

        pass
