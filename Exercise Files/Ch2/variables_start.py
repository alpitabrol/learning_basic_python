
# # Example file for variables


# Declare a variable and initialize it
 #f=0
# print(f)

# # re-declaring the variable works
# f="abc"
# print(f)
# # ERROR: variables of different types cannot be combined
# print("this is string "+str(132))

# # Global vs. local variables in functions
f=0
def somefunction():
    global f
    f="def"
    print(f)

somefunction()
print(f)

del f
print(f)
