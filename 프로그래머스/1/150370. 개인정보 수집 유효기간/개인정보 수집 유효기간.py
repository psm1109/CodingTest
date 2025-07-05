def convert(date):
    #1개월=28일, 12개월=336일
    y,m,d = map(int,date.split("."))
    return y*336 + m*28 + d
    
def solution(today, terms, privacies):
    answer = []
    
    dict = {t.split(" ")[0]:(int(t.split(" ")[1])*28) for t in terms}
    
    for i,p in enumerate(privacies):
        date,term = p.split(" ")
        if convert(today) >= convert(date) + dict[term]:
            answer.append(i+1)
    return answer