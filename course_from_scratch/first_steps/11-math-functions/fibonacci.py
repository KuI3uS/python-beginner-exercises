# 7.Napisz funkcję fibonacci(n), która przyjmuje liczbę całkowitą n i zwraca n-tą liczbę w ciągu Fibonacciego.

def fibonacci(n):
    if n < 0:
        raise ValueError("n is negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, 1 + n):
        a, b = b, a + b
    return b

print(fibonacci(12))