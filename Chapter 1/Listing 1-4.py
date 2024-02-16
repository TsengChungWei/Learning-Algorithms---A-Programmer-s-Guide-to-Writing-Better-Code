# Listing 1-4. Find two largest values by tweaking largest() approach

def largest_two(A):
    my_max, second = A[:2]                      # 1
    if my_max < second:
        my_max, second = second, my_max

    for idx in range(2, len(A)):
        if my_max < A[idx]:                     # 2
            my_max, second = A[idx], my_max
        elif second < A[idx]:                   # 3
            second = A[idx]
    return (my_max, second)

# 1. Ensure my_max and second are the first two values from A in descending order.
# 2. If A[idx] is a newly found maximum value, then set my_max to A[idx], and 
#    second becomes the old my_max.
# 3. If A[idx] is larger than second (but smaller than my_max), only update second.


array = [1, 5, 2, 9, 3, 4]
print(largest_two(array))

