
## Schemat bazy danych i zależności funkcyjne w tabelach

Klucze główne zaznaczamy przez pogrubienie.

1. Tabela Customers: R(**customer_id**, first_name, last_name, birth_date, email, phone)
 
    - customer_id [SMALLINT UNSIGNED] : numer  identyfikacyjny klienta
    - first_name [VARCHAR(45)]: imię klienta
    - last_name [VARCHAR(50)]: nazwisko klienta
    - birth_date [DATE]: data urodzenia klienta
    - email [VARCHAR(50)]: email klienta
    - phone [VARCHAR(12)]: numer telefonu klienta

    $$\Sigma = \left\{ \text{customer\_id} \to \text{first\_name}, \text{customer\_id} \to  \text{last\_name}, \text{customer\_id} \to \text{birth\_name},\text{customer\_id} \to \text{email}, \text{email} \to \text{customer\_id},\text{customer\_id} \to \text{phone}, \text{phone} \to \text{customer\_id}   \right\} $$

    Informacje o dokładnym kliencie możemy pozyskać przez customer_id. Dokładną identyfikację klienta zapewnia także jego email lub jego numer telefonu,ponieważ zakładamy, że każdy ma jeden unikalny numer telefony oraz adres email.
    

2. Tabela Employees: R(**employee_id**, first_name, last_name,start_work_date,end_work_date, email, phone, address_id)

    - employee_id [SMALLINT UNSIGNED]: numer identyfikacyjny pracownika
    - first_name [VARCHAR(45)]: imię pracownika
    - last_name [VARCHAR(50)]: nazwisko pracownika
    - start_work_date [DATE]: data zatrudnienia (rozpoczęcie pracy)
    - end_work_date [DATE]: data zakończenia pracy
    - email [VARCHAR(50)]: adres email pracownika
    - phone [VARCHAR(12)]: numer telefonu pracownika
    - address_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Addresses : numer identyfikacyjny adresu.

    $$\Sigma = \left\{ \text{employee\_id} \to \text{first\_name}, \text{employee\_id} \to  \text{last\_name}, \text{employee\_id} \to \text{start\_work\_date}, \text{employee\_id} \to \text{start\_work\_date},\text{employee\_id} \to \text{email}, \text{email} \to \text{employee\_id}, \text{employee\_id} \to \text{phone}, \text{phone} \to \text{employee\_id} , \text{employee\_id} \to \text{address\_id}    \right\} $$  

    Pracownik jest jednoznaczne zdefiniowany przez employee_id. Tak jak w przypadku klientów, pracownika też możemy rozpoznać po jego numerze telefonu lub email.
    
3. Tabela Addresses: R(**address_id**, country, city, street,number,postal_code)

    - address_id [SMALLINT UNSIGNED]: numer identyfikacyjny adresu.
    - country [VARCHAR(50)]: państwo
    - city [VARCHAR(50)]: miasto
    - street [VARCHAR(50)]: ulica
    - number [SMALLINT UNSIGNED]: numer budynku
    - postal_code [VARCHAR(10)]: kod pocztowy.

    $$\Sigma = \left\{\text{adress\_id} \to \text{country}, \text{adress\_id} \to \text{city},\text{adress\_id} \to \text{street},\text{adress\_id} \to \text{number}\text{adress\_id} \to \text{postal\_code}, \text{country} + \text{city} +\text{street} +\text{number} + \text{postal\_code} \to \text{adress\_id} \right\}$$

    Adres jest dokładnie, jednoznacznie wyznaczony dla danego adress_id. Pozostałe pola tylko razem wskażą nam dokładny adres. 
    
4. Tabela Games: R(**game_id**,title, release_year,min_players,max_players,play_time,min_age,type,price)
    
    - game_id [SMALLINT UNSIGNED]: numer identyfikacyjny gry
    - title [VARCHAR(100)]: oryginalny tytuł gry
    - release_year [DATE]: rok wydania gry
    - min_players [TINYINT UNSIGNED]: minimalna liczba graczy
    - max_players [TINYINT UNSIGNED]: maksymalna liczba graczy
    - play_time [SMALLINT UNSIGNED]: szacowany czas gry w minutach
    - min_age [TINYINT UNSIGNED]: wiek minimalny do zagrania w grę
    - type [VARCHAR(18)]:  typ gry tzn czy jest to gr czy rozszerzenie do gry 
    - price [DECIMAL]: cena za kupno gry

    $$\Sigma = \left\{ \text{game\_id} \to \text{title}, \text{game\_id} \to \text{release\_year},\text{game\_id} \to \text{min\_players},\text{game\_id} \to \text{max\_players},\text{game\_id} \to \text{play\_time}, \text{game\_id} \to \text{min\_age}, \text{game\_id} \to \text{price}, ,\text{game\_id} \to \text{description} \right\}$$

   Gra jest wyznaczona jednoznacznie przez game_id. Połączenie wszystkich pozostałych informacji nie musi nam jednoznacznie określić gry ( Tytuły nie muszą być unikatowe)


5. Tabela Inventory: R(**inventory_id**, game_id,type)

    - inventory_id [SMALLINT UNSIGNED]: numer identyfikacyjny inwentarza
    - game_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Games): numer identyfikacyjny grę
    - type [CHAR(1)]: przeznaczenie gry na magazynie ( czy na sprzedaż, czy na wypożyczenie, czy na turniej)

    $$ \Sigma = \left\{ \text{inventory\_id} \to \text{game\_id} , \text{inventory\_id} \to \text{type} \right\} $$

    Gra w magazynie jest wyznaczona jednoznacznie przez inventory_id. Reszta informacji nie pozwala nam tego określić ponieważ możemy mieć kilka takich samych tytułów o takim samym przeznaczeniu.
    
6. Tabela Tournaments: R(**tournament_id**, game_id,max_players,entry_fee,prize)

    - tournament_id [SMALLINT UNSIGNED]: numer identyfikacyjny turnieju
    - game_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Games): numer identyfikacyjny grę w jaką się gra na turnieju
    - max_players [TINYINT UNSIGNED]: maksymalna liczba graczy na turnieju
    - entry_fee [DECIMAL]: wpisowe
    - prize [DECIMAL]: nagroda za turniej zamiast 

    $$ \Sigma = \left\{ \text{tournament\_id} \to \text{game\_id}, \text{tournament\_id} \to \text{max\_players},\text{tournament\_id} \to \text{entry\_fee}, \text{tournament\_id} \to \text{prize} \right\} $$

    Turniej jest jednoznacznie wyznaczony jedynie przez tournament_id. Zakładamy, że nagroda nie jest bezpośrednio zależna iod wpisowego i liczby graczy.

7. Tabela Tournament_schedule: R(**tournament_id**, date)

    - tournament_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Tournaments): numer identyfikacyjny turnieju
    - date [DATE]: data turnieju

    $$ \Sigma = \left\{ \text{tournament\_id} \to \text{date} \right\} $$

    Tabela łącząca turniej z jego datą. W jeden dzień może odbywać się więcej niż 1 turniej

8. Tabela Tournaments_results: R(**tournament_id, place**, customer_id)

    - tournament_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Tournaments): numer identyfikacyjny turnieju
    - place [SMALLINT UNSIGNED]: miejsce zajęte w turnieju przez gracza (klienta)
    - customer_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Customers): numer identyfikacyjny klienta
    $$ \Sigma = \left\{ \text{tournament\_id} + \text{place} \to \text{client\_id} \right\} $$

    Identyfikator turnieju  w połączeniu z miejscem wyznacza nam jednoznacznie osobę, która te miejsce zajęła w turnieju. Zakładamy, że w turniejach nie ma miejsc ex aequo.

9. Tabela Finances: R(**payment_id** , in_out, value, date)

    - payment_id [MEDIUMINT UNSIGNED]: numer identyfikacyjny płatności
    - in_out [TINYINT]: czy jest to płatność czy przychód
    - value [DECIMAL]: wartość płatności
    - date [DATE]: data płatności

    $$ \Sigma = \left\{ \text{payment\_id} \to \text{in\_out}, \text{payment\_id} \to \text{value},\text{payment\_id} \to \text{date} \right\} $$

    Tylko payment id wyznacza nam jednoznacznie przepływ pieniężny.

10. Tabela Payoffs: R(**payment_id**, employee_id)

    - payment_id [MEDIUMINT UNSIGNED] (klucz obcy odwołujący się do tabeli Finances): numer identyfikacyjny płatności  
    - employee_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Employees): numer identyfikacyjny pracownika
    $$ \Sigma = \left\{ \text{payment\_id} \to \text{employee\_id}  \right\} $$
    
    Każda wypłata jest jednoznacznie zdefinowana przez payment_id i ma przypisanego pracownika. Relacją w drugą stronę nie zachodzi ponieważ pracownik może mieć kilka wypłat. 

11. Tabela Rentals: R(**rental_id**,payment_id,employee_id, customer_id,inventory_id,rental_date,return_date)

    - rental_id [SMALLINT UNSIGNED]: numer identyfikacyjny wypożyczenia
    - payment_id [MEDIUMINT UNSIGNED] (klucz obcy odwołujący się do tabeli Finances) : numer identyfikacyjny płatności
    - employee_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Employees): numer identyfikacyjny pracownika
    - customer_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Customers): numer identyfikacyjny klienta
    - inventory_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Inventory): numer identyfikacyjny inwentarza
    - rental_date [DATE]: data wypożyczenia gry
    - return_date [DATE]: data oddania gry

    $$\Sigma = \left\{\text{rental\_id} \to \text{payment\_id}, \text{rental\_id} \to \text{employee\_id},\text{rental\_id} \to \text{customer\_id},\text{rental\_id} \to \text{inventory\_id},\text{rental\_id} \to \text{rental\_date},\text{rental\_id} \to \text{return\_date}, \text{payment\_id} \to \text{rental\_id} \right\}$$

   Wypożyczenie jest jednoznacznie wyznaczone przez rental_id, tak jak payment id. Pozostałe pola nie muszą jednoznacznie wyznaczyć wypożyczenia.

12. Tabela Sales: R(**sales_id**,payment_id,employee_id, customer_id,inventory_id)

    - sales_id [SMALLINT UNSIGNED]: numer identyfikacyjny sprzedaży gry 
    - payment_id [MEDIUMINT UNSIGNED] (klucz obcy odwołujący się do tabeli Finances) : numer identyfikacyjny płatności
    - employee_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Employees): numer identyfikacyjny pracownika
    - customer_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Customers): numer identyfikacyjny klienta
    - inventory_id [SMALLINT UNSIGNED] (klucz obcy odwołujący się do tabeli Inventory): numer identyfikacyjny inwentarza

    Każda sprzedaż ma unikatowy sales_id. Transakcja sprzedaży może być też jednoznacznie wyznaczona przez payment_id
    
    $$ \Sigma = \left\{ \text{sales\_id} \to \text{payment\_id}, \text{sales\_id} \to \text{employee\_id},\text{sales\_id} \to \text{customer\_id},\text{sales\_id} \to \text{game\_id} ,  \text{payment\_id} \to \text{sales\_id}  \right\} $$

## Postać normalna bazy danych

Jak możemy zauważyć w naszej bazie danych w każdej tabeli wszystkie nietrywialne relację zaczynają się od nadklucza wię spełnia postać BCNF z czego wynika także że spełnia postać normalną EKNF.