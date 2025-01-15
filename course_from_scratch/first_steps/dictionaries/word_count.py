# 8. Stwórz program, który prosi użytkonika o wpisanie tekstu w konsoli, a następnie utwórz słownik, w którym kluczami bąda
# słowa występujące w teksie, a wartości liczby wystąpień każdego słowa. wyświetl wartość słowa.

texts = input("Enter a string: ")
words = texts.split(" ")
word_count = {}

for word in words:
    if word_count.get(word) is not None:
        word_count[word] += 1

    else: word_count[word] = 1

for word, words in word_count.items():
    print(f"{word} : {words}")