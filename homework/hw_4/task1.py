# Вычислить число Пи c заданной точностью d
# Пример:
#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤ 10^-10

import math

pi = math.pi
print(pi)
str_pi = str(pi)
d = 0.0001
counter = 2
while d < 1:
     counter += 1
     d = d*10
str_pi_d = str_pi
print(str_pi_d[0:counter])

