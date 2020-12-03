# Wrappers/Decorators
def yoda(func):
    def wrapper(*args, **kwargs):
        return "Yoda loves Python"
    return wrapper 

@yoda
def add(x, y):
    return x+y 

print(add(5, 2))
