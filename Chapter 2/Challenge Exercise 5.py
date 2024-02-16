# Challenge Exercise 5 (from Listing 2-8)

"""
Using the results I have outlined in this chapter, assess the storage complexity of
max_sort.

1. def max_sort(A):
2.     result = []
3.     while len(A) > 1:
4.         index_max = max(range(len(A)), key=A.__getitem__)
5.         result.insert(0, A[index_max])
6.         A = list(A[:index_max]) + list(A[index_max+1:])
7.     return A + result
"""

from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def storage_count(N):
        count = 0
        length = N
        while length > 1:
            length -= 1
            count += 1       
        return count+1

class algorithm():
    def linear_model(n, a, b):
        return a*n + b
    
    def quadratic_model(n, a, b):
        return a*n*n + b*n

    def regression(xs, ys, func, model, left=0, right=10000, cut=100):
        if func:
            ys = [func(x) for x in xs]
        
        [(a,b), _]   = curve_fit(model, np.array(xs), np.array(ys))
        a, b = round(a, 5), round(b, 5)
        
        x = np.linspace(left, right, cut)
        y = model(x, a, b)

        plt.plot(x, y, label='', color='b')
        plt.plot(xs, ys, marker='o', linestyle='', color='r')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title("algorithm Analysis")
        plt.show()

xs = [2**(i+5) for i in range(6)]

algorithm.regression(xs, None, storage_count, algorithm.linear_model, 0, 1100, 100)


"""
Answer:
We have an array A, and we can analyze the algorithm as follows. Line 2 initializes 
an empty array "result" to store the numbers. Line 3 sets up a loop for sorting. 
Line 4 initializes a variable "index_max" to store the index of the maximum value 
in array A. Then, line 5 inserts the maximum value into the "result" array at 
position 0 using "index_max." Next, line 6 removes the maximum value from A.

Since we have set up this loop, it continues until it finds the minimum value in A. 
Each iteration finds the maximum value in A, removes it, and inserts it into "
result" at the beginning. This process repeats until the array A is sorted.

According to the algorithm, we save "result" and "index_max." As we can determine 
the size (N) of array A, "result" starts empty but adds a number with each iteration. 
Therefore, it stores N-1 numbers when we complete the loops. We also save one number, 
"index_max." Thus, in total, we store N numbers throughout the entire algorithm. 
Consequently, the storage complexity is O(N).
"""