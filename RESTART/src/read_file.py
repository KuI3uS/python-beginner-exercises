# - wczytaj plik

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

# - obsłuż wyjątek (FileNotFoundError)

def calculate_stats(text):
    if not text.split():
        raise ValueError("File is empty")
    lines = text.splitlines()
    words = text.split()
    stats = {
        "lines": len(lines),
        "words": len(words),
        "characters": len(text),
    }
    return stats

# - wypisz statystyki
def main():


    path = input("Enter path to file: ")

    content = read_file(path)
    if content is None:
        return

    try:
        stats = calculate_stats(content)
    except ValueError as e:
        print(e)
        return

    for key, value in stats.items():
        print(f"{key}: {value}")



if __name__ == "__main__":
    main()