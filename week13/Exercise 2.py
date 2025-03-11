def check_all_numbers(func):
    def wrapper(*args, **kwargs):
        
        for arg in args:
            if type(arg) != int and type(arg) != float:
                raise ValueError(f"All arguments must be numbers. Found: {type(arg)}")
        
        
        for key, value in kwargs.items():
            if type(value) != int and type(value) != float:
                raise ValueError(f"All keyword arguments must be numbers. Found: {type(value)}")
        
        return func(*args, **kwargs)
    return wrapper


@check_all_numbers
def multiply(a, b):
    return a * b


print(multiply(3, 4))  



