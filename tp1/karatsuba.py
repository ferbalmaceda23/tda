s = 0
m = 0
def karatsuba(x, y):
    global m
    global s
    tamanioX = len(str(x))
    tamanioY = len(str(y))

    if (tamanioX == 1) or (tamanioY == 1):
        m+=1
        print(x, " por ", y, "es 1 multiplicacion de un digito")
        return x*y
    else:
        mitad = max(tamanioX, tamanioY)//2

        x1 = x // (10**mitad)
        x0 = x % (10**mitad)
        y1 = y // (10**mitad)
        y0 = y % (10**mitad)

        p = karatsuba(x1+x0, y1+y0)
        s+=2
        x1y1 = karatsuba(x1, y1)
        x0y0 = karatsuba(x0, y0)

        s+=4
        m+=2
        print("(",x1y1,"*(10^",mitad*2,")) + ((",p,"-",x1y1,"-",x0y0,")*(10^",mitad,")) + ",x0y0,"\n")
        return (x1y1*(10**(mitad*2))) + ((p-x1y1-x0y0)*(10**mitad)) + x0y0

print("x*y =", karatsuba(int(input("Ingrese x: ")), int(input("Ingrese y: "))))
print("total sumas: ", s)
print("total multiplicaciones: ", m)