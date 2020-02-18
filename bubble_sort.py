input = [1, 0, 0, 2, 5, 0, 8]
for i in range(0, len(input)-1):
    for j in range(0, len(input)-1-i):
        if input[j] > input[j+1]:
            input[j], input[j+1] = input[j+1], input[j]
print(input)
