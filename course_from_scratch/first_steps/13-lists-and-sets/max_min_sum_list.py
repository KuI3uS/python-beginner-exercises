# 14.Napisz funkcję, która przyjmuje listę liczb i zwraca: największą liczbę, najmniejszą liczbę oraz sumę liczb.

def max_min_sum(lista):
    return max(lista), min(lista), sum(lista)

liczby = {1,2,3,4,5,6,7,44,66,7,788,884}


result = max_min_sum(liczby)

print('the largest number', result[0])
print('smallest number', result[1])
print('sum of all numbers', result[2])

