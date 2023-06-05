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

## Jakie kolumny?

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

### Address 
- address ID
- city
- country
- street
- zip code
- number

### Asortyment/Inventor
- item ID
- game ID
- buy-back price?? (cena wykupienia)

### Gry
- game ID
- game name
- description??
- release year
- min players
- max players
- play time
- min age

### Turnieje
- turniej ID 
- game ID
- max teams/ile rund
- wpisowe
- nagroda

### Terminarz
- date
- turniej ID

### Wyniki
- mecz ID
- turniej ID
- drużyna A ID
- drużyna B ID
- runda 
- wynik rundy

### Gracze
- gracz ID
- gracz name
- klient ID
- team ID

### Teams
- team ID
- team name


### Finanse/ pomysły
- payment ID
- in/out (0/1)
- typ płatności (wypłada, stałe, turnieje, inne)


### Wypłaty
- payment ID
- pracownik ID
- wartość
- data
- nazwa

###  Koszty stałe
- payment ID
- wartość
- data
- nazwa

### Turnieje koszty
- payment ID
- wartość
- data
- nazwa

### Inne koszty
- payment ID
- wartość
- data
- nazwa

### Wypożyczenia 
- payment ID
- rental ID
- item ID
- rental date
- return date
- cost (stała cena za dzień wypożyczenia)


### Sprzedaż
- payment ID
- payment value
- item ID
- customer ID
- employee ID

### Klienci
- customer ID
- First name
- Last name
- birth date 
- email 
- phone number
- sex?


------------------------------------
- wynajmowanie budynku 
- wypłaty
- kaucje
- dofinansowanie z miasta
- nagrody na turnieje
- wpisowe na turniej
- zakupy rzeczy na turniej
-------------------------------------



## Linki

1. Gry:
    - gry w różnych językach (https://www.kaggle.com/datasets/andrewmvd/board-games)

2. Osoby :
    - imiona zagraniczne (https://catalog.data.gov/dataset/popular-baby-names/resource/02e8f55e-2157-4cb2-961a-2aabb75cbc8b)
    - nazwiska zagraniczne (https://namecensus.com/last-names/)
    - imiona polskie (https://dane.gov.pl/pl/dataset/219,imiona-nadawane-dzieciom-w-polsce)
    - nazwiska polskie (https://dane.gov.pl/pl/dataset/1681,nazwiska-osob-zyjacych-wystepujace-w-rejestrze-pesel)
