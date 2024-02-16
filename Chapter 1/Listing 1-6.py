# Listing 1-6. Algorithm to find two largest values in A using tournament

def tournament_two(A):
    N = len(A)
    winner = [None]*(N-1)               # 1
    loser = [None]*(N-1)
    prior = [-1]*(N-1)                  # 2

    idx = 0
    for i in range(0, N, 2):            # 3
        if A[i] < A[i+1]:
            winner[idx] = A[i+1]
            loser[idx] = A[i]
        else:
            winner[idx] = A[i]
            loser[idx] = A[i+1]
        idx += 1

    m = 0                               # 4
    while idx < N-1:
        if winner[m] < winner[m+1]:     # 5
            winner[idx] = winner[m+1]
            loser[idx] = winner[m]
            prior[idx] = m+1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m+1]
            prior[idx] = m
        m += 2                          # 6
        idx += 1

    largest = winner[m]
    second = loser[m]                   # 7
    m = prior[m]
    while m >= 0:
        if second < loser[m]:           # 8
            second = loser[m]            
        m = prior[m]

    return (largest, second)

# 1. These arrays store the winners and losers of match idx; there will be N – 1 of
#    them in the tournament.
# 2. When a value advances in match m, prior[m] records earlier match, or –1 when it
#    was initial match.
# 3. Initialize the first N/2 winner/loser pairs using N/2 invocations of less-than.
#    These represent the matches in the lowest round.
# 4. Pair up winners to find a new winner, and record prior match index.
# 5. An additional N/2 – 1 invocations of less-than are needed.
# 6. Advance m by 2 to find next pair of winners. When idx reaches N – 1, winner[m]
#    is largest.
# 7. Initial candidate for second largest, but must check all others that lost to largest
#    to find actual second largest.
# 8. No more than log(N) – 1 additional invocations of less-than.


array = [3, 1, 4, 1, 5, 9, 2, 6]
print(tournament_two(array))

