import pandas as pd
import numpy as np

# Wczytanie danych z pliku CSV do ramki danych (database)
database = pd.read_csv('data.csv')

# Funkcja do obliczania entropii dla danej kolumny
def oblicz_entropie(kolumna):
    """
    Oblicza entropię na podstawie serii pandas, listy lub tablicy numpy.
    """
    prawdopodobienstwa = kolumna.value_counts(normalize=True)
    entropia = -(prawdopodobienstwa * np.log2(prawdopodobienstwa)).sum()
    return entropia

# Funkcja do obliczania zysku informacji dla podziału danej kolumny
def oblicz_zysk_informacji(dane, kolumna_podzialu, kolumna_docelowa):
    """
    Oblicza zysk informacji na podstawie zbioru danych, nazwy kolumny do podziału i nazwy kolumny docelowej.
    """
    poczatkowa_entropia = oblicz_entropie(dane[kolumna_docelowa])

    podzbiory = dane.groupby(kolumna_podzialu)
    entropie_podzbiorow = podzbiory.apply(lambda x: oblicz_entropie(x[kolumna_docelowa]))
    wagi_podzbiorow = podzbiory.size() / len(dane)
    entropia_suma = (entropie_podzbiorow * wagi_podzbiorow).sum()

    return poczatkowa_entropia - entropia_suma

# Lista nazw kolumn
kolumny = ['a1', 'a2', 'a3']

# Funkcja do znalezienia kolumny o największym zysku informacji
def najwyzszy_zysk_informacji(kolumny):
    # Utworzenie słownika zysków informacji za pomocą listy składanej
    zyski_informacji = {kol: oblicz_zysk_informacji(database, kol, kol) for kol in kolumny}
    # Zwrócenie klucza o najwyższej wartości
    return max(zyski_informacji, key=zyski_informacji.get)

# Wywołanie funkcji i wydrukowanie kolumny o najwyższym zysku informacji
print(najwyzszy_zysk_informacji(kolumny))
