def try_finally_return():
    try:
        print("In try block")
        return "Try return"
    finally:
        print("In finally block")
        return "Finally return"

result = try_finally_return()
print(result)
