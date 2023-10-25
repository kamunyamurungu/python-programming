#list of intergers as input and create new one containing only the even numbers
def my_numbers(numbers): 
    even_numbers = [x for x in numbers if x % 2 == 0]
    return even_numbers

my_list=[8,5,3,6,9,70,8,2]
result=my_numbers(my_list)
print(result)
