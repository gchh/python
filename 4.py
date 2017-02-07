import math
def quadratic(a,b,c):
    i=b*b-4*a*c
    if i>=0:
        x=(math.sqrt(i)-b)/2a
        y=(-b-(math.sqrt(i)-b))/2a
        return x,y
    else:
        return

