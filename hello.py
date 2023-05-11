#Write a function that takes an unknown number of arguments and returns their sum.
def sum_of_unknown(*args):
    return sum(args)
answer = sum_of_unknown(4,8,9,5,7,3)
print(answer)


#Write a function that takes two arguments, the first being a string and the second being an
#  unknown number of integers. The function should return a new string where the integers
#  have been added to the original string.
# def add_my_string(strings, *args):
    # string1 = strings
    # for number in args:
    #     string1 += str(number)
    #     return string1
    
    # answer = add_my_string(100,200,300)
    # print(answer) 

#Write a function that takes an unknown number of keyword arguments and returns a dictionary where the keys are the argument names and the values are the argument values.
def my_detail(**kwargs):
    return{key: value for key,value in kwargs.items()}
anser = my_detail(name='Emmily',age=20,location='Karen')
print(anser)

#Write a function that takes a function and an unknown number of arguments, and returns the result of calling the function with the arguments.
def function_args(function, *args):
    return function(*args)
def sum_of_numbers(*args):
    return sum(args)
ans =function_args(sum_of_numbers,9,8,7,6,5)
print(ans)


#Write a function that takes a list of integers and an unknown number of keyword arguments. The function should return a new list where each integer in the original list has been multiplied by the value of the corresponding keyword argument.
def list_of_argmunts(num_list, **kwargs):
    new_list = []
    for i in new_list:
        ans = i
        for key, value in kwargs.items():
            ans *= value
            new_list.append(ans)
            return new_list
# list_of_argmunts([1,2,3],e=2,d=3,f=4)[8,24,72]   
#Write a function that takes a list of integers and an unknown number of additional integers as arguments. The function should return the index of the first occurrence of the sum of the list and the additional integers
def sum_index(list, *args):
    total_sum = (list) + sum(args)
    sum = 0
    for i, num in enumerate(list):
        sum += num
        if sum == total_sum:
            return i
    return -1
    