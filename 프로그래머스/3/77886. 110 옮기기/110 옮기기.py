def solution(arr):
    answer = []
    
    for s in arr:
        stack = []
        cnt = 0
        for c in s:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ["1","1","0"]:
                stack.pop(); stack.pop(); stack.pop()
                cnt += 1
                
        i = ''.join(stack).rfind("0") + 1 #있으면 값 없으면 -1 이므로 없어도 i가 0이 돼 맨 앞에 추가
        stack.insert(i,"110"*cnt)
        answer.append(''.join(stack))
    return answer