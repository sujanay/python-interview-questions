""" Programming illustrations on first class functions """
# def decorator_function(msg):
#     message = msg
#     def wrapper_function():
#         print("Inside wrapper function", message)
#     return wrapper_function
#
# func = decorator_function('hello')
# func()

def html_tag(tag):
    def wrap_text(msg):
        print("<{0}> {1} <{0}>".format(tag, msg))
    return wrap_text

print_hi = html_tag('script')
print_hi("This is my message")
print_hi("This is second message")