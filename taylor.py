from math import factorial

r = float(input())

if r == 90:
    print('0.000')
else:
    r = r*3.1415/180

    taylor = 1

    for i in range(1,6):
        taylor += ((-1)**i)*(r**(2*i))/factorial(2*i)

    taylor = str(taylor)
    if len(taylor) > 5:
        casa=taylor[5]
    else:
        casa = '0'
    saida = float(taylor[0:5])

    if int(casa) > 6:
        saida += 0.001

    print('%.3f' % saida)