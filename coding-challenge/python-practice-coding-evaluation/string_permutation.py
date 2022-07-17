def ifExists(n, a, b):
    # this id default OUTPUT. You can change it.
    result = -404

    # write your logic here:
    # print("".join(sorted(a)))  # used to sort alphabets. sort() for numbers

    list_of_sorted_characters_in_a = sorted(a)
    list_of_sorted_characters_in_b = sorted(b)

    result = "YES"

    distance = abs(ord(list_of_sorted_characters_in_a[0]) - ord(list_of_sorted_characters_in_b[0]))
    for i in range(1, n):
        if abs(ord(list_of_sorted_characters_in_a[i]) - ord(list_of_sorted_characters_in_b[i])) != distance:
            # ord() gives an ASCII number that particularly represents a character
            # we then get the absolute of that to rid of negative results - abs()
            result = "NO"
            break

    return result

# INPUT [uncomment and modify if required]
T = int(input())
N = []
A = []
B = []

for i in range(T):
    N.append(int(input()))
    A.append(input())  # input() is raw_input() in python2
    B.append(input())

# OUTPUT [uncomment and modify if required]
for i in range(T):
    print(ifExists(N[i], A[i], B[i]))
