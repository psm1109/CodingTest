def solution(sequence):
    answer = 0
    ps1 = [sequence[i] * pow(-1,i) for i in range(len(sequence))]
    ps2 = [n * -1 for n in ps1]
    
    current_max1,current_max2 = ps1[0],ps2[0]
    for i in range(1,len(sequence)):
        current_max1 = max(ps1[i],current_max1+ps1[i])
        ps1[i] = current_max1
        current_max2 = max(ps2[i],current_max2+ps2[i])
        ps2[i] = current_max2
    
    return max(max(ps1),max(ps2))