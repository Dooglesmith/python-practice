#function that returns a message with a <name> argument
def greet(name):
    return f"Hello, {name} how are you?"
    #return "Hello, %s how are you today?" % name
    #return "Hello, {name} how are you doing today?".format(name)

#Calling the function
greet("Doogle")

#-------------------------------Using a LAMBDA function--------------------------------------#

#lambda function
#function name = lambda +arguments: instructions
greet = lambda name, surname: f'Hello, {name} {surname} how are you doing today?'

#calls         1arg     2arg
print(greet("Doogle", "Smith"))
print(greet("Lebron", "James"))
print(greet("Michael", "Jordan"))