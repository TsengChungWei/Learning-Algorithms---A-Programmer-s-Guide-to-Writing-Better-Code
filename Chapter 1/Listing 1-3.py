# Listing 1-3. A different approach to locating largest value in A

def alternate(A):    
    for v in A:
        v_is_larest = True          # 1
        for x in A:
            if v < x:
                v_is_larest = False # 2
                break
        if v_is_larest:
            return v                # 3
    return None                     # 4

# 1. When iterating over A, assume each value, v, could be the largest.
# 2. If v is smaller than another value, x, stop and record that v is not greatest.
# 3. If v_is_largest is true, return v since it is the maximum value in A.
# 4. If A is an empty list, return None.


array = [1, 5, 2, 9, 3, 4]
print(alternate(array))

