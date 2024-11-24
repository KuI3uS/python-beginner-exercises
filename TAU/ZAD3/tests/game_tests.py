import unittest
from unittest.mock import patch
from io import StringIO
from TAU.ZAD3.src.game import generuj_plansze, rows, cols, wyswietl_plansze, wykonaj_ruch, ilosc_przeszkod


class TestGame(unittest.TestCase):

    def test_board_size(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        self.assertEqual(len(plansza), rows)
        self.assertEqual(len(plansza[0]), cols)

    def test_start_on_edge(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        self.assertTrue(start[0] in [0, rows - 1] or start[1] in [0, cols - 1])

    def test_end_on_edge(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        self.assertTrue(stop[0] in [0, rows - 1] or stop[1] in [0, cols - 1])

    def test_obstacle_count(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        actual_obstacles = sum(row.count('X') for row in plansza)
        self.assertEqual(actual_obstacles, ilosc_przeszkod)

    def test_display_board(self):
        plansza, start, stop = generuj_plansze(rows, cols)
        aktualna_pozycja = start
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            wyswietl_plansze(plansza, aktualna_pozycja)
            output = mock_stdout.getvalue().strip()
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)

    def test_movement_valid(self):
        plansza, start, _ = generuj_plansze(rows, cols)
        plansza[start[0]][start[1]] = '-'
        if start[0] > 0 and plansza[start[0] - 1][start[1]] != 'X':
            new_pos = wykonaj_ruch(plansza, start, 'W')
            self.assertEqual(new_pos, (start[0] - 1, start[1]))

    def test_movement_invalid(self):
        plansza, start, _ = generuj_plansze(rows, cols)
        current_pos = wykonaj_ruch(plansza, start, 'Z')
        self.assertEqual(current_pos, start)

    def test_blocked_movement(self):
        plansza, start, _ = generuj_plansze(rows, cols)
        plansza[start[0]][start[1]] = '-'
        plansza[start[0] - 1][start[1]] = 'X'
        new_pos = wykonaj_ruch(plansza, start, 'W')
        self.assertEqual(new_pos, start)