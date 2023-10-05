
WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._n = name
        self._m = money
        self._w_l = withdraw_limit

    def withdraw(self, amount):
        if amount > self._m:
            print('Error')
        elif amount > self._w_l:
            print('Exceed Limit')
        else:
            self._m -= amount
            print(f"{self._n} remains: {self._m}")

    # Setter
    def set_username(self, newname):
        self._n = newname

    # Getter
    def get_money(self):
        return self._m

    # toString Method
    def __str__(self):
        return f"{self._n} remains: {self._m}/Limit:{self._w_l}"


def bank():
    jerry_a = Pypal('YangHung', money=1000, withdraw_limit=700)
    jerry_a.withdraw(1000)
    jerry_a.withdraw(700)
    jerry_a.withdraw(700)
    print(jerry_a)


if __name__ == '__main__':
    bank()