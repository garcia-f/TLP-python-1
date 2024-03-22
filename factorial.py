# Calcular el factorial de n sin *

# def suma(a, b):
#     return a +b

def multi(a, b):
    resultado = 0
    for _ in range(b):
        # resultado = suma(resultado, a)
        resultado = resultado + a
    return resultado

def factorial(num):
    if num == 0:
        return 1
    resultado = 1
    for i in range(1, num + 1):
        resultado = multi(resultado, i)
    return resultado


print('Ingrese un numero para realizar su factorial')
num = int(input())
resultado = factorial(num)
print(f'El factorial es {num} es: {resultado}')





