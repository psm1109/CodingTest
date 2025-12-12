N,r,c = map(int,input().split()) 

def Z(N,r,c,result):
    if N == 1:
        return result
    else:
        if r < N//2 and c < N//2: 
            return Z(N//2,r,c,result)
        elif r < N//2 and c >= N//2: 
            return Z(N//2,r,c-N//2,result+pow(N//2,2))
        elif r >= N//2 and c < N//2: 
            return Z(N//2,r-N//2,c,result+pow(N//2,2)*2)
        else: 
            return Z(N//2,r-N//2,c-N//2,result+pow(N//2,2)*3)
    
print(Z(2**N,r,c,0))
