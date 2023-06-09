def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    starts = [x[0] for x in R]
    ends = [x[1] for x in R]

    starts = merge_sort(starts)
    ends = merge_sort(ends)

    start_idx = 0
    end_idx = 0

    curr_time = starts[0]
    num_rooms = 0
    while (start_idx < len(starts)) or (end_idx < len(ends)):
        while (start_idx < len(starts)) and (curr_time == starts[start_idx]):
            num_rooms += 1
            start_idx += 1
        while (end_idx < len(ends)) and  (curr_time == ends[end_idx]):
            num_rooms -= 1
            end_idx += 1

        if (num_rooms == 0):
            continue
        
        if (start_idx == len(starts)):
            next_time = ends[end_idx]
        else:
            next_time = min(starts[start_idx], ends[end_idx])

        if (len(B) > 0) and (B[-1][0] == num_rooms):
            prev_time = B[-1][1]
            del(B[-1])
            B.append((num_rooms, prev_time, next_time))
        else:
            B.append((num_rooms, curr_time, next_time))

        curr_time = next_time            
    
    return tuple(B)

def merge_sort(X):
    def merge(arr, i, j):
        if (i+1 == j):
            return

        if (i+2 == j):
            j -= 1    # decrement j since it normally points
                      # one position past the second position in the array
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
            return
        
        c = (i+j) // 2
        merge(arr, i, c)
        merge(arr, c, j)

        temp_arr1 = arr[i:c]
        temp_arr2 = arr[c:j]
        idx1 = 0
        idx2 = 0
        for k in range(i, j):
            if (idx1 == len(temp_arr1)):
                arr[k:j] = temp_arr2[idx2:]
                break
            if (idx2 == len(temp_arr2)):
                arr[k:j] = temp_arr1[idx1:]
                break
            if (temp_arr1[idx1] > temp_arr2[idx2]):
                arr[k] = temp_arr2[idx2]
                idx2 += 1
            else:
                arr[k] = temp_arr1[idx1]
                idx1 += 1
        return
    
    start = 0
    end = len(X)
    merge(X, start, end)

    return X

def main():
    test1 = [1, 2, 3, 4, 5]
    out1 = [1, 2, 3, 4, 5]
    res1 = merge_sort(test1)
    assert(res1 == out1)
    
    test2 = [2, 1, 3, 5, 2, 1, 6, 3]
    out2 = [1, 1, 2, 2, 3, 3, 5, 6]
    res2 = merge_sort(test2)
    assert(res2 == out2)
    
    test3 = [5, 4, 3, 2]
    out3 = [2, 3, 4, 5]
    res3 = merge_sort(test3)
    assert(res3 == out3)

if __name__ == '__main__':
    main()
    
