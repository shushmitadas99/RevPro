# Return True if input string has only unique characters
# Return False if input string has any occurance of duplicate characters

# Time complexities
def addition(a, b):
    return a + b  # O(1)


# find sum of all elements in a list
# def sum_list(my_list_of_numbers
def sum_list(my_list_of_numbers):
    my_sum = 0

    for e in my_list_of_numbers:
        my_sum += e
    return my_sum


# nested for loops account for O(n^2) time complexity
# however if you have a constant 10 for the nested for loop, it would be O(n)
# because it is n(10)
def bruteForce_noDuplicateCharacters(my_string):
    for i in range(len(my_string) - 1):
        for j in range(i + 1, len(my_string)):
            if my_string[i] == my_string[j]:
                return False

    return True

#O(n)
def set_noDuplicateCharacters(my_string):
    my_set = set() # O(1)

    # O(n)
    for char in my_string:
        my_set.add(char)  # If you try to add a value that already exists in the set, it will not add it a second time

        # Compare to see if the set has the same number of characters as the string
        # If they do, then it means that all characters in the string are unique
        # If they don't then it means that we have duplicates
    return len(my_set) == len(my_string)

def sorting_noDuplicateCharacters(my_string):
    # O(n log n) <- The best "general" sorting algorithms can ONLY achieve O(n log n)
    my_list_of_sorted_characters = sorted(my_string)

    # O(n)
    for i in range(len(my_list_of_sorted_characters) - 1):
        if my_list_of_sorted_characters[i] == my_list_of_sorted_characters[i + 1]:
            return False

    # O(1)
    return True



# Input: abc
# Expected Output: True
print(bruteForce_noDuplicateCharacters("abc"))

# Input: apple
# Expected Output: False
print(bruteForce_noDuplicateCharacters("apple"))

print()

# Input: abc
# Expected Output: True
print(set_noDuplicateCharacters("abc"))

# Input: apple
# Expected Output: False
print(set_noDuplicateCharacters("apple"))

print()

# Input: abc
# Expected Output: True
print(sorting_noDuplicateCharacters("abc"))

# Input: apple
# Expected Output: False
print(sorting_noDuplicateCharacters("apple"))