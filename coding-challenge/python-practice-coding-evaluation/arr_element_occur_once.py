# INPUT
sample_input = list(map(str, input().strip().split()))
result = -404

# Your code logic:
element_frequency = {}  # dict

# Overall solution is O(2n) => O(n)

# O(n)
for e in sample_input:
    if e in element_frequency:
        element_frequency[e] = element_frequency[e] + 1
    else:
        element_frequency[e] = 1

# O(n)
for key in element_frequency:
    if element_frequency[key] == 1:
        result = key
        break

# OUTPUT
print(result)