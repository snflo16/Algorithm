N = int(input())

answer = -1
numbers = [[], [N]]

if N == 1:
    answer = 0
else:
    def make_num(n):

        global answer

        tmp = set()
        for k in numbers[n-1]:
            if k%3 == 0:
                tmp.add(k//3)
            if k%2 == 0:
                tmp.add(k//2)
            tmp.add(k-1)
        if 1 in tmp:
            answer = n-1
            return
        else:
            numbers.append(list(tmp))
            make_num(n+1)

    make_num(2)

print(answer)