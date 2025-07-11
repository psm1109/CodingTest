def solution(sequence, k):
    len_sequence = len(sequence)
    answer = [0,len_sequence-1]
    l = 0
    
    result = 0
    for r in range(len_sequence): 
        result += sequence[r]
        
        while result > k:
            result -= sequence[l]
            l += 1
        
        if result == k:
                if answer[1]-answer[0] > r-l:
                    answer = [l,r]
              
    return answer