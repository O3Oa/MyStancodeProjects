from robot import Robot3
from campy.graphics.gwindow import GWindow

print('I am in robot_starter.py ["__name__"]:', __name__)


def main():
    window = GWindow()
    r1 = Robot3(183, 70, 'yellow', color3='purple')
    rect1 = r1.give_me_a_rect(500)
    window.add(rect1)
    ball1 = r1.give_me_a_ball(200)
    window.add(ball1)
    r1.start_count()
    print(r1.c)
    r1.say_hi()

    # r1 = Robot2(183, 70, count2=5)
    # r1.start_count()
    # ball1 = r1.give_me_a_ball(300)
    # window.add(ball1)
    # r1 = Robot(183, 70, color='magenta')
    # ball1 = r1.give_me_a_ball(400)
    # r1.self_intro()
    # r1.bmi()
    # Robot.say_hi()
    # r2 = Robot(160, 50)
    # ball2 = r2.give_me_a_ball(300)
    # r2.self_intro()
    # r2.bmi()
    # Robot.say_hi()
    #
    # window.add(ball1)
    # window.add(ball2)


if __name__ == '__main__':
    main()