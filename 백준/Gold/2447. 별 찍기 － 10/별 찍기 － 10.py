import sys
sys.setrecursionlimit(10**6)
N = int(input())


def print_star(len:int):
    if len == 1:
        return ["*"]

    inner = print_star(len//3)

    result = []
    for s in inner:
        result.append(s*3)
    for s in inner:
        result.append(s+" "*(len//3)+s)
    for s in inner:
        result.append(s*3)
    return result

print('\n'.join(print_star(N)))