N = int(input())

answer = 1
weights = (3, 5)

while N not in weights:
    new_weights = set()
    stop = True
    for weight in weights:
        new_weights.add(weight+3)
        new_weights.add(weight+5)
        if weight+3 <= N:
            stop = False
    if stop:
        answer = -1
        break
    answer += 1
    weights = new_weights
    print(weights)
print(answer)
