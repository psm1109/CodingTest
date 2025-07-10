def solution(number, k):
    answer = ''
    arr = []
    for n in number:
        if not arr or arr[-1] >= n:
            arr.append(n)
        else: #arr and arr[-1] < n:
            while k>0 and arr and arr[-1] < n:
                arr.pop()
                k -= 1
            arr.append(n)
    
    if k:
        return ''.join(arr[:-k])
    else:
        return ''.join(arr)
        
