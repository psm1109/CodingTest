def solution(storey):
    answer = 0
    
    while storey:
        
        r = storey % 10 
        print(storey, f"1의자리 {r}")
        #나머지가 4이하 = 내림 , 6이상 = 올림 , 5는 다음 자릿수에 따라서 결정
        if r <= 4:  #내림
            storey //= 10
            answer += r
        elif r > 5: #올림
            storey = storey // 10 + 1
            answer += (10-r)
        else:
            #내림
            if storey // 10 < 1 or storey // 10 % 10 < 5: 
                storey //= 10
                answer += r
            else: #올림
                storey = storey // 10 + 1
                answer += (10-r)

    return answer