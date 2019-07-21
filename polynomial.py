from sympy import sympify, diff, Symbol, Pow, factorial, lambdify
import math
import numpy as np
from matplotlib import pyplot as plt
var = Symbol("x")

class Approximator:
    def __init__(self):
        self.input_f = sympify("sin(x)")
        self.degree = 2
        self.center = 0
        self.approx_f = sympify("x")

    def update_fields(self, input_f, degree, center):
        self.input_f = sympify(input_f)
        self.degree = degree
        self.center = center
        self.approx_f = self.approximate(self.input_f, self.degree, self.center)

    def approximate(self, f, d, c):
        if d == 0:
            return f.evalf(subs={var:c})
        else:
            return self.approximate(f, d-1, c) + diff(f, var, d).evalf(subs={var:c}) * Pow((var - c), d) / factorial(d)
            #pt_1 = diff(f, var, d).evalf(subs={var:c})
            #print(pt_1, type(pt_1))
            #pt_2 = Pow((var - c), d)
            #print(pt_2, type(pt_2))
            #pt_3 = factorial(d)
            #print(pt_3, type(pt_3))
    def convert(self, f):
        return lambdify(var, f)

ap = Approximator()
ap.update_fields("sin(x)", 10, 0)
func = ap.convert(ap.input_f)
func_approx = ap.convert(ap.approx_f)
xpts = np.linspace(-10, 10, 100)
plt.plot(xpts, [func_approx(x) for x in xpts], 'r')
plt.plot(xpts, [func(x) for x in xpts], 'b')
axes = plt.gca()
axes.set_ylim([-20, 20])
plt.show()
#Structure:

##input fields: function, degree of approximation, point to approximate around, [update button?]
##display fields: live graph, approximated function
