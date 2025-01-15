phone_book = {
    'Jakub': 500300400,
    'Mariusz': 424556778,
    'Michał': 455677888
}

print(phone_book.get("Jakub"))

for name, phone_number  in phone_book.items():
    print(name + ":" + str(phone_number))