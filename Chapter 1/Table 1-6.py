# Table 1-6 (from Listing 1-7). Counting operations in four different functions

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

s = ["N", "|", "f0(N)", "f1(N)", "f2(N)", "f3(N)"]
print(f"\n{s[0]:<7} {s[1]:<3} {s[2]:<7} {s[3]:<7} {s[4]:<7} {s[5]:<7}")
print("-"*43)
for N in [512, 1024, 2048]:
    print(f"{N:<7} {s[1]:<3} {f0(N):<7} {f1(N):<7} {f2(N):<7} {f3(N):<7}")