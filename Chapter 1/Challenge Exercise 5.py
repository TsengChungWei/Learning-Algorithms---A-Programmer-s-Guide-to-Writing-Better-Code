# Challenge Exercise 5 (from Listing 1-11)

"""
Will the code in Listing 1-11 correctly locate the two largest values in A?

Explain the circumstances when this code works correctly and when it fails.
"""

import random


def two_largest_attempt(A):
    m1 = max(A[:len(A)//2])
    m2 = max(A[len(A)//2:])
    if m1 < m2:
        return (m2, m1)
    return (m1, m2)

"""
Answer:
The code simply finds the maximums of the first half of the list and the second half of the list.
But if the first and second maximums are both in the first half list or the second half list.
It will give a wrong answer.
"""