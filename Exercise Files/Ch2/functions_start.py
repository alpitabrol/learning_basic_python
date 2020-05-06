#
# Example file for working with functions
#

# define a basic function
def funct1(): 
    print("this funct1")

# function that takes arguments
def func2(arg1,arg2):
    print(arg1," ",arg2)

# function that returns a value
def cude(x):
    return x*x*x


# function with default value for an argument
def power(num,x=1):
    result=1
    for i in range(x):
        result = result*num
    return result

#function with variable number of arguments
def mult(*arg):
    result =0
    for x in arg:
        result = result +x
    return result



# funct1()
# print(funct1())
# print(funct1)
# func2(10,20)
# print(func2(100,20))
# print(cude(3))

# print(power(2))
# print(power(2,3))
# print(power(x=2,num=3))

print(mult(10,5,5,10,4))