import math

def f(x):
    return (math.cos(x ** 3)) ** 2 - 2.5 * math.log(abs(x))

def rectangle_method(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        x_i = a + i * h
        fx = f(x_i)
        result += fx
        print(f"Прямокутники - крок {i + 1}: x = {x_i}, f(x) = {fx}")
    total = result * h
    print(f"Результат методом прямокутників: {total}")

    return total


def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    print(f"Трапеції - перший доданок: x = {a}, f(x) = {f(a)}")
    print(f"Трапеції - останній доданок: x = {b}, f(x) = {f(b)}")
    for i in range(1, n):
        x_i = a + i * h
        fx = f(x_i)
        result += fx
        print(f"Трапеції - крок {i}: x = {x_i}, f(x) = {fx}")
    total = result * h
    print(f"Результат методом трапецій: {total}")
    return total


def simpson_method(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    print(f"Сімпсон - перший доданок: x = {a}, f(x) = {f(a)}")
    print(f"Сімпсон - останній доданок: x = {b}, f(x) = {f(b)}")
    for i in range(1, n):
        x_i = a + i * h
        coeff = 4 if i % 2 == 1 else 2
        fx = f(x_i)
        result += coeff * fx
        print(f"Сімпсон - крок {i}: x = {x_i}, коефіцієнт = {coeff}, f(x) = {fx}")
    total = result * h / 3
    print(f"Результат методом Сімпсона: {total}")
    return total

e = 3

a = float(input("Введіть нижню межу a: "))
b = float(input("Введіть верхню межу b: "))
n = int(input("Введіть кількість проміжків n: "))

print("\nОбчислення методом прямокутників:")
rectangle_result = rectangle_method(f, a, b, n)

print("\nОбчислення методом трапецій:")
trapezoidal_result = trapezoidal_method(f, a, b, n)

print("\nОбчислення методом Сімпсона:")
simpson_result = simpson_method(f, a, b, n)

# Підсумок
print("\nПідсумкові результати:")
print(f"Метод прямокутників: {round(rectangle_result,e) }")
print(f"Метод трапецій: { round(trapezoidal_result,e) }")
print(f"Метод Сімпсона: {round(simpson_result,e) }")
