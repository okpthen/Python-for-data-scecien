class calculator:

    def __init__(self, object):
        self.object = object

    def __add__(self, object) -> None:
        self.object = [x + object for x in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        self.object = [x * object for x in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        self.object = [x - object for x in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.object = [x / object for x in self.object]
            print(self.object)
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
