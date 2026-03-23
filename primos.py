"""
Nombre: ORIOL PERARNAU

>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
"""

import doctest


def esPrimo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2

    return True


def primos(numero):
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    factores = []
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero = numero // divisor
        divisor += 1

    return tuple(factores)


# FUNCIONES AUXILIARES

def contar(lista, valor):
    return lista.count(valor)


def unicos(lista):
    return list(set(lista))


def mcm(a, b):
    f1 = list(descompon(a))
    f2 = list(descompon(b))

    primos = set(f1 + f2)

    resultado = 1
    for p in primos:
        e1 = contar(f1, p)
        e2 = contar(f2, p)
        resultado *= p ** max(e1, e2)

    return resultado


def mcd(a, b):
    f1 = list(descompon(a))
    f2 = list(descompon(b))

    primos = set(f1) & set(f2)

    resultado = 1
    for p in primos:
        e1 = contar(f1, p)
        e2 = contar(f2, p)
        resultado *= p ** min(e1, e2)

    return resultado


def mcmN(*numeros):
    factores = []

    for n in numeros:
        factores.append(list(descompon(n)))

    todos = set()
    for f in factores:
        todos.update(f)

    resultado = 1

    for p in todos:
        max_exp = 0
        for f in factores:
            exp = f.count(p)
            if exp > max_exp:
                max_exp = exp

        resultado *= p ** max_exp

    return resultado


def mcdN(*numeros):
    factores = [list(descompon(n)) for n in numeros]

    comunes = set(factores[0])
    for f in factores[1:]:
        comunes = comunes & set(f)

    resultado = 1

    for p in comunes:
        min_exp = float('inf')
        for f in factores:
            exp = f.count(p)
            if exp < min_exp:
                min_exp = exp

        resultado *= p ** min_exp

    return resultado


if __name__ == "__main__":
    doctest.testmod(verbose=True)