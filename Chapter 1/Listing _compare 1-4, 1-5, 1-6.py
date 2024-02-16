import time
import random

n = 1048576
array = [random.randint(-10*n,10*n) for _ in range(n)]
# array = [i+1 for i in range(n)]
first_max = max(array)
copy = list(array)
copy.remove(first_max)
second_max = max(copy)
print(f"\nAnswer: {(first_max, second_max)}\n")

def largest_two(A):
    my_max, second = A[:2]
    if my_max < second:
        my_max, second = second, my_max
    for idx in range(2, len(A)):
        if my_max < A[idx]:
            my_max, second = A[idx], my_max
        elif second < A[idx]:
            second = A[idx]
    return (my_max, second)

def sorting_two(A):
    return tuple(sorted(A, reverse=True)[:2])

def double_two(A):
    my_max = max(A)
    copy = list(A)
    copy.remove(my_max)
    return (my_max, max(copy))

def mutable_two(A):
    idx = max(range(len(A)), key=A.__getitem__)
    my_max = A[idx]
    del A[idx]
    second = max(A)
    A.insert(idx, my_max)
    return (my_max, second)

def tournament_two(A):
    N = len(A)
    winner = [None]*(N-1)
    loser = [None]*(N-1)
    prior = [-1]*(N-1)
    idx = 0
    for i in range(0, N, 2):
        if A[i] < A[i+1]:
            winner[idx] = A[i+1]
            loser[idx] = A[i]
        else:
            winner[idx] = A[i]
            loser[idx] = A[i+1]
        idx += 1
    m = 0
    while idx < N-1:
        if winner[m] < winner[m+1]:
            winner[idx] = winner[m+1]
            loser[idx] = winner[m]
            prior[idx] = m+1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m+1]
            prior[idx] = m
        m += 2
        idx += 1
    largest = winner[m]
    second = loser[m]
    m = prior[m]
    while m >= 0:
        if second < loser[m]:
            second = loser[m]            
        m = prior[m]
    return (largest, second)


temp = time.perf_counter()
result = largest_two(array)
t = time.perf_counter()-temp
print(f"ex 1-4(largest_two):\n {result == (first_max, second_max)} answer, \n time: {round(t*1000, 3)} ms\n")

temp = time.perf_counter()
result = sorting_two(array)
t = time.perf_counter()-temp
print(f"ex 1-5(sorting_two):\n {result == (first_max, second_max)} answer, \n time: {round(t*1000, 3)} ms\n")

temp = time.perf_counter()
result = double_two(array)
t = time.perf_counter()-temp
print(f"ex 1-5(double_two):\n {result == (first_max, second_max)} answer, \n time: {round(t*1000, 3)} ms\n")

temp = time.perf_counter()
result = mutable_two(array)
t = time.perf_counter()-temp
print(f"ex 1-5(mutable_two):\n {result == (first_max, second_max)} answer, \n time: {round(t*1000, 3)} ms\n")

temp = time.perf_counter()
result = tournament_two(array)
t = time.perf_counter()-temp
print(f"ex 1-5(tournament_two):\n {result == (first_max, second_max)} answer, \n time: {round(t*1000, 3)} ms\n")