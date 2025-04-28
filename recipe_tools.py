#Uses recursion and decorators
def logger(func):
    def wrapper(*args):
        print(f"Running {func.__name__} with {args}")
        result = func(*args)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@logger
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

@logger
def count_steps(steps):
    if not steps:
        return 0
    return 1 + count_steps(steps[1:])

print("Factorial of 5:", factorial(5))
print("Steps:", count_steps(["mix", "bake", "serve"]))
