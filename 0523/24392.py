N, M = map(int, input().split())

for i in range(N):
    if i == 0:
        glass = list(map(int, input().split()))
    else:
        tmp_lst = list(map(int, input().split()))
        for j in range(M):
            if tmp_lst[j] == 0:
                continue
            tmp = glass[j]
            if j-1 >= 0:
                tmp += glass[j-1]
            if j+1 < M:
                tmp += glass[j+1]
            tmp_lst[j] = tmp
        glass = tmp_lst

print(sum(glass)%1000000007)