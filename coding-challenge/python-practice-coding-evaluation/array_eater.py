def maxPoss(N, K, P, A):

    # this is default OUTPUT. You can change it.
    result = -404
    # write your logic here:
    A.sort()  # At this point, A is sorted from least to greatest

    saved_elements = []  # saving P elements and add them to empty list
    for _ in range(P):  # don't change range to xrange here
        saved_elements.append(A.pop())  # pop off the rightmost (greatest) element

    # Array eater will not eat K elements
    for _ in range(K):  # don't change range to xrange here
        A.pop()

    result = sum(A) + sum(saved_elements)

    return result


# INPUT [uncomment and modify if required]
temp1 = input().split()  # input() is raw_input() in python2
N = int(temp1[0])
K = int(temp1[1])
P = int(temp1[2])
A = []

temp = input().split()

for i in range(N):  # range is xrange() in python2
    A.append(int(temp[i]))

# OUTPUT [uncomment and modify if required]
print(maxPoss(N, K, P, A))
