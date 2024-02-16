
import time
import random

from matplotlib import pyplot as plt

def flawed(A):
    my_max = 0
    for v in A:
        if my_max < v:
            my_max = v    
    return my_max

def largest(A):
    my_max = A[0]
    for idx in range(1, len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
    return my_max

def alternate(A):    
    for v in A:
        v_is_larest = True
        for x in A:
            if v < x:
                v_is_larest = False
                break
        if v_is_larest:
            return v
    
    return None

N = [2**(10+i) for i in range(12)]
T_ms = [[], [], [], []]
# print(N)

for i, n in enumerate(N):
    array = [random.randint(-10*n,10*n) for _ in range(n)]
    
    temp = time.time()
    maximum = max(array)
    t = time.time()-temp
    t *= 1000
    T_ms[0].append(t)

    temp = time.time()
    result = flawed(array)
    t = time.time()-temp
    t *= 1000
    T_ms[1].append(t)

    temp = time.time()
    result = largest(array)
    t = time.time()-temp
    t *= 1000
    T_ms[2].append(t)

    if i < 11:
        temp = time.time()
        result = alternate(array)
        t = time.time()-temp
        t *= 1000
        T_ms[3].append(t)
    else:
        T_ms[3].append(None)

# print(T_ms)
plt.plot(N, T_ms[0], marker='o', linestyle='-', label='max() function')
plt.plot(N, T_ms[1], marker='^', linestyle='-', label='flawed()')
plt.plot(N, T_ms[2], marker='*', linestyle='-', label='largest()')
plt.plot(N, T_ms[3], marker='+', linestyle='-', label='alternate()')

plt.title('Algorithm Performance Comparison')
plt.xlabel('Size (N)')
plt.xticks([500000*i for i in range(6)])
plt.ylabel('Elapsed Time (ms)')
plt.yticks([50*i for i in range(8)])
plt.grid(True)
plt.legend()

plt.show()