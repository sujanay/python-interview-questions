""" Implement the concept of decorators"""
def decorator_function(original_func):
    def wrapper_function():
        return original_func()
    return wrapper_function

@decorator_function
def display():
    print("This is from display!")

# my_func = decorator_function(display)
# my_func()

display()