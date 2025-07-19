def convert(time):
    a,b = time.split(":")
    return int(a) * 60 + int(b)

def solution(book_time):
    book_time.sort()
    answer = [[]]
    
    for t in book_time: 
        start,end = map(convert,t)
        flag = False
        for room in answer:
            if not room or room[-1][1]+10 <= start:
                room.append([start,end])
                flag = True
                break
        if not flag:
            answer.append([[start,end]])
            
    return len(answer)