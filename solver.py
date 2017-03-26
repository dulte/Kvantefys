from sympy.solvers import solve
from sympy import *

A = Symbol('A')
B = Symbol('B')
C = Symbol('C')
D = Symbol('D')
F = Symbol('F')

omega = Symbol('omega')
alpha = Symbol('alpha')

solution = solve([Eq(A*alpha + B,C*alpha + D),Eq(C+D*alpha,F),Eq(C*alpha - D - A*alpha + B, omega*(A*alpha + B)),Eq(F-C + D*alpha,omega*F)],[B,C,D,F   ])


for i in solution:
    print str(i) + " = " + str(solution[i])
    print "______________________________"
