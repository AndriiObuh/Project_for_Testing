from typing import Union


class Calc:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not  isinstance(y, (int, float)):
            raise TypeError("Both arg should be numeric")
        if y == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arg should be numeric")
        return x + y


if __name__ == "__main__":
    calc = Calc()


