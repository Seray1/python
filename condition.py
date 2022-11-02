# if statements in python starts with if then a boolean statement ending with a colon then the next line of cone is 
# indented

# n = input("Number: ")

# if n > 0 :
#     print("n is positive")
# elif n < 0:
#     print("n is negative")
# else:
#     print("n is not positive")

# the above line of code will not work because inputs will always return a string,and a str cannot be greater
#than another string, therefore we have to convert it to an interger usinng a function int()

n = int(input("Number: "))

if n > 0 :
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is not positive")
