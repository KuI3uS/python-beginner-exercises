#Stwórz liste, która bedzie zwracac 10 słów.
# Następnie stwórz drugą listę, która będzie zwracac tylko te słowa, które mają więcej niż 5 liter.
lists = ['bird', 'cat', 'dog', 'elephant', 'cheetah', 'jaguar', 'crocodile', 'lizard']

lists.extend(["python", "code", "developer", "algorithm", "function", "list", "variable", "integer", "debug", "compile"])

for words in lists:
    if len(words) > 5:
        print(words)