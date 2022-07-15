lookup = dict()

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in lookup:
        return lookup[n]
    else:
        memo = fibonacci(n-1) + fibonacci(n-2)
        lookup[n] = memo
        return memo

# Test cases:
print(fibonacci(0)) # 0
print(fibonacci(1)) # 1
print(fibonacci(2)) # 1 
print(fibonacci(8)) # 21
print(fibonacci(17)) # 1597
print(fibonacci(58)) # 591286729879