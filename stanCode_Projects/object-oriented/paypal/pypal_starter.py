
import pypal


def bank():
    jerry_a = pypal.Pypal('YangHung', money=1000, withdraw_limit=700)
    jerry_a.withdraw(1000)
    jerry_a.withdraw(700)
    jerry_a.withdraw(700)
    print(jerry_a.get_money())
    jerry_a.set_username('Jerry')
    jerry_a.withdraw(100)


if __name__ == '__main__':
    bank()

