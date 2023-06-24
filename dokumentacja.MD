
## Schemat bazy danych i zależności funkcyjne w tabelach

Klucze główne zaznaczamy przez pogrubienie 

1. Tabela Customers: R(**customer_id**, first_name, last_name, birth_date, email, phone)
 

    - customer_id : numer  identyfikacyjny klienta
    - first_name: imię klienta
    - last_name: nazwisko klienta
    - birth_date: data urodzenia klienta
    - email: email klienta
    - phone: numer telefonu klienta

    $$\Sigma = \left\{ \text{customer\_id} \to \text{first\_name}, \text{customer\_id} \to  \text{last\_name}, \text{customer\_id} \to \text{birth\_name},\text{customer\_id} \to \text{email}, \text{email} \to \text{customer\_id},\text{customer\_id} \to \text{phone}, \text{phone} \to \text{customer\_id}   \right\} $$

    Customer_id mówi nam jednoznacznie wszystko o danym kliencie, więc znamy jego imię, nazwisko, datę urodzin, email oraz numer telefonu. Email tak jak numer telefonu wyznacza na też jednoznacznie klienta więc pozwalają nam określić pozostałe. Zakładamy unikatowość email, numeru telefonu oraz customer_id. Połączenie reszty informacji o kliencie nie musi nam mówić jednoznacznie jaki to klient.




 




2. Tabela Employees: R(**employee_id**, first_name, last_name,start_work_date,end_work_date, email, phone, address_id)
    - employee_id: numer identyfikacyjny pracownika
    - first_name: imię pracownika
    - last_name: nazwisko pracownika
    - start_work_date: data zatrudnienia (rozpoczęcie pracy)
    - end_work_date: data zakończenia pracy (data końca umowy)
    - email: adres email pracownika
    - phone: numer telefonu pracownika
    - address_id (klucz obcy odwołujący się do tabeli Addresses): numer identyfikacyjny adresu.

    $$\Sigma = \left\{ \text{employee\_id} \to \text{first\_name}, \text{employee\_id} \to  \text{last\_name}, \text{employee\_id} \to \text{start\_work\_date}, \text{employee\_id} \to \text{start\_work\_date},\text{employee\_id} \to \text{email}, \text{email} \to \text{employee\_id}, \text{employee\_id} \to \text{phone}, \text{phone} \to \text{employee\_id} , \text{employee\_id} \to \text{address\_id}    \right\} $$  

    employee_id jednoznacznie definiuje pracownika więc pozwala określić jego imię, nazwisko, date zatrudnienia, datę końca pracy, jego adres email, telefon oraz address_id. Te same informację możemy uzyskać za pomocą jego adresu email jak i numeru telefonu, identycznie jak w przypadku tabeli Customers.




3. Tabela Addresses: R(**address_id**, country, city, street,number,postal_code)

    - adress_id: numer identyfikacyjny adresu.
    - country: państwo
    - city: miasto
    - street: ulica
    - number: numer mieszkania/lokalu
    - postal_code: kod pocztowy.

    $$\Sigma = \left\{\text{adress\_id} \to \text{country}, \text{adress\_id} \to \text{city},\text{adress\_id} \to \text{street},\text{adress\_id} \to \text{number}\text{adress\_id} \to \text{postal\_code}, \text{country} + \text{city} +\text{street} +\text{number} + \text{postal\_code} \to \text{adress\_id} \right\}$$

    Adres jest dokładnie, jednoznacznie wyznaczony dla danego adress_id. Pozostałe pola tylko razem wskażą nam dokładny adres. 
    


4. Tabela Games: R(**game_id**,title, description, release_year,min_players,max_players,play_time,min_age,price)
    
    - game_id: numer identyfikacyjny gry
    - title: oryginalny tytuł gry
    - description: opis gry
    - release_year: rok wydania gry
    - min_players: minimalna liczba graczy
    - max_players: maksymalna liczba graczy
    - play_time: szacowany czas gry
    - min_age: wiek minimalny do zagrania w grę
    - price: cena za kupno gry

    $$\Sigma = \left\{ \text{game\_id} \to \text{release\_year},\text{game\_id} \to \text{min\_players},\text{game\_id} \to \text{max\_players},\text{game\_id} \to \text{play\_time}, \text{game\_id} \to \text{min\_age}, \text{game\_id} \to \text{price}, \text{game\_id} \to \text{title},\text{game\_id} \to \text{description},\text{title} + \text{description} \to \text{game\_id} \right\}$$

    Game_id, tak jak połączenie tytułu i opisu określa nam jednoznacznie grę.


5. Tabela Inventory: R(**inventory_id**, game_id,type)

    - inventory_id: numer identyfikacyjny inwentarza
    - game_id (klucz obcy odwołujący się do tabeli Games): numer identyfikacyjny grę
    - type: przeznaczenie gry na magazynie ( czy na sprzedaż, czy na wypożyczenie, czy na turniej)

    $$ \Sigma = \left\{ \text{inventory\_id} \to \text{game\_id} , \text{inventory\_id} \to \text{type} \right\} $$

    Inventory id wyznacza nam jednoznacznie jaka to gra i jakie jest jej przeznaczenie. game_id mówi nam co to za gra, type mówi jakie jest przeznaczenie te gry. Możemy mieć kilka tych samych gier z tym samym lub inny przeznaczeniem, dlatego z game_id i typu nie wynika inventory_id.


6. Tabela Tournaments: R(**tournament_id**, game_id,max_players,entry_fee,reward )

    - tournament_id: numer identyfikacyjny turnieju
    - game_id (klucz obcy odwołujący się do tabeli Games): numer identyfikacyjny grę w jaką się gra na turnieju
    - max_players: maksymalna liczba graczy na turnieju
    - entry_fee: wpisowe
    - reward: nagroda za turniej

    $$ \Sigma = \left\{ \text{tournament\_id} \to \text{game\_id}, \text{tournament\_id} \to \text{max\_players},\text{tournament\_id} \to \text{entry\_fee}, \text{tournament\_id} \to \text{reward} \right\} $$

    Tournament id  wyznacza jednoznacznie gre, ilość graczy, wpisowe oraz nagrodę w turnieju, odwrotna relacja nie zachodzi. Zakładamy, że nagroda oraz wpisowe bezpośrednio  nie wynikają z siebie ani z gry rozgrywanej na turnieju.

7. Tabela Tournament_schedule: R(**tournament_id**, date)
    - tournament_id (klucz obcy odwołujący się do tabeli Tournaments): numer identyfikacyjny turnieju
    - date: data turnieju

    $$ \Sigma = \left\{ \text{tournament\_id} \to \text{date} \right\} $$

    Tabela łącząca turniej z jego datą. W jeden dzień może odbywać się więcej niż 1 turniej

8. Tabela Tournaments_results: R(**tournament_id, place**, customer_id)
    - tournament_id (klucz obcy odwołujący się do tabeli Tournaments): numer identyfikacyjny turnieju
    - place: miejsce zajęte w turnieju przez gracza (klienta)
    - customer_id (klucz obcy odwołujący się do tabeli Customers): numer identyfikacyjny klienta
    $$ \Sigma = \left\{ \text{tournament\_id} + \text{place} \to \text{client\_id} \right\} $$

    Tournament id w połączeniu z place wyznacza nam jednoznacznie osobę, która te miejsce zajęła w turnieju. Zakładamy, że w turniejach nie ma miejsc ex aequo.

9. Tabela Finances: R(**payment_id** , in_out, value, date, title)

    - payment_id: numer identyfikacyjny płatności
    - in_out: czy jest to płatność czy przychód
    - value: wartość płatności
    - date: data płatności
    - title: tytuł płatności

    $$ \Sigma = \left\{ \text{payment\_id} \to \text{in\_out}, \text{payment\_id} \to \text{value},\text{payment\_id} \to \text{date}, \text{payment\_id} \to \text{title} \right\} $$

    Tylko payment id wyznacza nam jednoznacznie przepływ pieniężny. 

10. Tabela Payoffs: R(**payment_id**, employee_id)

    - payment_id (klucz obcy odwołujący się do tabeli Finances): numer identyfikacyjny płatności  
    - employee_id (klucz obcy odwołujący się do tabeli Employees): numer identyfikacyjny pracownika
    $$ \Sigma = \left\{ \text{payment\_id} \to \text{employee\_id}  \right\} $$
    
    payment id wyznacza nam jednoznacznie przypisanego do tej płatności pracownika. Relacja w drugą stronę nie zachodzi bo pracownik może być przypisany do wielu płatności.
    


11. Tabela Rentals: R(**rental_id**,payment_id,employee_id, customer_id,inventory_id,rental_date,return_date)

    - rental_id: numer identyfikacyjny wypożyczenia
    - payment_id (klucz obcy odwołujący się do tabeli Finances) : numer identyfikacyjny płatności
    - employee_id (klucz obcy odwołujący się do tabeli Employees): numer identyfikacyjny pracownika
    - customer_id (klucz obcy odwołujący się do tabeli Customers): numer identyfikacyjny klienta
    - inventory_id (klucz obcy odwołujący się do tabeli Inventory): numer identyfikacyjny inwentarza
    - rental_date: data wypożyczenia gry
    - return_date: data oddania gry

    $$ \Sigma = \left\{\text{rental\_id} \to \text{payment\_id}, \text{rental\_id} \to \text{employee\_id},\text{rental\_id} \to \text{customer\_id},\text{rental\_id} \to \text{inventory\_id},\text{rental\_id} \to \text{rental\_date},\text{rental\_id} \to \text{return\_date}, \text{payment\_id}} \to \text{rental\_id} \right\} $$

    Rental id jednoznacznie nam wyznacza wypożyczenie, tak jak payment id.

12. Tabela Sales: R(**payment_id**,employee_id, customer_id,inventory_id)

    - payment_id (klucz obcy odwołujący się do tabeli Finances) : numer identyfikacyjny płatności
    - employee_id (klucz obcy odwołujący się do tabeli Employees): numer identyfikacyjny pracownika
    - customer_id (klucz obcy odwołujący się do tabeli Customers): numer identyfikacyjny klienta
    - inventory_id (klucz obcy odwołujący się do tabeli Inventory): numer identyfikacyjny inwentarza

    Z payment id wynika jednoznacznie jaka gra została sprzedana przez kogo i komu. Nie ma odwrotnych relacji.
$$ \Sigma = \left\{ \text{payment\_id} \to \text{employee\_id},\text{payment\_id} \to \text{customer\_id},\text{payment\_id} \to \text{game\_id}   \right\} $$


## Postać normalna bazy danych

Jak możemy zauważyć w naszej bazie danych w każdej tabeli wszystkie nietrywialne relację zaczynają się od nadklucza wię spełnia postać BCNF z czego wynika także że spełnia postać normalną EKNF.