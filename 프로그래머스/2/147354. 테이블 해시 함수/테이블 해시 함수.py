def solution(data, col, row_begin, row_end):
    #2
    data.sort(key=lambda x : (x[col-1],-x[0]))
    
    #4
    answer = sum([data%row_begin for data in data[row_begin-1]])
    for i in range(row_begin+1,row_end+1):
        answer = answer ^ sum([data%i for data in data[i-1]])
    
    return answer