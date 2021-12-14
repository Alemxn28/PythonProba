def factorial(x):
    f = 1
    for i in range(1, x+1):
        print(i)
        f = f * i
    return f

def permutacion_sin_repeticion(n, r):
    return int(factorial(n)/factorial(n-r))

def permutacion_con_repeticion(elementos):
    n = 0
    total = 1
    factorial_array = list()
    for i in elementos:
        n = n + i

    for i in elementos:
        factorial_array.append(factorial(i))

    for i in factorial_array:
        total = total * i

    return int(factorial(n)/total)

def combinacion(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))