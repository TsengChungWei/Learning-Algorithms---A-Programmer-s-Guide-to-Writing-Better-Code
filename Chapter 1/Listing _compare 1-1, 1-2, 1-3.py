
import time
import random

array = [random.randint(-10**7,10**7) for _ in range(10**5)]
# array = [i+1 for i in range(10000)]
# array = [i+1 for i in reversed(range(10000))]
temp = time.time()
maximum = max(array)
max_t = time.time()-temp
print(f"\nAnswer: {maximum}, runtime: {round(max_t*1000, 3)} ms.\n")

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

# array = [1, 5, 2, 9, 3, 4]

temp = time.time()
result_flawed = flawed(array)
t_flawed = time.time()-temp
print(f"ex 1-1:\n {result_flawed == maximum} answer, \n time: {round(t_flawed*1000, 3)} ms\n")

temp = time.time()
result_largest = largest(array)
t_largest = time.time()-temp
print(f"ex 1-2:\n {result_largest == maximum} answer, \n time: {round(t_largest*1000, 3)} ms\n")

temp = time.time()
result_alternate = alternate(array)
t_alternate = time.time()-temp

print(f"ex 1-3:\n {result_alternate == maximum} answer, \n time: {round(t_alternate*1000, 3)} ms\n")


