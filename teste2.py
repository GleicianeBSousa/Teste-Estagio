
import math

def is_fibonacci(n):
    a, b = 5*n**2 + 4, 5*n**2 - 4
    return math.sqrt(a).is_integer() or math.sqrt(b).is_integer()

num = int(input("Digite um número: "))

if is_fibonacci(num):
    print(f'O número {num} pertence à sequência de Fibonacci.')

else:
    print(f'O número {num} não pertence à sequência de Fibonacci.')