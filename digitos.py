import math

def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1))

n = int(input())

lista= []
for i in range(0,n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    lista.append([a,b])

intervalo = 1
res = ''
for i in range(0, n):
    a = lista[i][0]
    b = lista[i][1]
    contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numeros_primos = (n for n in range(a, b+1) if is_prime(n))
    for num in numeros_primos:
        for x in str(num):
            contador[int(x)] += 1

    res += f'INTERVALO {intervalo}\n'

    for i, v in enumerate(contador):
        res += f'{i}: {v}\n'
    intervalo += 1

print(res[0:len(res)-1])