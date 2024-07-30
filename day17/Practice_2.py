def print_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
print_args_kwargs(1, 2, 3, a=4, b=5)  
