# Write a function that takes an unknown number of arguments and returns their sum.
def sum_of_unknown(*args):
    return sum(args)


answer = sum_of_unknown(4, 8, 9, 5, 7, 3)
print(answer)


# Write a function that takes two arguments, the first being a string and the second being an
#  unknown number of integers. The function should return a new string where the integers
#  have been added to the original string.
def add_my_string(strings, *numbers):
    result = strings
    for number in numbers:
        result += str(numbers)
        return result


print(add_my_string("Hello", 10, 20, 30))

# Write a function that takes an unknown number of keyword arguments and returns a dictionary
#  where the keys are the argument names and the values are the argument values.


def my_detail(**kwargs):
    return {key: value for key, value in kwargs.items()}


anser = my_detail(name='Emmily', age=20, location='Karen')
print(anser)

# Write a function that takes a function and an unknown number of arguments,
#  and returns the result of calling the function with the arguments.


def function_args(function, *args):
    return function(*args)


def sum_of_numbers(*args):
    return sum(args)


ans = function_args(sum_of_numbers, 9, 8, 7, 6, 5)
print(ans)


# Write a function that takes a list of integers and an unknown number of keyword arguments.
# The function should return a new list where each integer in the original list has been multiplied by
# the value of the corresponding keyword argument.
def list_of_arguments(int_list, **kwargs):
    new_list = []
    for i in int_list:
        result = i
        for key, value in kwargs.items():
            result *= value
        new_list.append(result)
    return new_list


result_list = list_of_arguments([2, 4, 7], a=2, b=3, c=4)
print(result_list)


# list_of_argmunts([1,2,3],e=2,d=3,f=4)[8,24,72]
# Write a function that takes a list of integers and an unknown number of additional integers as arguments.
# The function should return the index of the first occurrence of the sum of the list and the additional integers
def sum_index(list, *args):
    result = sum(list + sum(args))
    try:
        index = list.index(result)
        return index
    except ValueError:
        return -1
    list=[9,8,7,6,5]
    total = sum_index(list,2,3,4)
    print(total) 
    


# Write a function that takes an unknown number of keyword arguments, each with a string value.
# The function should concatenate all the strings and return the resulting string.
def concatenate_string(**kwargs):
    empty = ""
    for keys, value in kwargs.items():
        empty += value
        return empty
    empty = concatenate_string(
        one="Emmily", two="Stephanie", three="Software Developer")
    print(empty)
