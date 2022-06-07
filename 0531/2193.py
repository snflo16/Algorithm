N = int(input())

ans = 1
end_one = 1
end_two = 0

for i in range(1, N):
    tmp_one = end_one
    tmp_two = end_two
    end_one = end_two
    end_two = tmp_one + tmp_two
    ans = end_one + end_two

print(ans)