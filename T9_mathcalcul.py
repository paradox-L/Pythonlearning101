#solve quadratic equation with one unknown
import math

def solve(a,b,c):
    delta = math.pow(b,2) - 4*a*c
    if delta > 0:
        print"The unknown has 2 values"
    elif delta == 0:
        print"The unknown has 1 value"
    else:
        print"The unknown has no solution in real"
        raise SystemExit

    X1=float((-b + math.sqrt(delta))/(2*a))
    X2=float((-b - math.sqrt(delta))/(2*a))
    print "solution:\nX1=%f\nX2=%f"%(X1,X2)

print"Please enter the 3 coefficient in descending order:\n"
A=input()
if A == 0:
    print"Are you sure it's a quadratic equation?"
    A=input("Please re-enter the number or use ctr+c to quit\n")
B=input()
C=input()
solve(A,B,C)