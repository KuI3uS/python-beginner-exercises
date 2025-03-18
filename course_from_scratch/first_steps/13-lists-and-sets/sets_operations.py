# 12.Napisz funkcję, która przyjmuje dwa zbiory i zwraca ich sumę, różnicę i część wspólną.

def operacje_na_zbiorach(set1, set2):
    suma = set1.union(set2)
    roznica = set1.difference(set2)
    czesc_wspolna = set1.intersection(set2)
    return suma,roznica,czesc_wspolna


name = {"Jakub", "Marcinkowski", "Marta", "Bajor", "Marcelina"}
name2 = {"Jakub", "Marcinkowski", "Marta", "Bajor"}

suma, roznica, czesc_wspolna = operacje_na_zbiorach(name, name2)

print('suma', suma)
print('roznica', roznica)
print('czesc_wspolna', czesc_wspolna)
