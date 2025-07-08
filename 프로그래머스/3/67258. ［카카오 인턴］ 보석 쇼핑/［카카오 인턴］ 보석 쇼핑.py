from collections import defaultdict

def solution(gems):
    gem_count = defaultdict(int)
    type_count = len(set(gems))
    l,r = 0,len(gems)-1
    answer= [l,r]
    
    for r in range(len(gems)):
        #구간 확장
        gem_count[gems[r]] += 1
        # 구간 내 모든 종류의 보석이 들어있다면 최대한 구간을 축소
        while len(gem_count) == type_count:
            # 모든 종류의 보석을 포함한 가장 짧은 구간 갱신
            if r-l < answer[1] - answer[0]:
                answer = [l,r]
            
            gem_count[gems[l]] -= 1
            if gem_count[gems[l]] == 0: 
                gem_count.__delitem__(gems[l])
            l += 1
            
    return [answer[0]+1,answer[1]+1]
            
        