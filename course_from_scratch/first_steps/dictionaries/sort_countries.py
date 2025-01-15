# 7. Posortuj słownik z poprzedniego ćwiczenia w kolejnosci alfabetycznej

countries_capitals = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Francja": "Paryż",
    "Włochy": "Rzym",
    "Hiszpania": "Madryt"
}

countries_and_capitals = dict(sorted(countries_capitals.items()))
print(countries_and_capitals)