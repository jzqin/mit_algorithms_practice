def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    max_substr_len = 0
    substr_len = 0
    for i in range(len(A)-1):
        if A[i+1] > A[i]:
            substr_len += 1
            if substr_len > max_substr_len:
                max_substr_len = substr_len
        else:
            substr_len = 0

    substr_len = 0
    for i in range(len(A)-1):
        if A[i+1] > A[i]:
            substr_len += 1
            if substr_len == max_substr_len:
                count +=1
        else:
            substr_len = 0
            
    ##################
    return count
