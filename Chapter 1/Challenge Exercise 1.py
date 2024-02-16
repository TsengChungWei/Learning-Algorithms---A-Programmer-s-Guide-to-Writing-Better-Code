# Challenge Exercise 1 (from Listing 1-8)

"""
Palindrome word detector: A palindrome word reads the same backward as for
ward, such as madam. Devise an algorithm that validates whether a word of N
characters is a palindrome. Confirm empirically that it outperforms the two
alternatives in Listing 1-8.

Once you have Listing 1-8 working, modify it to detect palindrome strings with
spaces, punctuation, and mixed capitalization. For example, the following string
should classify as a palindrome: "A man, a plan, a canal. Panama!"
"""

def is_palindrome1(w):
    w = "".join(char.lower() for char in w if char.isalpha())
    return w[::-1] == w

def is_palindrome2(w):
    while len(w) > 1:
        if not w[0].isalpha():
            w = w[1:]
            continue
        if not w[-1].isalpha():
            w = w[:-1]
            continue
        
        if w[0].lower() != w[-1].lower():
            return False
        w = w[1:-1]
    return True


w = "A man, a plan, a canal. Panama!"

print(f"'{w}' is a palindrome.")
print(f"First  method: {is_palindrome1(w)}")
print(f"Second method: {is_palindrome2(w)}")
