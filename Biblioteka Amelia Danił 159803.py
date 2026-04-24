
ksiazki = [
    {"tytul": "Ostatnie życzenie", "autor": "Andrzej Sapkowski", "sztuki": 3},
    {"tytul": "Instytut", "autor": "Stephen King", "sztuki": 2},
    {"tytul": "Metro 2033", "autor": "Dmitrij Głuchowski", "sztuki": 4},
    {"tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "sztuki": 1},
    {"tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "sztuki": 2}
]

uzytkownicy = [
    {"login": "Amelia", "haslo": "1234", "rola": "czytelnik", "wypozyczenia": []},
    {"login": "Adrianna", "haslo": "abcd", "rola": "czytelnik", "wypozyczenia": []},
    {"login": "Kacper", "haslo": "haslo", "rola": "czytelnik", "wypozyczenia": []}
]

# Logowanie użytkownika
def logowanie():
    liczba_prob = 0

    while liczba_prob < 3:
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")

        for uzytkownik in uzytkownicy:
            if uzytkownik["login"] == login and uzytkownik["haslo"] == haslo:
                print("Zalogowano pomyślnie.\n")
                return uzytkownik

        liczba_prob += 1
        print("Nieprawidłowy login lub hasło.")
        print("Pozostało prób:", 3 - liczba_prob)

    print("Przekroczono limit prób logowania. Program zakończony.")
    return None

# Wyświetlanie katalogu książek
def wyswietl_katalog():
    print("\n--- Katalog książek ---")

    for ksiazka in ksiazki:
        print("Tytuł:", ksiazka["tytul"])
        print("Autor:", ksiazka["autor"])
        print("Dostępne sztuki:", ksiazka["sztuki"])
        print("----------------------")

#Szukanie ksiązki na podstawie tytułu
def znajdz_ksiazke_po_tytule(tytul):
    for ksiazka in ksiazki:
        if ksiazka["tytul"].lower() == tytul.lower():
            return ksiazka

    return None

# Wypożyczanie książek
def wypozycz_ksiazke(uzytkownik):
    print("\n--- Wypożyczenie książki ---")
    tytul = input("Podaj tytuł książki: ")

    ksiazka = znajdz_ksiazke_po_tytule(tytul)

    if ksiazka is None:
        print("Nie znaleziono książki o takim tytule.")
    elif ksiazka["sztuki"] > 0:
        ksiazka["sztuki"] -= 1
        uzytkownik["wypozyczenia"].append(ksiazka["tytul"])
        print("Wypożyczono książkę:", ksiazka["tytul"])
    else:
        print("Brak dostępnych sztuk tej książki.")

# Możliwość sprawdzenia wypożyczonych książek
def pokaz_moje_wypozyczenia(uzytkownik):
    print("\n--- Moje wypożyczenia ---")

    if len(uzytkownik["wypozyczenia"]) == 0:
        print("Nie masz aktualnie wypożyczonych książek.")
    else:
        for numer, tytul in enumerate(uzytkownik["wypozyczenia"], start=1):
            print(numer, "-", tytul)

# Wyświetlanie menu głównego
def wyswietl_menu():
    print("\n--- Menu główne ---")
    print("1. Przeglądaj katalog")
    print("2. Wypożycz książkę")
    print("3. Moje wypożyczenia")
    print("4. Wyloguj")

# Wybieranie funkcji którą chcemy wykonać w menu głównym
def menu_glowne(uzytkownik):
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            wyswietl_katalog()
        elif wybor == "2":
            wypozycz_ksiazke(uzytkownik)
        elif wybor == "3":
            pokaz_moje_wypozyczenia(uzytkownik)
        elif wybor == "4":
            print("Wylogowano. Do widzenia!")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

# Uruchomienie programu
def uruchom_program():
    print("=== System obsługi biblioteki ===")

    zalogowany_uzytkownik = logowanie()

    if zalogowany_uzytkownik is not None:
        menu_glowne(zalogowany_uzytkownik)


uruchom_program()