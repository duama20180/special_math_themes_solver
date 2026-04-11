import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

i = 47
c = [-i, -(i + 2)]

A = [
    [i, 3 * i],
    [i + 4, i]
]

b = [5 * i + 1, 5 * i + 2]

x1_bounds = (0, None)
x2_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='highs')

if res.success:
    print(f'Оптимальні значення x1 = {res.x[0]:.2f}, x2 = {res.x[1]:.2f}')
    print(f'Максимальне значення цільової функції: {-res.fun:.2f}')
else:
    print("Рішення не знайдено")

x1 = np.linspace(0, 10, 400)

x2_1 = ((5 * i + 1) - i * x1) / (3 * i)
x2_2 = ((5 * i + 2) - (i + 4) * x1) / i

plt.plot(x1, x2_1, label=r'$47x_1 + 141x_2 \leq 236$')
plt.plot(x1, x2_2, label=r'$51x_1 + 47x_2 \leq 237$')

plt.fill_between(x1, 0, np.minimum(x2_1, x2_2), where=(x2_1 >= 0) & (x2_2 >= 0), color='gray', alpha=0.3)

if res.success:
    plt.plot(res.x[0], res.x[1], 'ro', label='Оптимальне рішення')

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()
plt.grid(True)
plt.title('Графічне рішення задачі лінійного програмування')
plt.show()

