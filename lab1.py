import sympy as sp

def getUserInput():
    precision = int(input("Введіть точність обчислень (кількість знаків після коми): "))
    eps = 10 ** (-precision)

    expr_input = input("Введіть вираз для розв'язання (наприклад, 'x**2 - 10 * sin(x)'): ")
    x = sp.Symbol('x')
    expr = sp.sympify(expr_input)

    a = float(input("Введіть початкову точку a: "))
    b = float(input("Введіть початкову точку b: "))

    print()

    return precision, eps, a, b, expr

def checkIfValidRootExists (expr, a, b ):
    return expr.subs(x,a) * expr.subs(x,b) < 0

def findMoveablePoint (expr, a, b):
    deritave2 = sp.diff(expr,x,2)
    if expr.subs(x, a) * deritave2.subs(x,a) < 0:
        return a, b
    else:
        return b, a

def errorRate (expr, newPoint, eps):
    deritave1 = sp.diff(expr,x)
    if abs( expr.subs(x,newPoint) / deritave1.subs(x,newPoint) )  < eps:
        return "Точність відповідає вимогам"
    else:
        return "Знайдений корінь не задовільняє вимоги точності"

def hordaMethod (expr, a, b, eps):
    if not checkIfValidRootExists(expr, a, b):
        return f"Необхідно змінити проміжок \n"

    point, notPoint = findMoveablePoint (expr, a, b)
    previousPoint = None

    while checkIfValidRootExists(expr, point, notPoint):
        newPoint = point - ( ( notPoint - point ) * expr.subs(x,point) ) / ( expr.subs(x,notPoint) - expr.subs(x,point) )
        print(newPoint)

        if previousPoint is not None and abs(newPoint - previousPoint) <= eps:
            break

        previousPoint = point
        point = newPoint

    ans = round(point, precision)
    accuracy = errorRate (expr, point, eps)

    return f"\n{ans}\n{accuracy}\n"


def errorRateNewtonMethod(expr, newPoint, eps):
    deritave1 = sp.diff(expr, x)
    deritave2 = sp.diff(newPoint, x, 2)

    deritave_from_division = deritave1 / (deritave2)

    if abs(expr.subs(x, newPoint) / deritave1.subs(x, newPoint)) < eps:
        return "Точність відповідає вимогам"
    else:
        return "Знайдений корінь не задовільняє вимоги точності"

def findMoveablePoint2 (expr, a, b):
    deritave1 = sp.diff(expr, x)

    if expr.subs(x, a) * deritave1.subs(x, a) < 0 and expr.subs(x, b) * deritave1.subs(x, b) >= 0:
        return b, a
    else:
        return a, b

def newtonMethod(expr, a, b, eps):

    if not checkIfValidRootExists(expr, a, b):
        return f"Необхідно змінити проміжок \n"

    deritave1 = sp.diff(expr, x)

    point, notPoint = findMoveablePoint2 (expr, a, b)
    previousPoint = None

    while  checkIfValidRootExists(expr, point, notPoint):
        newPoint = point - ( expr.subs(x,point) / deritave1.subs(x,point) )
        print(newPoint)

        if previousPoint is not None and abs(newPoint - previousPoint) <= eps:
            break

        previousPoint = point
        point = newPoint

    ans = round(point, precision)
    accuracy = errorRateNewtonMethod (expr, point, eps)
    return f"\n{ans}\n{accuracy}\n"


def combinedMethod (expr, a, b):

    if not checkIfValidRootExists(expr, a, b):
        return f"Необхідно змінити проміжок \n"

    pointHord, pointNewton = findMoveablePoint2 (expr, a, b)

    deritave1 = sp.diff(expr, x)

    while checkIfValidRootExists(expr, pointHord, pointNewton):
        newPointHord = pointHord - ( ( pointNewton - pointHord ) * expr.subs(x,pointHord) ) / ( expr.subs(x,pointNewton) - expr.subs(x,pointHord) )
        print(newPointHord)
        pointHord = newPointHord

        newPointNewton = pointNewton - ( expr.subs(x,pointNewton) / deritave1.subs(x,pointNewton) )
        print(newPointNewton)
        pointNewton = newPointNewton

        print()

        if ( round(newPointHord, precision ) == round( newPointNewton, precision ) ):
            return  f"{round(newPointHord, precision )}\n{"Точність відповідає вимогам"} "

def errorRateIterationMethod(expr, newPoint, eps):
    return 1

def iterationMethod (expr, a, b, eps):

    if expr != x**2 - 10 * sp.sin(x):
        return newtonMethod(expr, a, b, eps)
    else:
        exprNew = x - (expr / sp.diff(expr, x))
        point = a

        exprDer = sp.asin(x ** 2 / 10)
        if abs(exprDer.subs(x, a)) < 1:
            lPoint = a
        elif abs(exprDer.subs(x, b)) < 1:
            lPoint = b

        previousPoint = None

        newPoint = None

        for i in range(100):

            newPoint = exprNew.subs(x, point)
            print(newPoint)
            if previousPoint is not None and abs(newPoint - previousPoint) <= eps:
                break
            else:
                previousPoint = point
                point = newPoint

        ans = round(point, precision)
        accuracy = errorRateNewtonMethod(expr, point, eps)
        return f"\n{ans}\n{accuracy}"


# precision, eps, a, b, expr = getUserInput()

x = sp.Symbol('x')

precision = 4
eps = 10 ** (-precision)
expr = x**2 - 10 * sp.sin(x)
a = float( 2.4 )
b = float( 2.5 )

# expr = x**2 + 4 * sp.sin(x)
# a = float( -2 )
# b = float( -1 )

print ( "Метод хорд:" )
print ( hordaMethod(expr, a, b, eps) )

print ( "Метод дотичних:" )
print ( newtonMethod(expr, a, b, eps) )

print ( "Комбінований метод:" )
print ( combinedMethod(expr, a, b) )
print()

print( "Ітераційний метод:" )
print( iterationMethod(expr, a, b, eps,) )