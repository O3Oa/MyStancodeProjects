"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Name: Jessica
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=self.window_width/2-paddle_width/2, y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.paddle_width = paddle_width

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball_x = self.window_width/2-ball_radius
        self.ball_y = window_height/2-ball_radius
        self.ball_radius = ball_radius
        self.__dx = 0
        self.__dy = 0
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        self.counter = 0
        onmouseclicked(self.move_ball)
        onmousemoved(self.move_paddle)
        # Draw bricks
        # bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT, y=BRICK_OFFSET)
        # bricks.filled = True
        # self.window.add(bricks)
        # bricks2 = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=BRICK_WIDTH+BRICK_SPACING, y=BRICK_OFFSET)
        # bricks3 = GRect(BRICK_WIDTH, BRICK_HEIGHT, y=BRICK_OFFSET+BRICK_HEIGHT+BRICK_SPACING)
        # self.window.add(bricks2)
        # self.window.add(bricks3)

        lst = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        self.bricks = []
        self.bricks_num = brick_cols * brick_rows
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height,
                              x=(brick_width+brick_spacing)*i, y=brick_offset+(brick_height+brick_spacing)*j)
                brick.filled = True
                brick.fill_color = lst[j//2 % len(lst)]
                self.bricks.append(brick)
                self.window.add(brick)

    def move_paddle(self, event):
        if self.paddle_width/2 <= event.x <= self.window_width-self.paddle_width/2:
            self.paddle.x = event.x - self.paddle_width/2
        elif event.x < self.paddle_width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window_width-self.paddle_width

    def move_ball(self, event):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        # print('click', self.__dx, self.__dy)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        # while True:
        #     self.ball.move(self.__dx, self.__dy)
        #     pause(10)

    def back_to_start(self):
        self.ball.x = self.ball_x
        self.ball.y = self.ball_y
        self.__dx = 0
        self.__dy = 0

    def get___dx(self):
        return self.__dx

    def get___dy(self):
        return self.__dy

    def win(self):
        win_info = GLabel('Win!', 300, 400)
        self.window.add(win_info)




