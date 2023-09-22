x=2
pi=3
while True:
    pi=pi+4/(x*(x+1)*(x+2))-4/((x+2)*(x+3)*(x+4))
    x=x+4
    print(pi)