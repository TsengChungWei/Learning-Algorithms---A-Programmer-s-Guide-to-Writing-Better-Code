# Table 2-5.
# Code fragments to analyze

# Fragment-1
"""
for i in range(100):
    for j in range(N):
        for k in range(10000):
            ...
"""

# Fragment-2 
"""
for i in range(N):
    for j in range(N):
        for k in range(100):
            ...
"""

# Fragment-3
"""
for i in range(0,N,2):
    for j in range(0,N,2):
        ...
"""

# Fragment-4
"""
while N > 1:
    ...
    N = N // 2
"""

# Fragment-5
"""
for i in range(2,N,3):
    for j in range(3,N,2):
        ...
"""