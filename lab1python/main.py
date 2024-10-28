import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]

    except:
        print(prompt)
        coef_str = input()

    try:
        coef = float(coef_str)
    except:
        return get_coef(index, prompt)

    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.append(root1**0.5)
        if root2 > 0:
            result.append(root2**0.5)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print("Нет корней")
    elif len_roots == 1:
        print(f"Два корня: ±{roots[0]}")
    elif len_roots == 2:
        print(f"Четыре корня: ±{roots[0]} и ±{roots[1]}")

if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4