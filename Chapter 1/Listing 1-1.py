# Listing 1-1. Flawed implementation to locate largest value in list

def flawed(A):
    my_max = 0              # 1
    for v in A:             # 2
        if my_max < v:
            my_max = v      # 3
    return my_max

# 1. my_max is a variable that holds the maximum value; here my_max is initialized to 0.
# 2. The for loop defines a variable v that iterates over each element in A. The if 
#    statement executes once for each value, v.
# 3. Update my_max if v is larger.


array = [1, 5, 2, 9, 3, 4]
print(flawed(array))

