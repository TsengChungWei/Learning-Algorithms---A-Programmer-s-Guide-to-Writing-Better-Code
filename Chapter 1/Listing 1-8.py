# Listing 1-8. Two methods of checking palindrome

def is_palindrome1(w):
    """Create slice with negative step and confirm equality with w."""
    return w[::-1] == w

def is_palindrome2(w):
    """Strip outermost characters if same, return false when mismatch."""
    while len(w) > 1:
        if w[0] != w[-1]:       # if mismatch, return False
            return False
        w = w[1:-1]             # strip characters on either end; repeat
    
    return True                 #  must have been palindrome


w = "madam"

print(f"'{w}' is a palindrome.")
print(f"First  method: {is_palindrome1(w)}")
print(f"Second method: {is_palindrome2(w)}")
