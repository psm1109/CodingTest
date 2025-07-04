import math

def solution(arrayA, arrayB):
    answer = 0
    gcdA,gcdB = arrayA[0],arrayB[0]
    
    for i in range(1,len(arrayA)):
        gcdA = math.gcd(gcdA,arrayA[i])
        gcdB = math.gcd(gcdB,arrayB[i])
        
    A,B = True,True
    for n in arrayA:
        if n % gcdB == 0:
            B = False
            break
    for n in arrayB:
        if n % gcdA == 0:
            A = False
            break
            
    if A and B: return max(gcdA,gcdB)
    elif A: return gcdA
    elif B : return gcdB
    else: return 0
        
