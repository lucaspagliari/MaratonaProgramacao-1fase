from math import sqrt

N,T = input().split()
N = int(N)
T = int(T)

def calc_pontos(dbb,dbv):
    pontos=0
    bfora = 0
    i,j = 0,0
    entrou = False
    while dbb[i]==dbv[j] and i < len(dbb):
        i += 1
        j += 1
    while dbb[i]<dbv[j] and i < len(dbb):
        pontos += 1
        i += 1
        entrou = True
    while dbb[i]>dbv[j] and j < len(dbb) and not entrou:
        pontos -= 1
        j += 1
    return pontos

pbranco=0
pvermelho=0

bb =[]
bv = []

for t in range(0,T):
    xbolim,ybolim = input().split()
    xbolim = int(xbolim)
    ybolim = int(ybolim)
    for i in range(0,N):
        x,y = input().split()
        bb.append([int(x),int(y)])
    for i in range(0,N):
        x,y = input().split()
        bv.append([int(x),int(y)])

    dbb = []
    dbv = []

    for i in bb:
        dbb.append(sqrt((i[0]-xbolim)**2+(i[1]-ybolim)**2))
    for i in bv:
        dbv.append(sqrt((i[0]-xbolim)**2+(i[1]-ybolim)**2))

    dbb.sort()
    dbv.sort()
    ponto = calc_pontos(dbb,dbv)
    if ponto > 0:
        pbranco += ponto
    elif ponto < 0:
        pvermelho -= ponto

if pvermelho > pbranco:
    venc = 'VENCEDOR: BOCHAS VERMELHAS'
elif pvermelho < pbranco:
    venc = 'VENCEDOR: BOCHAS BRANCAS'
else:
    venc = 'EMPATE'

print(f'PONTOS DAS BOCHAS BRANCAS = {pbranco}\nPONTOS DAS BOCHAS VERMELHAS = {pvermelho}\n{venc}')