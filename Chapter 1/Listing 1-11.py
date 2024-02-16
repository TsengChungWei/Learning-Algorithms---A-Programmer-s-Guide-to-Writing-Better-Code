# Listing 1-11. Another attempt to try to compute two largest values in unordered list

def two_largest_attempt(A):
    m1 = max(A[:len(A)//2])
    m2 = max(A[len(A)//2:])
    if m1 < m2:
        return (m2, m1)
    return (m1, m2)

# wrong algorithm