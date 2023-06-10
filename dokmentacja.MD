
## Zależności funkcyjne w tabelach

Klucze gółwne zaznaczamy przez pogrubienie 

- Tabela Customers: R(**customer_id**, first_name, last_name, birth_date, email, phone)
 $$\Sigma = \left\{ \text{customer\_id} \to \text{first\_name}, \text{customer\_id} \to  \text{last\_name}, \text{customer\_id} \to \text{birth\_name},\text{customer\_id} \to \text{email}, \text{email} \to \text{customer\_id},\text{customer\_id} \to \text{phone}, \text{phone} \to \text{customer\_id}   \right\} $$  

customer_id mówi nam jednoznacznie jaki to jest klient , więc znamy jego imię, nazwisko oraz datę urodzin. Imię i nazwisko oraz data urodzin klienta nie wyznacza nam jednoznacznie customer_id, ponieważ klienci mogą tak samo się nazywać i urodzić się w tym samym dniu przykładowo w bazie możemy mieć dwóch Janów Kowalski urodzonych 01.01.2001. Customer_id mówi nam jednoznacznie o mailu klienta, ponieważ maile są unikatowe, wynikanie działa w dwie strony. Zakładamy, że każdy klient ma jednego maila, mail może być użyty tylko dla jednej osoby.  

 


<!-- 
- Tabela Customers_phone: R(**customer_id**, phone)
 $$\Sigma = \left\{ \text{customer\_id} \to \text{phone}, \text{phone} \to \text{customer\_id}   \right\} $$  

customer_id mówi nam jednoznacznie o telefonie klienta, ponieważ numery telefonów są unikatowe, wynikanie działa w dwie strony. Zakładamy że każdy klient ma jeden numer telefonu, który może być przypisany tylko do jednej osoby. -->

- Tabela Gender: R(**first_name**, gender)
 $$\Sigma = \left\{ \text{first\_name} \to \text{gender}   \right\} $$  

 Zakładamy, że imię jednoznacznie mówi nam o płci ( nie ma takiego samego imienia dla różnych płci).
 
- Tabela Employees: R(**employee_id**, first_name, last_name,start_work_date,end_work_date, email, phone, address_id)
 $$\Sigma = \left\{ \text{employee\_id} \to \text{first\_name}, \text{employee\_id} \to  \text{last\_name}, \text{employee\_id} \to \text{start\_work\_date}, \text{employee\_id} \to \text{start\_work\_date},\text{employee\_id} \to \text{email}, \text{email} \to \text{employee\_id}, \text{employee\_id} \to \text{phone}, \text{phone} \to \text{employee\_id} , \text{employee\_id} \to \text{adress\_id}    \right\} $$  

employee_id mówi nam jednoznacznie jaki to jest pracownik, więc zanmy jego imię, nazwisko, datę zatrudnienia, datę końca pracy. Imię, nazwisko, data zatrudnienia, data końca pracy nie wyznacza nam jednoznacznie pracownika, ponieważ pracownicy mogą tak samo się nazywać i być zatrudnieni w tym samy czasie i skończyć pracę też w tym samy dniu.  employee_id mówi nam jednoznacznie o mailu pracownika, ponieważ maile są unikatowe, wynikanie działa w dwie strony. Zakładamy, że każdy pracownik ma jednego maila, mail może być użyty tylko dla jednej osoby.
employee_id mówi nam jednoznacznie o telefonie pracownika, ponieważ numery telefonów są unikatowe, wynikanie działa w dwie strony. Zakładamy że każdy pracownik ma jeden numer telefonu, który może być przypisany tylko do jednej osoby.Każdy pracownik ma przypisany jeden adress, ale jeden adrees może mieć kilku pracowników.


<!-- - Tabela Employee_emails: R(**employee_id**, email)
 $$\Sigma = \left\{ \text{employee\_id} \to \text{email}, \text{email} \to \text{employee\_id}   \right\} $$  

employee_id mówi nam jednoznacznie o mailu pracownika, ponieważ maile są unikatowe, wynikanie działa w dwie strony. Zakładamy, że każdy pracownik ma jednego maila, mail może być użyty tylko dla jednej osoby. -->

<!-- - Tabela Employee_phone: R(**employee_id**, phone)
 $$\Sigma = \left\{ \text{employee\_id} \to \text{phone}, \text{phone} \to \text{employee\_id}   \right\} $$  

employee_id mówi nam jednoznacznie o telefonie pracownika, ponieważ numery telefonów są unikatowe, wynikanie działa w dwie strony. Zakładamy że każdy pracownik ma jeden numer telefonu, który może być przypisany tylko do jednej osoby. -->

<!-- - Tabela Employee_adress: R(**employee_id**, adress_id)
 $$\Sigma = \left\{ \text{employee\_id} \to \text{adress\_id} \right\} $$  

Każdy pracownik ma przypisany jeden adress, ale jeden adrees może mieć kilku pracowników. -->

- Tabela Addresses: R(**adress_id**, country, city, street,number,postal_code)

$$\Sigma = \left\{\text{adress\_id} \to \text{country}, \text{adress\_id} \to \text{city},\text{adress\_id} \to \text{street},\text{adress\_id} \to \text{number}\text{adress\_id} \to \text{postal\_code}, \text{country} + \text{city} +\text{street} +\text{number} + \text{postal\_code} \to \text{adress\_id} \right\}$$

Adress_id wyznacza nam dokładnie adress zamieszkania i odwrotnie. Zakładamy, że mogą istnieć dwa takie same adresy lecz z innym kodem pocztowym. Kod poczrtowy nie jest wyznaczony przez country + city+ street ponieważ mogą występować takie same miasta w kraju z takimi samymi ulicami i numerami, lecz różniące się kodem pocztowym. 


- Tabela Games: R(**game_id**,title, description, release_year,min_players,max_players,play_time,min_age,price)

$$\Sigma = \left\{ \text{game\_id} \to \text{release\_year},\text{game\_id} \to \text{min\_players},\text{game\_id} \to \text{max\_players},\text{game\_id} \to \text{play\_time}, \text{game\_id} \to \text{min\_age}, \text{game\_id} \to \text{price}, \text{game\_id} \to \text{title},\text{game\_id} \to \text{description},\text{title} + \text{description} \to \text{game\_id} \right\}$$

Game id definiuje jednoznacznie rok wydania, minimalną ilość groczy, maksymalną ilość grczy, czas gry, minmalny wiek graczy oraz cenę zakupu gry.Każda gra ma zdefinowany tytuł i opis. Może się zdarzyć sytuacja gdzie dwie gry mają ten sam tytuł albo opis. Zakładamy że połączenie tytułu i opisu daje nam jednoznacznie informację o grze.

<!-- - Tabela Games_title: R(**game_id**, title, description)
 $$\Sigma = \left\{ \text{game\_id} \to \text{title},\text{game\_id} \to \text{description},\text{title} + \text{description} \to \text{game\_id} \right\} $$

Każda gra ma zdefinowany tytuł i opis. Może się zdarzyć sytuacja gdzie dwie gry mają ten sam tytuł albo opis. Zakładamy że połączenie tytułu i opisu daje nam jednoznacznie informację o grze. -->

- Tabela Inventory: R(**inventory_id**, game_id,type)

$$ \Sigma = \left\{ \text{inventory\_id} \to \text{game\_id} , \text{inventory\_id} \to \text{type} \right\} $$

Inventory id wyznacza nam jednoznacznie jaka to gra i jakie jest jej przeznaczenie. game_id mówi nam co to za gra, type mówi jakie jest przeznaczenie te gry ( czy na sprzedaż czy na wypożyczenie czy na turniej). Możemy mieć kilka tych samych gier z tym samy lub inny przeznaczeniem, dlatego z game_id i typu nie wynika inventory_id


- Tabela Tournamet_schedule: R(**tournamet_id**, date)

$$ \Sigma = \left\{ \text{tournament\_id} \to \text{date} \right\} $$

Tabela łącząca turniej z jego datą. 

- Tabela Tournaments: R(**tournment_id**, game_id,max_players,entry_fee,reward )

$$ \Sigma = \left\{ \text{tournament\_id} \to \text{game\_id}, \text{tournament\_id} \to \text{max\_players},\text{tournament\_id} \to \text{entry\_fee}, \text{tournament\_id} \to \text{reward} \right\} $$

Każdy turniej ma określoną gre, ilość graczy, wpisowe oraz nagrodę. Te parametry nie mówią jednoznacznie, który jest to turniej. Zakładamy, że nagroda oraz wpisowe nie wynikają z siebie ani z gry rozgrawanej na turnieju.

- Tabela Tournaments_results: R(**tournament_id**, place, customer_id)

$$ \Sigma = \left\{ \text{tournament\_id} + \text{place} \to \text{client\_id} \right\} $$

Każda pozycja w danym turnieju ma okreśnoną osobę która tą pozycję zajeła. 

- Tabela Finaces: R(**payment_id** , in_out, value, date, title)
$$ \Sigma = \left\{ \text{payment\_id} \to \text{in\_out}, \text{payment\_id} \to \text{value},\text{payment\_id} \to \text{date}, \text{payment\_id} \to \text{title} \right\} $$

Każda płatność ma okreśnone czy my płacimy czy nam jest płacone, wartość tej  płatności( wartość absolutna) oraz data płatności. Płatność nie jest jednoznacznie zdefiniowana przez datę , wrtość i czy jest kosztem czy przychodem i nazwę.

- Tabela Payoffs: R(**payment_id**, employee_id)

$$ \Sigma = \left\{ \text{payment\_id} \to \text{employee\_id}  \right\} $$

Każda wypłata jest powiązana z pracownikiem.


- Tabela Rentals: R(**rental_id**,payment_id,employee_id, customer_id,inventory_id,rental_date,return_date)

$$ \Sigma = \left\{\text{rental\_id} \to \text{peyment\_id}, \text{rental\_id} \to \text{employee\_id},\text{rental\_id} \to \text{customer\_id},\text{rental\_id} \to \text{inventory\_id},\text{rental\_id} \to \text{rental\_date},\text{rental\_id} \to \text{return\_date}, \text{inventory\_id}+ \text{rental\_date} \to \text{rental\_id}   \right\} $$

Każde wypożyczenie jest jednoznacznie związane z przepływem gotówki,pracownikiem, klientem, przedmiotem, datą wyporzyczenia i datą oddania. Wypożyczenie jednoznacznie określa też inventory_id połączony z rental_date. Jeśli jest gra nie oddana ro payment_id jest pusty tak jak return_date.


- Tabela Sales: R(**payment_id**,employee_id, customer_id,inventory_id)

$$ \Sigma = \left\{ \text{payment\_id} \to \text{employee\_id},\text{payment\_id} \to \text{customer\_id},\text{payment\_id} \to \text{game\_id}   \right\} $$

Z payment_id wynika pracownik, klient, oraz jaka graa. Nie ma żadnej relacji w drugą stronę.







