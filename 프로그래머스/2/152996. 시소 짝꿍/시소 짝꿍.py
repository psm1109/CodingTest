from collections import Counter

def solution(weights):
    answer = 0
    w_cnt = Counter(weights)
    
    for w in set(weights):
        if w_cnt[w] >= 2:
            answer += w_cnt[w] * (w_cnt[w]-1) // 2
        if w * 3/2 in w_cnt:
            answer += w_cnt[w] * w_cnt[w*3/2]
        if w * 4/2 in w_cnt: 
            answer += w_cnt[w] * w_cnt[w*4/2]
        if w * 4/3 in w_cnt: 
            answer += w_cnt[w] * w_cnt[w*4/3]
            
    return answer