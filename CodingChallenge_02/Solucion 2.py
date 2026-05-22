def fibonacci(n):
    previous = 1
    one_before_previous = 1
    if n < 2:
        return n
    print(0)
    print(1)
    print(1)
    for n in range(2, n-1):
        actual = previous + one_before_previous
        print(actual)
        one_before_previous = previous
        previous = actual


fibonacci(11)
