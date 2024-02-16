# Listing 1-7. Four different functions with different performance profiles

def f0(N):
    ct = 0
    ct += 1
    ct += 1
    return ct

def f1(N):
    ct = 0
    for i in range(N):
        ct += 1
    return ct

def f2(N):
    ct = 0
    for i in range(N):
        ct += 1
        ct += 1
        ct += 1
        ct += 1
        ct += 1
        ct += 1
        ct += 1
    return ct

def f3(N):
    ct = 0
    for i in range(N):
        for j in range(N):
            ct += 1
    return ct
