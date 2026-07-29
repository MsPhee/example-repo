#define a function which takes two arguments.
#a list of integers and a single integer that represents an index point
# the single integer will represent the index point up to which the function should sum 
# all the numbers in the list 
# the function is required to sum of all the numbers in the list up to the index point
#calculate using recursion instead of a loop

integer_list = [2, 2, 3, 4, 5, 6, 7]
single_integer = 5

def sum_up_to_n(numbers, n):
    if n == 0:
        return numbers[0] #This is the base case, if n is 0, return the first element of the list
    return numbers[n] + sum_up_to_n(numbers, n - 1)

result = sum_up_to_n(integer_list, single_integer)
print(result)



