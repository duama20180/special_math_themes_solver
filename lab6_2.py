from scipy.optimize import linprog

c = [-9, -7]

A = [
    [2, 1],   # Обмеження на ресурс A1
    [2, 5],   # Обмеження на ресурс A2
    [3, 4]    # Обмеження на ресурс A3
]

b = [34, 105, 91]

x_bounds = (0, None)
x2_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x2_bounds], method='highs')

if res.success:
    print(f'Оптимальні значення x1 = {res.x[0]}, x2 = {res.x[1]}')
    print(f'Максимальний прибуток: {-res.fun}')
else:
    print("Рішення не знайдено")
