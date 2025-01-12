names = {'Jakub', 'Janusz', 'Dominik'}
name2 = {'Jakub', 'Janusz', 'Joanna', 'Martyna'}
names.add('Piotr')
names.update({'Kamil','Marta'})

# print(names)

print(names | name2)

# część wspólna
print(names & name2)
print(names.intersection(name2))

# Symetryczna różnica
print(names.difference(name2))
print(names - name2)

print(names.symmetric_difference(name2))
print(names ^ name2)