def solution(numbers):
    answer = []
    for n in numbers:
        if n%2==0: #짝수의 경우 첫번째 비트가 0이므로 +1을 하면 비트가 1개 차이난다.
            answer.append(n+1)
        else: #홀수의 경우 가장 오른쪽의 0을 1로 그 뒤의 1을 0으로 바꿔주면 2개 차이남
            bn = bin(n)
            if bn[2:].find("0") == -1:
                answer.append(int("0b"+"10"+bn[3:],2))
            else:
                answer.append(int(bn[::-1].replace("10","01",1)[::-1],2))
    return answer