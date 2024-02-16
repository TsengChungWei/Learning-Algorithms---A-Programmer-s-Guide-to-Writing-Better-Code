# Challenge Exercise 1 (from Table 2-5)

"""
Rate the time complexity of each code fragment in Table 2-5.
"""

# Fragment-1
"""
for i in range(100):
    for j in range(N):
        for k in range(10000):
            ...
"""

"""
Answer:
The Fragment-1 shows that there is a three-layer loop in the algorithm. 
If we give a size N, then the algorithm counts 100*N*10000 times. 
Therefore, the counting function is f(N) = 1000000*N and the complexity
is linear. That is, the algorithm is O(N).
"""

# Fragment-2 
"""
for i in range(N):
    for j in range(N):
        for k in range(100):
            ...
"""

"""
Answer:
The Fragment-2 shows that there is a three-layer loop in the algorithm. 
If we give a size N, then the algorithm counts N*N*10000 times. 
Therefore, the counting function is f(N) = 10000*N**2 and the complexity
is quadratic. That is, the algorithm is O(N**2).
"""


# Fragment-3
"""
for i in range(0,N,2):
    for j in range(0,N,2):
        ...
"""

"""
Answer:
The Fragment-3 shows that there is a two-layer loop in the algorithm. 
If we give a size N, then the algorithm counts (N/2)*(N/2) times. 
Therefore, the counting function is f(N) = (N**2)/4 and the complexity
is quadratic. That is, the algorithm is O(N**2).
"""

# Fragment-4
"""
while N > 1:
    ...
    N = N // 2
"""

"""
Answer:
The Fragment-4 shows that there is a loop in the algorithm. 
If we give a size N, then the algorithm counts log(N)/log(2) times. 
Therefore, the counting function is f(N) = log(N)/log(2) and the complexity
is logarithmic. That is, the algorithm is O(log(N)).
"""

# Fragment-5
"""
for i in range(2,N,3):
    for j in range(3,N,2):
        ...
"""

"""
Answer:
The Fragment-5 shows that there is a two-layer loop in the algorithm. 
If we give a size N, then the algorithm counts ((N-2)/3)*((N-3)/2) times. 
Therefore, the counting function is f(N) = (N**2-5*N+6)/6 and the complexity
is quadratic. That is, the algorithm is O(N**2).
"""