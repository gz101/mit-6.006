def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 1
    N = len(A)
    curLen, curMax = 1, 1

    for i in range(1, N):
        if A[i] > A[i - 1]:
            curLen += 1
        else:
            curLen = 1

        if curLen == curMax:
            count += 1
        elif curLen > curMax:
            curMax = curLen
            count = 1

    return count
