# Listing 2-2. Using grade-school algorithm to multiply two N-digit integers

"""
   456                  123456
 x 712                x 712835
   ---                  ------
   912                  617280
  456                  370368
3192                  987648
------               246912
324672              123456
                   864192
                   ----------
                   88003757760
"""

import random


def int_to_list(n):
    arr = []
    while n >= 1:
        arr.append(n%10)
        n = n//10
    return arr

def multiplication_test(a, b):
    a = int_to_list(a)
    b = int_to_list(b)
    length = 2*len(a)
    arr = [0]*length
    for i, n in enumerate(b):
        for j, m in enumerate(a):
            carry, origin = (m*n)//10, (m*n)%10
            arr[i+j] += origin
            arr[i+j+1] += carry
        
    for i in range(length):
        carry, origin = arr[i]//10, arr[i]%10
        arr[i] = origin
        if i < length-1:
            arr[i+1] += carry

    result = 0
    for i, n in enumerate(arr):
        result += n*10**i
    return result

def multiplication(a, b):
    a = int_to_list(a)
    b = int_to_list(b)
    len_a = len(a)
    len_b = len(b)
    arr = [[0 for _ in range(len_a)] for _ in range(len_b)]
    for i, n in enumerate(b):
        temp = 0
        for j, m in enumerate(a):
            carry = (m*n)//10
            arr[i][j] = (m*n)%10 + temp

            carry_temp = arr[i][j]//10
            arr[i][j] = arr[i][j]%10

            temp = carry + carry_temp
        if temp != 0:
            arr[i].append(temp)
            
    # print(arr)
    result = [0]*(len_a+len_b)
    carry = 0
    for k in range(len_a+len_b):
        s = 0
        for i in range(k+1):
            if i < len(arr) and k-i < len(arr[i]):
                s += arr[i][k-i]

            result[k] = s + carry
        carry = result[k]//10
        result[k] = result[k]%10

    answer = 0
    for i, n in enumerate(result):
        answer += n*10**i
    return answer


# print(multiplication(49, 99, 2))
# print(multiplication(456, 712, 3))
# print(multiplication(123456, 712835, 6))


# N_sample = [2**(8+i) for i in range(7)]
N_sample = [i+1 for i in range(1, 10)]
for N in N_sample:
    a = random.randint(10**(N-1), 10**N-1)
    b = random.randint(10**(N-1), 10**N-1)
    mult = multiplication(a, b) 
    print(f"{a} x {b} = {mult}, {mult == a*b}")
