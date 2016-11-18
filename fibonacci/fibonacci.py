def fibonacci(n):
    acum = 0
    first = 1
    last = 1
    while acum < n:
        acum = first + last
        temp = first
        first = acum
        last = temp
    print acum

fibonacci(13)
