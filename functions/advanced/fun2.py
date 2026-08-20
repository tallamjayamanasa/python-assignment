def outer():
    def inner():
        return "hello world"

    return inner 
result=outer()
print(result())