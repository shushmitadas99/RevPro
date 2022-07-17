# INPUT
sample_input = list(map(str, input().strip().split()))
result = -404

# Your code logic:
# Sliding window
given_string = sample_input[0]
substring = sample_input[1]

for i in range(len(substring)):
    all_matching = True  # Boolean flag => find counter example
    for j in range(len(substring)):
        if given_string[i + j] != substring[j]:
            all_matching = False  # used in coding interviews

        if all_matching:
            result = i
            break

result = given_string.find(substring)

# OUTPUT
print(result)
