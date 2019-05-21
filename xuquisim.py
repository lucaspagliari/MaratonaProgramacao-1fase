A,L = input().split()
A = int(A)
L = int(L)

lista= []
for i in range(0,(2**(A+1))-1):
    lista.append('0')

for j in range(0,L):
    j,frase = input().split()
    lista[int(j)-1] = frase

num = int(input())
pont = 0

for i in range(0,num):
    escolha = input()
    if escolha == 'true':
        pont =  2*pont + 2
    else:
        pont = 2*pont +1

print(lista[pont])