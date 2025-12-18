def sayhi():
    print("running inside function")
    #print("i am saying hi")
    # what is the function returning?
    return "I am saying hi"

myvar = sayhi # we created myvar and put a function
result = myvar() # we ran the function and put the results in variable result
print(result)
print(type(result))