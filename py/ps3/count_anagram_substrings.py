ORD_A = ord("a")


def lower_ord(c):
    return ord(c) - ORD_A


def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    H = {}
    F = [0] * 26
    k = len(S[0])

    # compute frequency tables in T
    for i in range(len(T)):
        F[lower_ord(T[i])] += 1
        if i > k - 1:
            F[lower_ord(T[i - k])] -= 1
        if i >= k - 1:
            key = tuple(F)  # key needs to be immutable
            H[key] = 1 + H.get(key, 0)

    # compute char counts of s
    for s in S:
        F = [0] * 26
        for c in s:
            F[lower_ord(c)] += 1
        key = tuple(F)
        A.append(H.get(key, 0))

    return tuple(A)
