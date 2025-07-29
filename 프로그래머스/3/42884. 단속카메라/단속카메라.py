def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    
    arr=[]
    for route in routes:
        if not arr or arr[0][1] >= route[0]:
            arr.append(route)
        else:
            arr = [route]
            answer += 1
    return answer + 1
        