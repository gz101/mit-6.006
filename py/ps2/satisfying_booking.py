def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    N = len(R)
    if N == 1:
        return ((1, R[0][0], R[0][1]),)

    # recursively subdivide into two halves
    B1 = satisfying_booking(R[:(N // 2)])
    B2 = satisfying_booking(R[(N // 2):])

    # merge in sorted fashion
    return tuple(_merge(B1, B2))


def _merge(B1, B2):
    i1, i2 = 0, 0
    len_R1, len_R2 = len(B1), len(B2)
    x = 0
    B = []

    while i1 < len_R1 or i2 < len_R2:
        if i1 < len_R1:
            k1, s1, t1 = B1[i1]
        if i2 < len_R2:
            k2, s2, t2 = B2[i2]

        # only B2 elements left
        if i1 == len_R1:
            k, s, x = k2, max(x, s2), t2
            i2 += 1

        # only B1 elements left
        elif i2 == len_R2:
            k, s, x = k1, max(x, s1), t1
            i1 += 1

        # both B1, B2 are not depleted yet
        else:
            # case 1: nothing overlaps with x
            if x < min(s1, s2):
                x = min(s1, s2)

            # case 2: no overlap with another after time x
            if t1 <= s2:
                k, s, x = k1, x, t1
                i1 += 1
            elif t2 <= s1:
                k, s, x = k2, x, t2
                i2 += 1

            # case 3: overlaps with later start after x
            elif x < s2:
                k, s, x = k1, x, s2
            elif x < s1:
                k, s, x = k2, x, s1

            # case 4: overlaps from time x onwards
            else:
                k, s, x = k1 + k2, x, min(t1, t2)
                if t1 == x:
                    i1 += 1
                if t2 == x:
                    i2 += 1

        B.append((k, s, x))

    # iterate through and merge adjacent bookings with equal k's
    res = [B[0]]
    for k, s, t in B[1:]:
        k_, s_, t_ = res[-1]
        if k == k_ and t_ == s:
            res.pop()
            s = s_
        res.append((k, s, t))

    return res
