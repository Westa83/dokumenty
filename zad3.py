"""Oblicz wartość bezwzględną z liczby tzn. spraw,
aby liczba ujemna stała się dodatnią.

Wartość bezwzględna usuwa 'minus' liczbie ujemnej.
Wartość dodatnią i zerową pozostawia bez zmian.

Tzn. liczba:

-5 ma stać się 5.

4 ma zostać 4.

-1 ma stać się 1.

0 ma zostać 0.

1) Pobierz od użytkownika wartość i zapisz ją do zmiennej

2) Jeśli liczba jest ujemna to zmień wartość zmiennej tak, aby była dodatnia.
Wypisz wynik.
"""





liczba = int(input('Podaj liczbę: '))


if (liczba > 0):
    print('Liczba bezwzględna z', liczba, 'to',abs(liczba))
elif (liczba < 0):
    print('Liczba bezwzględna z', liczba, 'to',abs(liczba))
else:
    print('Liczba bezwzględna z', liczba, 'to',0)
