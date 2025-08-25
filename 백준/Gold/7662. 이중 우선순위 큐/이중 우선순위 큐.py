import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):  # 테스트 케이스 수
    max_heap = []
    min_heap = []
    dic = defaultdict(int)

    for _ in range(int(input())):  # 연산 수
        c, n = input().split()
        n = int(n)

        if c == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            dic[n] += 1

        elif c == "D":
            if n == 1:
                while max_heap:
                    num = -heapq.heappop(max_heap)
                    if dic[num] > 0:
                        dic[num] -= 1
                        break
            elif n == -1:
                while min_heap:
                    num = heapq.heappop(min_heap)
                    if dic[num] > 0:
                        dic[num] -= 1
                        break

    valid = [k for k in dic if dic[k] > 0]
    print(f"{max(valid)} {min(valid)}" if valid else "EMPTY")
