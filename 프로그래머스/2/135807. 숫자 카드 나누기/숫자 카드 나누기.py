import math

def get_gcd(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
    return gcd

def is_valid(divisor, array):
    for num in array:
        if num % divisor == 0:
            return False
    return True

def solution(arrayA, arrayB):
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)
    
    validA = is_valid(gcdA, arrayB)
    validB = is_valid(gcdB, arrayA)
    
    if validA and validB:
        return max(gcdA, gcdB)
    elif validA:
        return gcdA
    elif validB:
        return gcdB
    else:
        return 0