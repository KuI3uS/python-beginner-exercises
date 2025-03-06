#3.Napisz funkcję factorial(n), która przyjmuje liczbę całkowitą n i zwraca jej silnię (n!).

def factorial(n):
    if n < 0:
        return "Nie można obliczyć silni dla liczby ujemnej"
    elif n == 0 or n == 1:
        return 1
    else:
        wynik = 1
        for i in range(2, n+1):
            wynik *= i
        return wynik

print(factorial(5))