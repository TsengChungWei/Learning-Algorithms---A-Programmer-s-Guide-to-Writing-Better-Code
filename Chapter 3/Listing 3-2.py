# Listing 3-2. Convert word to an integer assuming base 26

def base26(w):
    val = 0
    for ch in w.lower():                    # 1
        next_digit = ord(ch) - ord('a')     # 2
        val = 26*val + next_digit           # 3
    return val

# 1. Convert all characters to lowercase.
# 2. Compute digit in next position.
# 3. Accumulate total and return.

w = "June"
print(base26(w))
