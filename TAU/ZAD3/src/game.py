import random

rows = 5
cols = 5
ilosc_przeszkod = random.randint(5, rows * cols // 4)

def generuj_plansze(rows, cols):
    plansza = [['-' for _ in range(cols)] for _ in range(rows)]

    start_row, start_col = random.choice([(0, random.randint(0, cols - 1)), (rows - 1, random.randint(0, cols - 1))])
    start = (start_row, start_col)

    stop_row, stop_col = random.choice([(0, random.randint(0, cols - 1)), (rows - 1, random.randint(0, cols - 1))])
    while (stop_row, stop_col) == start:
        stop_row, stop_col = random.choice([(0, random.randint(0, cols - 1)), (rows - 1, random.randint(0, cols - 1))])
    stop = (stop_row, stop_col)

    # Ustawianie na planszy punktów start i stop
    plansza[start[0]][start[1]] = 'S'
    plansza[stop[0]][stop[1]] = 'E'

    # Generowanie przeszkód
    for _ in range(ilosc_przeszkod):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while plansza[row][col] in ['S', 'E', 'X']:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        plansza[row][col] = 'X'

    return plansza, start, stop

def wyswietl_plansze(plansza, aktualna_pozycja):
    for i, row in enumerate(plansza):
        for j, cell in enumerate(row):
            if (i, j) == aktualna_pozycja:
                print('@', end=' ')
            else:
                print(cell, end=' ')
        print()

def wykonaj_ruch(plansza, aktualna_pozycja, ruch):
    nowe_pozycja = list(aktualna_pozycja)

    kierunki = {
        'W': (-1, 0),
        'S': (1, 0),
        'A': (0, -1),
        'D': (0, 1)
    }

    if ruch in kierunki:
        delta_row, delta_col = kierunki[ruch]
        nowe_pozycja[0] += delta_row
        nowe_pozycja[1] += delta_col

        if 0 <= nowe_pozycja[0] < len(plansza) and 0 <= nowe_pozycja[1] < len(plansza[0]):
            if plansza[nowe_pozycja[0]][nowe_pozycja[1]] != 'X':
                return tuple(nowe_pozycja)

    print("Nieprawidłowy ruch! Spróbuj ponownie.")
    return aktualna_pozycja

def poruszanie(plansza, start, stop):
    aktualna_pozycja = start

    while aktualna_pozycja != stop:
        wyswietl_plansze(plansza, aktualna_pozycja)
        ruch = input("Podaj kierunek (W, A, S, D): ").upper()
        aktualna_pozycja = wykonaj_ruch(plansza, aktualna_pozycja, ruch)

    print("Gratulacje! Dotarłeś do celu!")

def start_game(rows, cols):
    plansza, start, stop = generuj_plansze(rows, cols)
    print("Gra rozpoczęta! S - Start, E - Meta, X - Przeszkoda")
    poruszanie(plansza, start, stop)

if __name__ == "__main__":
    start_game(rows, cols)