num = int(input ("Digite o número a verificar: "))

# Encontrar a quantidade de dígitos em n
q = 0
while(10 ** q < num):
    q = q + 1

i = q
f = 0
ni = nf = num
pi = pf = 0

while(i > f):
    pi = int(ni / (10 ** (i-1)))
    pf = nf % 10
    if pi != pf:
        break
    f = f + 1
    i = i - 1
    ni = ni - (pi * (10 ** i))
    nf = int(nf / 10)

if(pi == pf):
    print("%d é palíndromo." % num)
else:
    print("%d não é palíndromo." % num)

