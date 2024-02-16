# Listing 2-4. Return location of target in A

def binary_array_search(A, target):
    lo = 0
    hi = len(A) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if target < A[mid]:
            hi = mid-1
        elif target > A[mid]:
            lo = mid+1
        else:
            return mid          # 1
 
    return -(lo+1)              # 2

# 1. Return the value of mid since that is the location of target.
# 2. Alert caller that target doesn’t exist by returning the negative of lo + 1.


A = [3, 14, 15, 19, 26, 53, 58]
target = 17
find = binary_array_search(A, target)

print(f"A = {A}, target = {target} -> {find}")
