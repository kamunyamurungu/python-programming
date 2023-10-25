def numbers(array):
 total=0
 for x in array:
  total+=x
 return total

num=(5,6,8,9,15)
result=numbers(num)
print (f"sum:{result}")
