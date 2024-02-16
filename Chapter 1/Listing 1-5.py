# Listing 1-5. Three different approaches using Python utilities

def sorting_two(A):
    return tuple(sorted(A, reverse=True)[:2])   # 1

def double_two(A):
    my_max = max(A)                             # 2
    copy = list(A)
    copy.remove(my_max)                         # 3
    return (my_max, max(copy))                  # 4

def mutable_two(A):
    idx = max(range(len(A)), key=A.__getitem__) # 5
    my_max = A[idx]                             # 6
    del A[idx]
    second = max(A)                             # 7
    A.insert(idx, my_max)                       # 8
    return (my_max, second)

# 1. Create a new list by sorting A in descending order and return its top two values.
# 2. Use built-in max() function to find largest.
# 3. Create a copy of the original A, and remove my_max.
# 4. Return a tuple containing my_max and the largest value in copy.
# 5. This Python trick finds the index location of the maximum value in A, rather than
#    the value itself.
# 6. Record my_max value and delete it from A.
# 7. Now find max() of remaining values.
# 8. Restore A by inserting my_max to its original location.


array = [1, 5, 2, 9, 3, 4]
print(mutable_two(array))

