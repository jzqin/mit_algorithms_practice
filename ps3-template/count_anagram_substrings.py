def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []

    if (len(T) == 0):
        return A
    if (len(S) == 0):
        return A

    k = len(S[0])
    
    def build_hash_table(T, k):
        substr_hash_table = {}

        counts = [0 for x in range(26)]
        # populate the first k letters first
        for i in range(k):
            letter = ord(T[i]) - 97 # subtract 97, which is value of 'a' in ASCII
                                    # so that indicies for 'a' to 'z' span 0 to 25
            counts[letter] += 1

        substr_hash_table[tuple(counts)] = 1

        for i in range(k, len(T)):
            prev_letter = ord(T[i-k]) - 97
            new_letter = ord(T[i]) - 97

            counts[prev_letter] -= 1
            counts[new_letter] += 1

            if tuple(counts) not in substr_hash_table:
                substr_hash_table[tuple(counts)] = 1
            else:
                substr_hash_table[tuple(counts)] += 1

        return substr_hash_table

    def compute_anagrams(hash_table, S):
        A = []
        for substr in S:
            counts = [0 for x in range(26)]
            for i in range(len(substr)):
                letter = ord(substr[i]) - 97
                counts[letter] += 1
            counts = tuple(counts)
            if counts not in hash_table:
                A.append(0)
            else:
                A.append(hash_table[counts])

        return A

    hash_table = build_hash_table(T, k)
    A = compute_anagrams(hash_table, S)

    return tuple(A)
