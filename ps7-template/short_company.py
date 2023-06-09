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
    c = C[0]
    S = []
    ##################
    num_pts = n*k
    longest_across_companies_parents = {}
    longest_across_companies = 0
    longest_across_companies_pos = ()
    longest_company = ''
    longest_runs = {}
    longest_prices = []

    def add_entry(d, i, j, val):
        if i in d:
            d[i][j] = val
        else:
            d[i] = {i: val}
        return d
    
    for company, p in zip(C, P):
        longest_seen = 0
        longest_seen_pos = ()
        longest_so_far = {}
        parents = {}

        # initialize runs of length 1 beginning at each different index
        for i in range(0, num_pts):
            longest_so_far = add_entry(longest_so_far, i, i, 1)
            parents = add_entry(parents, i, i, (i, i))

        # find longest run
        for j in range(num_pts-1, 0, -1): # last pointer
            lower_bound = max(0, j-(2*k))
            for i in range(j, lower_bound-1, -1): # first pointer
                # are the two pointers within 1 day of each other?
                if (int(j / k) - int(i / k)) > 1:
                    continue
                    # longest_so_far = add_entry(longest_so_far, i, j, 1)
                    # parents = add_entry(parents, i, j, (i, j))
                if p[i] > p[j]:
                    new_long = 1 + longest_so_far[j][j]
                    if (new_long > longest_seen):
                        longest_seen = new_long
                        longest_seen_pos = (i, i) # set longest position as (i, i) for convenience down the line
                    if (new_long > longest_so_far[i][i]):
                        longest_so_far[i][i] = new_long
                        parents[i][i] = (i, j)
                    parents = add_entry(parents, i, j, (j, j))
                    # longest_so_far = add_entry(longest_so_far, i, i, new_long)

        if (longest_seen > longest_across_companies):
            longest_across_companies = longest_seen
            longest_across_companies_parents = parents
            longest_across_companies_pos = longest_seen_pos
            longest_company = company
            longest_prices = p

    # build S
    i = longest_across_companies_pos[0]
    j = longest_across_companies_pos[1]
    while longest_across_companies_parents[i][j] != (i, j):
        (new_i, new_j) = longest_across_companies_parents[i][j]
        if i == j:
            S.append(longest_prices[i])
        (i, j) = (new_i, new_j)
    S.append(longest_prices[i])
    c = longest_company
    # import pdb; pdb.set_trace()
    
    ##################
    return (c, S)
