def log_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Ejemplo de uso
@log_params_and_return
def add(a, b):
    return a + b

add(3, 4)
