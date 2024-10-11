import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify

def lagrange_polynomial(xi, yi):
    x = symbols('x')
    n = len(xi)
    poly = 0

    for i in range(n):
        basis = 1
        for j in range(n):
            if j != i:
                basis *= (x - xi[j]) / (xi[i] - xi[j])
        poly += yi[i] * basis

    simplified_poly = simplify(poly)
    print(f"інтерполяційний многочлен Лагранжа: P(x) = {simplified_poly}")

    return simplified_poly


n = int(input("Введіть кількість точок n: "))
xi = []
yi = []

for i in range(n):
    x_val, y_val = map(float, input(f"Введіть x{i}, y{i}: ").split())
    xi.append(x_val)
    yi.append(y_val)

poly = lagrange_polynomial(xi, yi)

x_values = np.linspace(min(xi) - 1, max(xi) + 1, 500)
y_values = np.array([poly.evalf(subs={'x': x}) for x in x_values], dtype=float)

plt.plot(x_values, y_values, label="Поліном Лагранжа", color="blue")
plt.scatter(xi, yi, color="red", label="Точки")
plt.title("Інтерполяційний поліном Лагранжа")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
