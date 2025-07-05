def solution(friends, gifts):
    N = len(friends)
    answer = [0]*N
    
    dict = {}
    for i,friend in enumerate(friends):
        dict[friend] = i
    
    record = [[0]*N for _ in range(N)]
    for gift in gifts:
        a,b = gift.split(" ")
        record[dict[a]][dict[b]] += 1
    
    # 선물 지수
    gift_index = [sum([record[i][j] for j in range(N)]) - sum([record[j][i] for j in range(N)]) for i in range(N)]
    
    
    for i in range(N):
        for j in range(i+1,N):
            if record[i][j] > record[j][i]: 
                answer[i] += 1
            elif record[i][j] < record[j][i]:
                answer[j] += 1
            else: #선물 지수 비교
                if gift_index[i] > gift_index[j]:
                    answer[i] += 1
                elif gift_index[i] < gift_index[j]:
                    answer[j] += 1
    return max(answer)