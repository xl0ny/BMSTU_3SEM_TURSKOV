import sys
import math


class BiSquareEquation:

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.result = []

    def set_cfs(self):
        try:
            self.a = float(sys.argv[1])
            self.b = float(sys.argv[2])
            self.c = float(sys.argv[3])
        except:
            self.a = float(input("Введите коэффицент A: "))
            self.b = float(input("Введите коэффицент B: "))
            self.c = float(input("Введите коэффицент C: "))

    def get_roots(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D == 0.0:
            root = -self.b / (2.0 * self.a)
            self.result.append(root ** 0.5)
            self.result.append(-root ** 0.5)
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-self.b + sqD) / (2.0 * self.a)
            root2 = (-self.b - sqD) / (2.0 * self.a)
            if root1 > 0:
                self.result.append(root1**0.5)
                self.result.append(-root1 ** 0.5)
            if root2 > 0:
                self.result.append(root2**0.5)
                self.result.append(-root2 ** 0.5)
        return self.result

    def show_roots(self):
        if self.result != []:
            print("\n".join([f"{j + 1}-й корень биквадратного уравнения - {i}" for i, j in zip(self.result, range(len(self.result)))]))
        else:
            print("Нет корней")


def main():
    first = BiSquareEquation()
    first.set_cfs()
    first.get_roots()
    first.show_roots()

if __name__ == "__main__":
    main()