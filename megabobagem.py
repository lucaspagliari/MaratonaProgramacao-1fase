from string import ascii_uppercase

palavra = input()

contador_letra = 0
impares = 0
flag = True

for letra in ascii_uppercase:
    for le in palavra:
        if letra is le:
            contador_letra += 1
    if contador_letra % 2 == 1:
        impares += 1
        if impares > 1:
            flag = False
            break
    contador_letra = 0

if flag:
    print('VERDADEIRO')
else:
    print('FALSO')
