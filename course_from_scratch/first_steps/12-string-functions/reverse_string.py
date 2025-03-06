# 4.Napisz funkcję reverse_string(s), która przyjmuje tekst i zwraca go w odwrotnej kolejności. Nie korzystaj z funkcji reversed().

def reverse(s):
    return s[::-1]

print(reverse("hello"))