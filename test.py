from grad_desc_approx import *

x = grad_desc(2, "x^2", step = 0.001, threshold=0.0001)
print(x)