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
- game name
- date

### Terminarz
- date
- game name
- how many teams

### Finanse/ pomysły
- wynajmowaniw budynku 
- wypłaty
- kaucje
- dofinansowanie z miasta
- nagrody na turnieje
- wpisowe na turniej
- zakupy rzeczy na turniej


### Wypożyczenia 
- rental ID
- item ID
- rental date
- return date
- cost ( stała cena za dzień wypożyczenia)
- payment ID

### Sprzedaż
- sale ID
- item ID
- customer ID
- employee ID
- payment ID

### Payments
- payment ID
- payment value
- customer ID
- employee ID

### Klienci???
- First name
- Last name
- birth year 
- address
- email
- phone number
- sex?



## Linki

1. Gry:
    - gry w różnych językach (https://www.kaggle.com/datasets/andrewmvd/board-games)

2. Osoby :
    - imiona zagraniczne (https://catalog.data.gov/dataset/popular-baby-names/resource/02e8f55e-2157-4cb2-961a-2aabb75cbc8b)
    - nazwiska zagraniczne (https://namecensus.com/last-names/)
    - imiona polskie (https://dane.gov.pl/pl/dataset/219,imiona-nadawane-dzieciom-w-polsce)
    - nazwiska polskie (https://dane.gov.pl/pl/dataset/1681,nazwiska-osob-zyjacych-wystepujace-w-rejestrze-pesel)
