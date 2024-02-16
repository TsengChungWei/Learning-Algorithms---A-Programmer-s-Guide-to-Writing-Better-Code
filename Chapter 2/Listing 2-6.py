# Listing 2-6. Sample function to analyze

def f4(N):
    ct = 1
    while N >= 2:
        ct = ct + 1
        N = N ** 0.5
    return ct

N_sample = [2**(10+i) for i in range(12)]

for N in N_sample:
    count = f4(N)
    print(f"{N}: {count}")
