def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    def dp(j):
        if memo[j] is None:
            f = min(j + (k - 1) - (j % k) + k, n * k - 1)
            x, r = 1, None
            for d in range(j + 1, f + 1):
                x_, _ = dp(d)
                if (p[j] > p[d]) and (1 + x_ > x):
                    x, r = 1 + x_, d
            memo[j] = (x, r)
        return memo[j]
    
    S = []
    
    for i in range(len(C)):
        p = P[i]
        memo = [None for _ in range(n*k)]
        best, opt = 0, 0
        for j in range(n * k):
            x, _ = dp(j)
            if x > opt:
                best, opt = j, x
        if opt > len(S):
            c, S = C[i], []
            while best != None:
                S.append(p[best])
                _, best = dp(best)
    S = tuple(S)
    return (c, S)
