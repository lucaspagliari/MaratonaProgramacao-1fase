from copy import deepcopy

def muda_estado(atual,past,i,j):
    global L
    global C
    cont=0
    for k in [-1,0,1]:
        for l in [-1,0,1]:
            if i+k>=0 and i+k<L and j+l>=0 and j+l<C:
                    cont += past[i+k][j+l]
    cont -= past[i][j]
    if cont<2 and past[i][j]==1:
        atual[i][j] = 0
    elif cont>3 and past[i][j]==1:
        atual[i][j] = 0
    elif cont == 3 and past[i][j]==0:
        atual[i][j] = 1
    elif (cont == 2 or cont == 3) and past[i][j]==1:
        atual[i][j] = 1


L,C = input().split()
L = int(L)
C = int(C)
atual = []
past = []

for i in range(0,L):
    entrada = input().split()
    past=[]
    for j in range(0,C):
        past.append(int(entrada[j]))
    atual.append(past)

past = deepcopy(atual)

tempo = int(input())

for t in range(0,tempo):
    for i in range(0,L):
        for j in range(0,C):
            muda_estado(atual,past,i,j)
    past = deepcopy(atual)

res = ''
for i in range(0,L):
    for j in range(0,C):
        res += f'{past[i][j]}'
    res+='\n'
print(res[0:len(res)-1])