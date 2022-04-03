N = int(input())

if N == 1:
    print(int(input()))
else:
    stairs = [0]+ [int(input()) for _ in range(N)]
    scores = [[] for _ in range(N+10)]

    scores[1].append([stairs[1], 1])
    scores[2].append([stairs[2], 1])
    scores[2].append([stairs[1]+stairs[2], 2])

    def make(now):
        
        tmp = []
        for i in range(len(scores[now-2])):
            tmp.append(scores[now-2][i][0])
        scores[now].append([max(tmp)+stairs[now], 1])

        tmp = []
        for i in range(len(scores[now-1])):
            if (scores[now-1][i][1] < 2):
                tmp.append(scores[now-1][i][0])
        scores[now].append([max(tmp)+stairs[now], 2])

    for i in range(3, N+1):
        make(i)

    tmp = []
    for num, cnt in scores[N]:
        tmp.append(num)

    print(max(tmp))