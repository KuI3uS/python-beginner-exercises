# 15.Napisz funkcję, która przyjmuje listę imion i wypisuje je w odwrotnej kolejności, używając pętli.


def reverse_numes(names):
    for name in list(names[::-1]):
        print(name)


imiona = ["Jakub", "Marta", "Daria", "Marcin"]

reverse_numes(imiona)
