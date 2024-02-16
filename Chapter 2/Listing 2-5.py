# Listing 2-5. Optimization that requires just a single value comparison

def binary_array_search(A, target):
    lo = 0
    hi = len(A) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        diff = target - A[mid]
        if diff < 0:
            hi = mid-1
        elif diff > 0:
            lo = mid+1
        else:
            return mid
 
    return -(lo+1)  

A = [16, 55, 98, 173, 429, 643, 818]
target = 173
find = binary_array_search(A, target)

print(f"A = {A}, target = {target} -> {find}")
