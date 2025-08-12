def solution(money):
    l = len(money)
    
    #첫번째 집을 턴 경우
    mm1 = [money[0],max(money[0],money[1])] + [0]*(l-2)
    #첫번째 집을 털지 않은 경우
    mm2 = [0,money[1]] + [0]*(l-2)
    
    for i in range(2,l):
        mm1[i] = max(mm1[i-1],mm1[i-2]+money[i]) if i != l-1 else mm1[i-1]
        mm2[i] = max(mm2[i-1],mm2[i-2]+money[i])
    
    return max(mm1[-1],mm2[-1])