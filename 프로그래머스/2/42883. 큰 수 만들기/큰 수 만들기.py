def solution(number, k):
    answer = ''
    arr = []
    for n in number:
        if arr and arr[-1] < n:
            while k and arr and arr[-1] < n:
                arr.pop()
                k -= 1
        arr.append(n)
    
    return ''.join(arr[:-k] if k else arr)
