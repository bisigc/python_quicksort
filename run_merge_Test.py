import random
from merge import merge

A = list(range(1,100,2))
B = list(range(2,101,2))

print(A)
print(B)

D = merge(A,B)

print(D)
