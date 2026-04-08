import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.351, 0.664, 0.978, 1.291, 1.605, 1.918, 2.232, 2.546, 2.859])
y = np.array([0.605, 0.265, 0.064, 0.116, 0.415, 0.728, 1.673, 3.138, 5.092])

def linear_regression(x, y):
    n = len(x)

    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_xy = np.sum(x * y)

    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a0 = (sum_y - a1 * sum_x) / n

    return a0, a1

def quadratic_regression(x, y):
    n = len(x)

    A = np.array([
        [n, np.sum(x), np.sum(x ** 2)],
        [np.sum(x), np.sum(x ** 2), np.sum(x ** 3)],
        [np.sum(x ** 2), np.sum(x ** 3), np.sum(x ** 4)]
    ])

    B = np.array([
        np.sum(y),
        np.sum(x * y),
        np.sum(x ** 2 * y)
    ])

    a0, a1, a2 = np.linalg.solve(A, B)

    return a0, a1, a2

a0_lin, a1_lin = linear_regression(x, y)
a0_quad, a1_quad, a2_quad = quadratic_regression(x, y)

y_pred_lin = a0_lin + a1_lin * x
y_pred_quad = a0_quad + a1_quad * x + a2_quad * x ** 2

def r_squared(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_pred) ** 2)
    return 1 - (ss_residual / ss_total)

r2_lin = r_squared(y, y_pred_lin)
r2_quad = r_squared(y, y_pred_quad)

plt.scatter(x, y, color='blue', label='Дані (xi, yi)')

x_line = np.linspace(min(x), max(x), 100)
y_line_lin = a0_lin + a1_lin * x_line
plt.plot(x_line, y_line_lin, color='red', label=f'Лінійна регресія: y = {a0_lin:.2f} + {a1_lin:.2f}x (R² = {r2_lin:.3f})')

y_line_quad = a0_quad + a1_quad * x_line + a2_quad * x_line ** 2
plt.plot(x_line, y_line_quad, color='green', label=f'Параболічна регресія: y = {a0_quad:.2f} + {a1_quad:.2f}x + {a2_quad:.2f}x² (R² = {r2_quad:.3f})')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Лінійна та параболічна регресії методом найменших квадратів')
plt.legend()
plt.grid(True)
plt.show()

print(f"Лінійне рівняння: y = {a0_lin:.4f} + {a1_lin:.4f} * x (R² = {r2_lin:.3f})")
print(f"Параболічне рівняння: y = {a0_quad:.4f} + {a1_quad:.4f} * x + {a2_quad:.4f} * x² (R² = {r2_quad:.3f})")
