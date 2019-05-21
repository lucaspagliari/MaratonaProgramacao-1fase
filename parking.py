carros = int(input())
hmin = 24
mmin = 60
hmax = 0
mmax = 0

for i in range(0,carros):
    he,me,hs,ms = input().split()
    he = int(he)
    me = int(me)
    hs = int(hs)
    ms = int(ms)
    if he < hmin:
        hmin,mmin = he,me
    elif he == hmin:
        if me < mmin:
            mmin = me
    if hs > hmax:
        hmax,mmax = hs,ms
    elif hs == hmax:
        if ms > mmax:
            mmax = ms

h = hmax - hmin
m = mmax - mmin
print(60*h+m)