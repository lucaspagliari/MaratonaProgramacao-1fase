from math import sqrt, asin, hypot

def area_intersec(x1,y1,r1, x2, y2, r2):
    global pi
    d = hypot(x2 - x1, y2 - y1)

    if d < (r1 + r2):

        a = r1 * r1
        b = r2 * r2

        x = (a - b + d * d) / (2 * d)
        z = x * x
        y = sqrt(a - z)

        if d < abs(r2 - r1):
            return pi * min(a, b)
    
        return a * asin(y / r1) + b * asin(y / r2) - y * (x + sqrt(z + b - a))
    return 0

n = int(input())

entradas = []
area_total = 0
pi = 3.1415

for qnt in range(0, n):
    entradas.append(input().split()) 

for v in entradas:
    area_total += pi * int(v[2]) ** 2

for i in range(0, len(entradas)):
    x1, y1, r1= int(entradas[i][0]), int(entradas[i][1]), int(entradas[i][2])
    
    for j in range(i+1, len(entradas)):
        area_total -= area_intersec(x1,y1,r1,int(entradas[j][0]), int(entradas[j][1]), int(entradas[j][2]))

print(int(area_total))