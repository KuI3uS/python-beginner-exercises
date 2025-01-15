# stwórz listę, która wypełnisz dziesięcioma liczbami całkowitymi. znajdz najmniejsza i jakwieksząą liczbe.

numbers = [42, 17, 89, 3, 56, 78, 23, 90, 11, 6,22]

min_number = numbers[0]
max_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

print(min_number)
print(max_number)