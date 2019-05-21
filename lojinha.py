nv = int(input())

valor = 0

for i in range(0,nv):
    qtde,uni = input().split()
    valor += int(qtde)*float(uni)

print('%.2f' % valor)