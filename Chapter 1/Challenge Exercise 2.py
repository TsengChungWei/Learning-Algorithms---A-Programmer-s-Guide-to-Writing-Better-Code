# Challenge Exercise 2 (from Listing 1-9)

"""
Linear time median: A wonderful algorithm exists that efficiently locates the
median value in an arbitrary list (for simplicity, assume size of list is odd). Review
the code in Listing 1-9 and count the number of times less-than is invoked, using
RecordedItem values as shown in the chapter. This implementation rearranges
the arbitrary list as it processes.

Implement a different approach (which requires extra storage) that creates a sorted 
list from the input and selects the middle value. Compare its runtime performance 
with linear_median() by generating a table of runtime performance.
"""

import random
import time
from matplotlib import pyplot as plt


def partition(A, lo, hi, idx):
    if lo == hi: return lo
    A[idx], A[lo] = A[lo], A[idx]
    i = lo
    j = hi + 1
    while True:
        while True:
            i += 1
            if i == hi: break
            if A[lo] < A[i]: break
        while True:
            j -= 1
            if j == lo: break
            if A[j] < A[lo]: break
        if i >= j: break
        A[i], A[j] = A[j], A[i]
    A[lo], A[j] = A[j], A[lo]
    return j

def linear_median(A):
    lo = 0
    hi = len(A) - 1
    mid = hi//2
    while lo < hi:
        idx = random.randint(lo, hi)
        j = partition(A, lo, hi, idx)
        if j == mid: return A[j]
        if j < mid: lo = j + 1
        else: hi = j - 1
    return A[lo]

def find_median(A):
    return sorted(A)[(len(A)-1)//2]


N_sample = [2**(10+i) for i in range(12)]
T_ms = [[], [], [], []]
# print(N)

for i, N in enumerate(N_sample):
    A = [random.randint(0, 10*N) for _ in range(N)]
    temp = time.time()
    result = linear_median(A)
    t = time.time()-temp
    t *= 1000
    T_ms[0].append(t)
    # print(f"The median: {result}\ntime: {round(t*1000, 3)} ms\n")
    
    temp = time.time()
    result = find_median(A)
    t = time.time()-temp
    t *= 1000
    T_ms[1].append(t)
    # print(f"The median(other way): {result}\ntime: {round(t*1000, 3)} ms\n")

plt.plot(N_sample, T_ms[0], marker='o', linestyle='-', label='linear_median()')
plt.plot(N_sample, T_ms[1], marker='^', linestyle='-', label='find_median()')

plt.title('Algorithm Performance Comparison')
plt.xlabel('Size (N)')
plt.xticks([500000*i for i in range(6)])
plt.ylabel('Elapsed Time (ms)')
plt.grid(True)
plt.ticklabel_format(style='plain')
plt.legend()

plt.show()
