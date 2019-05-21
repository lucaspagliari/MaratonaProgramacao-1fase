numcartas = int(input())

p1 = []
p2 = []

for i in range(0,numcartas):
    f,a,d,s = input().split()
    p1.append([int(f),int(a),int(d),int(s)])

for i in range(0,numcartas):
    f,a,d,s = input().split()
    p2.append([int(f),int(a),int(d),int(s)])

danete = 0
silvio = 0
empata = 0

for i in range(0,numcartas):
    for j in range(0,4):
        if p1[i][j] > p2[i][j]:
            danete += 1
            break
        elif p1[i][j] < p2[i][j]:
            silvio += 1
            break
        else:
            if j==3:
                empata += 1

print(f'danette venceu: {danete}\nsilvio venceu: {silvio}\nempates: {empata}')