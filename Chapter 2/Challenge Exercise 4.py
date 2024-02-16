# Challenge Exercise 4

"""
Generate empirical evidence on 50,000 random trials of Binary Array Search for
N in the range of 25 through 221. Each trial should use random.sample() to ran
domly select N values from the range 0 .. 4N and place these values in sorted
order. Then each trial should search for a random target value in the same range.
Using the results I have outlined in this chapter, use curve_fit() to develop a
log N model that models the results of runtime performance for N in the range
25 through 212. Determine the threshold problem instance size above which the
behavior stabilizes. Create a visual plot of the data to see whether the computed
model accurately models the empirical data.
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    return -1

'''
for _ in range(1):
    # N = random.randint(2**5, 2**21)
    # target_range = ((8*N)//11, (9*N)//11)

    N = 1250000
    target_idx_range = [900000, 920000]


    Trial = random.sample(list(range(0, 4*N)), N)
    Trial.sort()

    target_idx = random.randint(target_idx_range[0], target_idx_range[1])
    target = Trial[target_idx]


    print(binary_search(Trial, target) == target_idx)

    
def logarithm_model(n, a, b):
    return a*np.log2(n) + b

xs = [0.87, 2.1506, 3.89]
ys = [0.012, 0.95985, 2.3432]

[(a,b), _]   = curve_fit(logarithm_model, np.array(xs), np.array(ys))
S = 'Logarithm = {:.10f}*log2(N) + {:.10f}'.format(a, b)
print(S)

x = np.linspace(0.5, 6, 100)
y1 = logarithm_model(x, a, b)
plt.plot(x, y1, label='', color='b')
plt.plot(xs, ys, marker='o', linestyle='', color='r')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(S)
 
# Displaying the legend and the plot
plt.legend()
plt.show()
'''

