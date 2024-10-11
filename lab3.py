
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x, y):
    return x * y + x ** 2 + np.cos(y)
    # return 1 / (np.cos(x) - y)

def euler_method(a, b, h, y0):
    n = int((b - a) / h)
    x_values = []
    y_values = []
    x = a
    y = y0
    x_values.append(x)
    y_values.append(y)

    for i in range(n):
        y += h * f(x, y)
        x += h
        x_values.append(x)
        y_values.append(y)

    return np.array(x_values), np.array(y_values)

def runge_kutta_method(a, b, h, y0):
    n = int((b - a) / h)
    x_values = []
    y_values = []
    x = a
    y = y0
    x_values.append(x)
    y_values.append(y)

    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        x_values.append(x)
        y_values.append(y)

    return np.array(x_values), np.array(y_values)

def adams_method(a, b, h, y0, x_rk, y_rk):
    n = int((b - a) / h)
    x_values = list(x_rk)
    y_values = list(y_rk)

    for i in range(4, n+1):
        q3 =  h * f(x_rk[i-1], y_rk[i-1])
        q2 =  h * f(x_values[i-2], y_values[i-2])
        q1 =  h * f(x_values[i-3], y_values[i-3])
        q0 = h * f(x_values[i-4], y_values[i-4])

        delta_q0 = q1-q0
        delta_q1 = q2-q1
        delta_q2 = q3-q2

        y_values[i] = y_values[i-1] + q3+ delta_q2 * 0.5 + delta_q1**2 * 5 / 12 + delta_q0**3 * 3 / 8
        # print(f"iteration{i}")
        # print(f"\nq0= {q0} {h,x_values[i-4], round( y_values[i-4],5) } \nq1= {q1} { h,x_values[i-3], round( y_values[i-3],5)}"
        #       f"\nq2= {q2} { h,x_values[i-2], round( y_values[i-2],5)} \nq3= {q3} { h,x_values[i-1],round( y_values[i-1],5)}\ndelta_q0= {delta_q0}"
        #       f"\ndelta_q1= {delta_q1}\ndelta_q2= {delta_q2} \n {round(q3+ delta_q2 * 0.5 + delta_q1**2 * 5 / 12 + delta_q0**3 * 3 / 8, 5)}\ny= {y_values[i]}\n")
        # y_values [i] = y_values[i-1] +  ( y_values[i-1]*h - y_values[i-2]/2*h**2  + y_values[i-3]*5/12*h**3 - y_values[i-4]*3/8*h**3 )

        # y_values [i] = y_values[i-1] + (h * ( ( y_values[i-1]*55 + y_values[i-2]*59  + y_values[i-3]*37 - y_values[i-4]*9) /24 ))

    return np.array(x_values), np.array(y_values)

def picard_method(a, b, h, y0, f):
    n = int((b - a) / h)
    x_values = np.arange(a, b + h, h)

    y_values = np.zeros(len(x_values))
    y_values[0] = y0

    for i in range(1, n + 1):
        integrand = lambda t: f(t, y_values[i - 1])
        integral, _ = quad(integrand, x_values[0], x_values[i])
        y_values[i] = y_values[0] + integral

    return x_values, y_values

def print_points(x, y, method_name):
    print(f"{method_name}:")
    for xi, yi in zip(x, y):
        print(f"{xi:.3f}, {yi:}")
    print()


a = float(input("Введіть початок інтервалу (a): "))
b = float(input("Введіть кінець інтервалу (b): "))
y0 = float(input("Введіть початкове значення y0: "))
h = float(input("Введіть крок (h): "))
# a, b, y0, h = 1, 2, 0, 0.1

# a, b, y0, h = -4, 1, 0, 0.25

x_euler, y_euler = euler_method(a, b, h, y0)
print_points(x_euler, y_euler, "\nМетод Ейлера")

x_rk, y_rk = runge_kutta_method(a, b, h, y0)
print_points(x_rk, y_rk, "Метод Рунге-Кутти")

x_adams, y_adams = adams_method(a, b, h, y0, x_rk, y_rk)
print_points(x_adams, y_adams, "Метод_Адамса")

x_picard, y_picard = picard_method( a, b, h, y0, f )
print_points(x_picard, y_picard, "Метод Пікара")


plt.figure(figsize=(10, 6))
plt.plot(x_euler, y_euler, 'o-', label="Метод Ейлера", markersize=5)
plt.plot(x_rk, y_rk, 's-' , label="Метод Рунге-Кутти", markersize=5)
plt.plot(x_adams, y_adams,  's-', label="Метод Адамса", markersize=5)
plt.plot(x_picard, y_picard, 'd-', label="Метод Пікара", markersize=5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()