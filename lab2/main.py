import requests
from lab2.lab_python_oop.modules.circle import Circle
from lab2.lab_python_oop.modules.rectangle import Rectangle
from lab2.lab_python_oop.modules.square import Square


def main():
    N = 2

    rectangle = Rectangle(N, N, "фиолетовый")
    circle = Circle(N, "красный")
    square = Square(N, "желтый")

    print(rectangle)
    print(circle)
    print(square)

    res = requests.get('https://vk.com')

    print(res.status_code)

if __name__ == "__main__":
    main()