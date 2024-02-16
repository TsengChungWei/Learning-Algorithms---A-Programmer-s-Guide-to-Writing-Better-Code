# Challenge Exercise 3 (from Listing 1-10)

"""
Counting Sort: If you know that an arbitrary list, A, only contains nonnegative
integers from 0 to M, then the following algorithm will properly sort A using just
an extra storage of size M.

Listing 1-10 has nested loops—a for loop within a while loop. However, you can
demonstrate that A[pos+idx] = v only executes N times.

Conduct a performance analysis to demonstrate that the time to sort N integers
in the range from 0 to M doubles as the size of N doubles.
You can eliminate the inner for loop, and improve the performance of this operation, 
using the ability in Python to replace a sublist using sublist[left:right] = [2,3,4].
Make the change and empirically validate that it, too, doubles as N
doubles, while yielding a 30% improvement in speed.
"""

import random
import time
from matplotlib import pyplot as plt


def counting_sort(A, M):
    counts = [0]*M
    for v in A: counts[v] += 1
    pos = 0
    v = 0
    while pos < len(A):
        for idx in range(counts[v]):
            A[pos+idx] = v
        pos += counts[v]
        v += 1

def counting_sort_non_for(A, M):
    counts = [0]*M
    for v in A:
        counts[v] += 1
    pos = 0
    v = 0
    while pos < len(A):
        A[pos:pos+counts[v]] = [v]*counts[v]
        pos += counts[v]
        v += 1

def compute_time(func, A, M):
    temp = time.time()
    func(A, M)
    t = time.time()-temp
    return t


N_sample = [2**(10+i) for i in range(12)]
T_ms = [[], []]
times = 10

# print(N)
performaces = [[], []]

for i, N in enumerate(N_sample):
    per_performace = 1
    times_count_performace = times
    t_ms_total_1, t_ms_total_2 = 0, 0
    print(f"N = {N} ({i+1})\ntimes: ")
    
    for j in range(times):
        M = random.randint(0,N//2)
        A = [random.randint(0,M-1) for _ in range(N)]
        B = A.copy()
        
        t_1 = 1000*compute_time(counting_sort, A, M)
        t_ms_total_1 += t_1

        t_2 = 1000*compute_time(counting_sort_non_for, B, M)
        t_ms_total_2 += t_2

        if t_1 == 0 or t_ms_total_1 < t_ms_total_2:
            times_count_performace -= 1
        else:
            per_performace *= 100-(100*t_2)/t_1

        print(f"{j+1}", end = " ", flush = True)

    print(f"\n{times} times for N = {N} complete.\n")

    t_ms_average_1, t_ms_average_2 = t_ms_total_1/times, t_ms_total_2/times
    T_ms[0].append(t_ms_average_1)
    T_ms[1].append(t_ms_average_2)

    if t_ms_average_1 == 0 or t_ms_average_1 < t_ms_average_2:
        performaces[0].append(None)
    else:
        performaces[0].append(round(100-(100*t_ms_average_2)/t_ms_average_1, 2))
    if times_count_performace == 0:
        performaces[1].append(None)
    else:
        performaces[1].append(per_performace**(1/times_count_performace))

fig, axs = plt.subplots(1, 2)

axs[0].plot(N_sample, T_ms[0], marker='o', linestyle='-', label='counting_sort()')
axs[0].plot(N_sample, T_ms[1], marker='^', linestyle='-', label='counting_sort_non_for()')
axs[0].set_title('Algorithm Performance Comparison')
axs[0].set_xlabel('Size (N)')
axs[0].set_xticks([500000*i for i in range(6)])
axs[0].set_ylabel('Elapsed Time (ms)')
axs[0].grid(True)
axs[0].legend()

axs[1].plot(N_sample, performaces[0], marker='p', linestyle='-', color = 'r', label='average')
axs[1].plot(N_sample, performaces[1], marker='v', linestyle='-', color = 'g', label='geomertry')
axs[1].set_title('Performance improvement percentage')
axs[1].set_xlabel('Size (N)')
axs[1].set_xticks([500000*i for i in range(6)])
axs[1].set_ylabel('Performance improvement (%)')
axs[1].set_yticks([10*i for i in range(11)])
axs[1].grid(True)
axs[1].legend()

plt.show()