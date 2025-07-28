from collections import deque

def solution(begin, target, words):
    answer = 0
    
    #변환할 수 없는 경우 0 반환
    if target not in words:
        return 0
    
    queue = deque([[begin,0]])
    while queue:
        current,cnt = queue.popleft()
        for i in range(len(words)):
            if sum(c1 != c2 for c1,c2 in zip(current,words[i])) == 1:
                if words[i] == target:
                    return cnt+1
                queue.append([words[i],cnt+1])
                words[i] = ""
            
    return 0