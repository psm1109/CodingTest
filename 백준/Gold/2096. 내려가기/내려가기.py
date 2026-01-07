N = int(input())

prev_max = list(map(int,input().split()))
prev_min = prev_max[:]

for _ in range(1,N):
    P = list(map(int,input().split()))
    cur_max,cur_min = [0]*3,[0]*3
    for j in range(3):
        if j == 0:
            cur_max[j] = max(prev_max[0],prev_max[1]) + P[j]
            cur_min[j] = min(prev_min[0],prev_min[1]) + P[j]
        elif j == 1:
            cur_max[j] = max(prev_max[0],prev_max[1],prev_max[2]) + P[j]
            cur_min[j] = min(prev_min[0],prev_min[1],prev_min[2]) + P[j]
        else:
            cur_max[j] = max(prev_max[1],prev_max[2]) + P[j]
            cur_min[j] = min(prev_min[1],prev_min[2]) + P[j]
    prev_max,prev_min = cur_max,cur_min

print(max(prev_max),min(prev_min))