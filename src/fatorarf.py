def fatorar (a:int, b:int):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, b + 1):
            resultado *= a
        return resultado