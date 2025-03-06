# 5.Napisz funkcję is_palindrome(s), która przyjmuje tekst i zwraca True jeśli jest palindromem i False jeśli tekst nie jest palindromem.

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("abab"))
print(is_palindrome("kajak"))