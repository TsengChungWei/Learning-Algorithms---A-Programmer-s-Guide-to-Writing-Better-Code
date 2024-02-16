# Listing 1-2. Correct function to find largest value in list

def largest(A):
    my_max = A[0]                   # 1
    for idx in range(1, len(A)):    # 2
        if my_max < A[idx]:
            my_max = A[idx]         # 3
    return my_max

# 1. Set my_max to the first value in A, found at index position 0.
# 2. idx takes on integer values from 1 up to, but not including, len(A).
# 3. Update my_max if the value in A at position idx is larger.


array = [1, 5, 2, 9, 3, 4]
print(largest(array))

