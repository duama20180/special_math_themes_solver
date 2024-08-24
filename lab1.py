import sympy as sp

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
        return "Необхідно змінити проміжок"

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

    return f"{ans}\n{accuracy}"


def errorRateNewtonMethod(expr, newPoint, eps):
    deritave1 = sp.diff(expr, x)
    deritave2 = sp.diff(newPoint, x, 2)

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
        return "Необхідно змінити проміжок"

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
    return f"{ans}\n{accuracy}"


def combinedMethod (expr, a, b):

    if not checkIfValidRootExists(expr, a, b):
        return "Необхідно змінити проміжок"

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
            return ( round(newPointHord, precision ) )


def iterationMethod (expr, a, b, eps):
    return 1

precision = 4
eps = 10 ** (-precision)
x = sp.Symbol('x')

expr = x**2 - 10 * sp.sin(x)
a = float( 2.4 )
b = float( 2.5 )

# expr = x**2 + 4 * sp.sin(x)
# a = float( -2 )
# b = float( -1 )

#print ( "Метод хорд:" )
#print ( hordaMethod(expr, a, b, eps) )
print()

# print ( "Метод дотичних:" )
# print ( newtonMethod(expr, a, b, eps) )
print()

print ( "Комбінований метод:" )
print ( combinedMethod(expr, a, b) )