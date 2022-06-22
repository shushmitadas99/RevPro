def do_math(num1, num2, *args, **kwargs):
    # python allows us to define function within a function, unlike java
    # addition() and multiplication() are examples of helper functions.
    # helper functions exist within a function to reduce code redundancy
    def addition():
        my_sum = 0
        my_sum += num1  # adding positional arguments before moving onto args and kwargs
        my_sum += num2
        for element in args:
            my_sum += element

        return my_sum

    def multiplication():
        my_product = 1
        my_product *= num1
        my_product *= num2
        for element in args:
            my_product *= element

        return my_product

    # main logic
    if 'operation' in kwargs:
        if kwargs['operation'] == 'add':
            return addition()
        elif kwargs['operation'] == 'multiply':
            return multiplication()
    else:
        return addition()  # we have to return addition() because we
    # are inside do_math() function


print(do_math(10, 20))  # at least 2 arguments required to run the program (positional args)
print(do_math(10, 20, 30))  # variable argument - you can enter any number of args
print(do_math(10, 20, 2, 5, operation="add"))
print(do_math(10, 20, 2, 5, operation="multiply"))  # keyword argument - you specify a keyword for
# performing specific operations

