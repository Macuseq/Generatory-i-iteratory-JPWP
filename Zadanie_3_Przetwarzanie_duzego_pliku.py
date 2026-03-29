#Zadanie 3 - Przetwarzanie dużego pliku

#Zaimplementuj generator, który:

#czyta plik linia po linii,
#zwraca każdą linię przez yield.
#wypisz 3 pierwsze linie

def read_large_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:


file_name = "duzy_plik.txt"