# Challenge Exercise 2 (from Listing 2-6)

"""
Use the techniques described in this chapter to model the value of ct returned by
the f4 function in Listing 2-6.

You will find that none of the models used in this chapter is accurate. Instead,
develop one based on a*log(log(N)), in base 2. Generate a table up to N = 250
containing actual results as compared to the model. An algorithm with this
behavior would be classified as O(log(log(N))).
"""

def f4(N):
    ct = 0
    while N >= 2:
        ct = ct + 1
        N = N ** 0.5
    return ct

def test(N):
    ct = 0
    while N > 1:
        ct += 1
        N = N//2
    return ct

N = 65536
print(f4(N))
