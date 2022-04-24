import numpy as np

q1, q2, m = input().split(" ")

q1 = float(q1)
q2 = float(q2)
m = float(m)

f = ((9*(10**9)) * q1 * q2) / m ** 2
f = float(f)

print("A força eletrostática é:", end=" ")
print(np.format_float_scientific(f, precision=3, exp_digits=1) + "N")