def solution(stones, k):
    answer = 0
    left,right = 1 , max(stones)
    
    while left <= right:
        mid = (left+right)//2
        
        cnt = 0
        flag = True
        for s in stones:
            if s - mid < 0:
            	cnt += 1
                
            	if cnt == k: 
                	flag = False
                	break
            else:
                cnt = 0    
        
        if flag: #건널 수 있을 때 범위 확장, 인원 갱신
            left = mid+1
            answer = mid
        else: #건널 수 없으면 범위 축소
            right = mid-1
        
    return answer