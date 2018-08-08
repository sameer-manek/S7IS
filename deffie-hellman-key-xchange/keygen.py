import os

# deffie hellman key xchange

def cR(G,i,P):
    return (G**i)%P

def cK(Rx, Ry, x, y, G, P):
    ix = (Ry**x)%P
    iy = (Rx**y)%P
    if ix == iy:
        return ix

if __name__ == "__main__":

    P = int(input("give a large prime number"))
    x = int(input("secret key of x: "))
    y = int(input("secret key of y: "))
    G = int(input("value of Generator: "))

    Rx = cR(G,x,P)
    Ry = cR(G,y,P)
    
    print(Rx, Ry)
    print("shared key: {}".format(cK(Rx, Ry, x, y, G, P)))
    
