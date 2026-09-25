import math
def n(x):
    return 1 -(math.ceil(x)-math.floor(x))
def v(x):
    return (x-1)/4
def c(x):
    return n((x-1)/4) - n((x-1)/8)
def m(x):
    sum = 0
    for  i in range(x+1): 
        rx =x
        for t in range(i):
            rx = v(rx)
        sum += n(rx)*c(rx)
    return sum
def g(x):
    rx = x
    for i in range(m(x)):
        rx = v(x)
    return rx
def j(x):
    return (1-math.ceil(abs(x)/abs(x)+1))+x

def b(x):
    return (2*m(x)+1+n((g(x)-1)/8))

while True:
    x = int(input(": "))
    print(b(x))