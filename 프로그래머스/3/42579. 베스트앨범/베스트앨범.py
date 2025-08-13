from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    play_dict = defaultdict(list)
    play_total = defaultdict(int)
    
    for i, g in enumerate(genres):
        play_dict[g].append([i ,plays[i]])
        play_total[g] += plays[i]

    for i in play_dict.keys():
        play_dict[i].sort(key = lambda x : (-x[1],x[0]))

    for i in sorted(play_total.items(), key = lambda x : -x[1]):
            answer.append(play_dict[i[0]][0][0])
            if len(play_dict[i[0]]) >= 2:
                answer.append(play_dict[i[0]][1][0])
    return answer
