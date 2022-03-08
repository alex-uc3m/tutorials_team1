class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return "Error! --> " + str(self.message)

def add(x,y):
    for n in (x, y):
        if not isinstance(n, int) or not isinstance(n, float):
            raise CustomException("Must be int or float for add")

    return x+y

def subtract(x,y):
    for n in (x, y):
        if not isinstance(n, int) or not isinstance(n, float):
            raise CustomException("Must be int or float for subtract")

    return x-y

def multiply(x,y):
    for n in (x, y):
        if not isinstance(n, int) or not isinstance(n, float):
            raise CustomException("Must be int or float for multiply")

    return x*y

def divide(x,y):
    for n in (x, y):
        if not isinstance(n, int) or not isinstance(n, float):
            raise CustomException("Must be int or float for divide")

    return x/y

if __name__ == '__main__':
    x, y = 12, 4
    print(add(x, y))
    print(add(x, "a"))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))