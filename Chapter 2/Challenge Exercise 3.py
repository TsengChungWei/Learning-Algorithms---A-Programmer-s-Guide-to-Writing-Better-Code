# Challenge Exercise 3 (from Listing 2-7)

"""
Generate a table of results for sorting a worst case problem instance (i.e., the val
ues are in descending order) of up to 12 elements using permutation_sort().
Use the factorial_model() to curve fit the preliminary results and see how
accurate the model is in predicting runtime performance. Based on these results,
what is your estimate (in years) for the runtime performance on a worst case
problem instance of size 20?
"""

from itertools import permutations
import time
from matplotlib import pyplot as plt
import numpy as np
from scipy.special import factorial

def factorial_model(n, a):
    return a*factorial(n)

def check_sorted(a):
    for i, val in enumerate(a):
        if i > 0 and val < a[i-1]:
            return False
    return True

def permutation_sorted(A):
    for attempt in permutations(A):
        if check_sorted(attempt):
            A[:] = attempt[:]       # copy back into A
            return

Eles = 12
A_sample = [[j+1 for j in range(Eles-i)]+[Eles-j for j in range(i)] for i in range(1, Eles+1)]

T_ms = []
s = ["idx", "|", "year", "day", "hour", "min", "sec", "ms"]
print(f"\n{s[0]:<3} {s[1]:<3} {s[2]:<4} {s[3]:<4} {s[4]:<4} {s[5]:<4} {s[6]:<4} {s[7]:<4}")
print("-"*43)

times = 10
for idx, A in enumerate(A_sample): 
    if idx == 11:
        times = 1
    temp = time.time()
    for _ in range(times):
        B = A.copy()
        permutation_sorted(B)
    t = 1000*(time.time()-temp)
    t = round(t/times)
    sec, ms = divmod(t, 1000)
    min, sec = divmod(sec, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    print(f"{Eles-idx:<3} {s[1]:<3} {year:<4} {day:<4} {hour:<4} {min:<4} {sec:<4} {ms:<4}")
    T_ms.append(t)

A_size = [i+1 for i in range(Eles)]
plt.plot(A_size, T_ms, marker='o', linestyle='-', label='')

plt.title('')
plt.xlabel('reverse index')
plt.xticks(A_size)
plt.ylabel('Time')
plt.yticks([0, 10**(Eles-8), 2*10**(Eles-8), 15*10**(Eles-8), 2*10**(Eles-7)])
plt.grid(True)

plt.show()

"""
Answer:
Through pyplot, we can observe from the line chart that, for different numbers 
of elements (Eles), the computation time of taking the ith element from the 
front in ascending order and the ith element from the back in descending 
order (i.e. A(Eles-i+1) = [1, 2, ..., i-1, Eles, Eles-1, ..., i+1, i] or 
Ai = [1, 2, ..., Eles-i, Eles, Eles-1, ..., Eles-i+2, Eles-i+1]), 
for i = 1, 2, ..., Eles, shows the same growth trend.

For example, we complement the algorithm with 10 times and take the
average to obtain the computing time. However, it takes too much time 
when we sort. Therefore, we only perform the sorting once for A12. 

Eles    |   A6    A7    A8    A9    A10   A11    A12
----------------------------------------------------------------
9       |   0     3     19    129                           (ms)
10      |   1     3     21    151   1256                    (ms)
11      |   1     4     23    174   1486  13858             (ms)
12      |   0     4     25    200   1734  16397  163582     (ms)


But if we take the approximation, the table become

Eles    |   A6    A7    A8    A9    A10   A11    A12
----------------------------------------------------------------
9       |   0     2     20    130                           (ms)
10      |   null  0     20    150   1250                    (ms)
11      |   null  null  0     200   1500  14000             (ms)
12      |   null  null  null  0     1700  16000  160000     (ms)


If we observe the result and calculate the growth ratios 
(last three)/(last second) and (last second)/(last one) approximately, 
then

Eles    |   (-3)/(-2)   (-2)/(-1)
----------------------------
9       |   10          6.5
10      |   7.5         8.333
11      |   7.5         9.333
12      |   9.412       10

We calculate the geometric means of the four ratios in 
(last three)/(last second) and (last second)/(last one), so we gat 
8.53 and 8.432 two ratios. Therefore, we can choose the ratio 8.5 to 
estimate the computing time for the algorithm when Eles = 20.

Suppese that Ai = [1, 2, ..., 20-i, 20, 20-1, ..., 20-(i-2), 20-(i-1)] 
for i = 1, 2, ..., 20, and the algorithm spends 2*10**11 ms approximatly 
when the input is A18. Since we have the growth ratio 8.5, the algorithm 
will spend (8.5**2)*(2*10**11) ms if we want to sort A20.

Thus, we estimate that the algorithm spends at least 458 years 
(1.445*10**13 ms) for the runtime performance on a worst case problem 
instance of size 20.
"""

