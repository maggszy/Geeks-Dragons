# Treść
Zaprojektuj i zaimplementuj schemat bazy danych dla sklepu „Geeks & Dragons”, mającego w ofercie gry nieelektroniczne, przykładowo planszowe, kolekcjonerskie, karciane, RPG, strategiczne, ekonomiczne itp. Nie jest to jednak zwykły sklep, ponieważ prowadzi wypożyczalnię gier oraz organizuje turnieje (w zeszłym roku odbyły się turnieje przynajmniej pięciu różnych gier).

Baza powinna przynajmniej posiadać informacje o:
- pracownikach,
- asortymencie,
- odbytych turniejach, w tym zawodnikach i wynikach,
- terminarzu nadchodzących spotkań,
- informacjach finansowych,
- wypożyczeniach i sprzedaży.

# Notatki
1. Nasz sklep działa od poniedziału do piątku w godzinach 10-18.
2. Nie działa w święta.
3. Mamy 3 pracowników - każdy na pół etatu, 10-14, 12-16, 14-18.
4. Każdą grę którą mamy na stanie można wypożyczyć (10zl/dzień) lub kupić za cenę wykupu. Trezcia opcja to gra turniejowa.
5. Mamy osobne gry na turnieje, np po 4 sztuki (wtedy możemy zrobic 3 rundy). Nawet możnaby zahardkodować nazwy tych gier

## Jakie kolumny?

### Klienci
- customer ID
- First name
- Last name
- birth date 
- email 
- phone number
- ?sex do generowania?
1. To można wygenerować na początku np. 1000 klientów, z których pozniej bedziemy losowac i przypiywac im zakupy
2. Email składa się z imienia i nazwiska

### Pracownicy
- employee ID
- first name
- last name
- sex?
- email
- phone number
- address ID
- (active)
- date of employment?
- work end date?

1. Ile pracowników
2. Dla każdego ID losujemy płeć + odpowiednie imiona i nazwiska, mail składający sie z imienia i nazwiska, losowy numer, datę zatrudnienia. Address ID moze byc taki sam jak employee ID, bo tylko od pracowników zbieramy takie dane

### Address 
- address ID
- city
- country
- street
- zip code
- number
1. To dla uproszczenia mogą być jakieś wrocławskie dane, może nawet zahardkodowane.

### Gry
- game ID
- game name
- description??
- release year
- min players
- max players
- play time
- min age
- cena
1. Wybieramy losowo X gier z naszego pliku na temat gier i każdemu przypisujemy ID - tylko takie gry bedziemy u siebie mieć.


### Asortyment/Inventor
- item ID
- game ID
- typ(0 - do kupienia, 1 - do wypożyczenia, 2 - turniej )
1. Losujemy z jakiegoś rozkładu ile mamy sztuk której gry.
2. Każdej sztuce przypisujemy item ID

### Terminarz
- date
- turniej ID
1. Turnieje mamy np w pierwsze czwartki miesiąca (jeśli nie ma wtedy święta)
2. Wygenerowałabym najpierw daty turnieju i przypisałabym im ID

### Turnieje
- turniej ID 
- game ID
- max teams/ile rund
- wpisowe
- nagroda
3. Później wylosowała grę/ zahardkodujemy? bo potrzebujemy mieć tyle gier żeby w nią robić turnieje
4. Założyłabym 3 rundy, wtedy 16 mecze są w pierwszej rundzie - > 8 gier 
5. wtedy Maksymalna liczba graczy to 16*4
6. Wpisowe jakieś losowe 
7. Nagroda = wpisowe * liczba graczy / 3 


### Wyniki
- result ID
- turniej ID
- pozycja
- klient ID
1. Losujemy klientów którzy będą brać udział w turnieju (max graczy * ile meczów w pierwszej rundzie)

### Finanse/ pomysły
- payment ID
- in/out (0/1)

### Wypłaty
- payment ID
- pracownik ID
- wartość
- data
- nazwa

###  Koszty/ przepływy
- payment ID
- wartość
- data
- nazwa
- typ 

### Wypożyczenia 
- rental ID
- payment ID
- klient ID
- item ID
- rental date
- return date
- cost: (retun date - rental date ) * cost per day


### Sprzedaż
- sprzedaż ID
- payment ID
- klient ID
- payment value
- item ID
- employee ID
1. losuje wektor dni wypożyczeń
2. losuje wektor item ID
3. losuje wektor customerów





------------------------------------
Pomysły dodatkowe finanse:
- wynajmowanie budynku 
- wypłaty
- kaucje
- dofinansowanie z miasta
- nagrody na turnieje
- wpisowe na turniej
- zakupy rzeczy na turniej
-------------------------------------

### Tabele

- [ ] Pracownicy
- [ ] Address
- [x] Gry
- [ ] Asortyment/Inventor
- [ ] Terminarz
- [ ] Turnieje
- [ ] Wyniki
- [ ] Finanse/ pomysły
- [ ] Wypłaty
- [ ] Koszty/ przepływy
- [ ] Wypożyczenia
- [ ] Sprzedaż


## Linki

1. Gry:
    - gry w różnych językach (https://www.kaggle.com/datasets/andrewmvd/board-games)

2. Osoby :
    - imiona zagraniczne (https://catalog.data.gov/dataset/popular-baby-names/resource/02e8f55e-2157-4cb2-961a-2aabb75cbc8b)
    - nazwiska zagraniczne (https://namecensus.com/last-names/)
    - imiona polskie (https://dane.gov.pl/pl/dataset/219,imiona-nadawane-dzieciom-w-polsce)
    - nazwiska polskie (https://dane.gov.pl/pl/dataset/1681,nazwiska-osob-zyjacych-wystepujace-w-rejestrze-pesel)
