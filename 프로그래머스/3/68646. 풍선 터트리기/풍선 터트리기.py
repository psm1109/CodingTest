def solution(a):
    answer = 0
    len_a = len(a)
    #a[i]의 값이 좌측기준 최솟값 또는 우측기준 최솟값일 때 남기는 것이 가능
    left_min = [0]*len_a
    right_min = [0]*len_a
    
    lm,rm = 1000000001,1000000001
    for i in range(len_a):
        lm,rm = min(a[i],lm),min(a[len_a-i-1],rm)
        left_min[i],right_min[len_a-i-1] = lm,rm
    
    for i in range(len_a):
        if a[i]==left_min[i] or a[i]==right_min[i]:
            answer += 1
    
    return answer