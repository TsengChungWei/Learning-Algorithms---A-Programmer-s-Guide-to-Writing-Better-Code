# Listing 1-10. A linear-time Counting Sort algorithm

import random


def counting_sort(A, M):
    counts = [0]*M
    for v in A:
        counts[v] += 1
    
    pos = 0
    v = 0
    while pos < len(A):
        for idx in range(counts[v]):
            A[pos+idx] = v
        pos += counts[v]
        v += 1

M = 11
A = [random.randint(0, M-1) for _ in range(20)]

print(f"\nA = {A}")
counting_sort(A, M)
print(f"Sorting --> {A}")
        
