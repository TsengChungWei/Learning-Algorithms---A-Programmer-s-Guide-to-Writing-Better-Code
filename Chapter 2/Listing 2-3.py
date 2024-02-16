# Listing 2-3. Binary Array Search

def binary_array_search(A, target):
    lo = 0
    hi = len(A) - 1             # 1

    while lo <= hi:             # 2
        mid = (lo + hi) // 2    # 3

        if target < A[mid]:     # 4
            hi = mid-1
        elif target > A[mid]:   # 5
            lo = mid+1
        else:
            return True         # 6
 
    return False                # 7

# 1. Set lo and hi to be inclusive within list index positions of 0 and len(A)–1.
# 2. Continue as long as there is at least one value to explore.
# 3. Find midpoint value, A[mid], of remaining range A[lo .. hi].
# 4. If target is smaller than A[mid], continue looking to the left of mid.
# 5. If target is larger than A[mid], continue looking to the right of mid.
# 6. If target is found, return True.
# 7. Once lo is greater than hi, there are no values remaining to search. Report that
#    target is not in A.


A = [3, 14, 15, 19, 26, 53, 58]
target = 53
find = binary_array_search(A, target)

print(f"A = {A}, target = {target} -> {find}")
