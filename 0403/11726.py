N = int(input())
answer = 0

def count(two_num):
    one_num = N - two_num*2
    ans = 1
    tmp = one_num + two_num
    # print(tmp, one_num, two_num)
    while tmp > max(one_num, two_num):
        ans *= tmp
        tmp -= 1
    for i in range(1, min(one_num, two_num)+1):
        ans //= i
    return int(ans)

for i in range(0, N//2+1):
    answer += count(i)

print(answer%10007)