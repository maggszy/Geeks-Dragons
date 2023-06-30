--  3. a) Ustal, które gry przynoszą największy dochód ze sprzedaży, a które z wypożyczeń.

-- SPRZEDAŻ
SELECT Games.game_id, Games.title, SUM(Finances.value) AS dochod, COUNT(*) AS game_num, Inventory.type
FROM Sales
INNER JOIN Finances USING(payment_id)
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Games USING(game_id)
GROUP BY Games.game_id
ORDER BY dochod DESC;

-- WYPOŻYCZENIA
SELECT Games.game_id, Games.title, SUM(Finances.value) AS dochod, COUNT(*) AS game_num, Inventory.type
FROM Rentals
INNER JOIN Finances USING(payment_id)
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Games USING(game_id)
GROUP BY Games.game_id
ORDER BY dochod DESC;

-- ----------------------------------------------------------
-- *4. Ustal dochód w każdym miesiącu ze sprzedaży gier

-- SPRZEDAŻ  - dochód i ilośc gier
SELECT EXTRACT(YEAR FROM Finances.date) AS year, EXTRACT(MONTH FROM Finances.date) AS month, SUM(Finances.value) AS dochod, COUNT(*) AS game_num
FROM Sales
INNER JOIN Finances USING(payment_id)
INNER JOIN Inventory USING(inventory_id)
GROUP BY year, month;

-- *5. Ustal dochód w każdym miesiącu z wypożyczeń gier

-- WYPOŻYCZENIA - dochód i ilośc gier
SELECT EXTRACT(YEAR FROM Finances.date) AS year, EXTRACT(MONTH FROM Finances.date) AS month, SUM(Finances.value) AS dochod, COUNT(*) AS game_num
FROM Rentals
INNER JOIN Finances USING(payment_id)
INNER JOIN Inventory USING(inventory_id)
GROUP BY year, month;
--  -----------------------------------------

-- *7. Wyznacz ranking najpopularniejszych gier (gry które były najczęściej wypożyczane/ największa ilośc wypożyczeń danej gry)

SELECT Games.game_id, Games.title,Finances.value --COUNT(*) AS game_num
FROM Rentals
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Games USING(game_id)
INNER JOIN Finances USING(payment_id)
GROUP BY Games.game_id
ORDER BY game_num DESC;


-- *8. Wyznacz ranking najpopularniejszych kupowanych gier (gry które były najczęściej kupowane/ największa ilośc kupionej danej gry)

SELECT Games.game_id, Games.title, COUNT(*) AS game_num
FROM Sales
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Games USING(game_id)
GROUP BY Games.game_id
ORDER BY game_num DESC;



-- *9. ustal ranking średnio najdłużej przetrzymywanych gier (najdłuższe wypożyczenie)

-- czy to zapytanie ma sens? w sensie wyniki są bardzo zbliżone xd
--  trzeba by było zaokrąglić avg_day_num
SELECT Games.game_id, Games.title, AVG(DATEDIFF(Rentals.return_date, Rentals.rental_date)) AS avg_day_num
FROM Rentals
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Games USING(game_id)
GROUP BY Games.game_id
ORDER BY avg_day_num DESC;
-- ----------------------------------------

-- *10. ustal ranking klientów, którzy najdłużej przetrzymywanych gier (najdłuższe wypożyczenie)

SELECT Customers.customer_id, CONCAT(Customers.first_name, " ", Customers.last_name) AS customer_name , DATEDIFF(Rentals.return_date, Rentals.rental_date) AS day_num
FROM Rentals
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Customers USING(customer_id) 
ORDER BY day_num DESC;



-- *11. Dochód firmy, ogólnie
-- 0: out
-- 1: in

SELECT EXTRACT(MONTH FROM date) AS month, CONCAT(YEAR(date),"-",MONTH(date)) AS year_month
FROM Finances
GROUP BY month, in_out

SELECT DATE_FORMAT(date, '%Y-%m') as ym  FROM Finances

SELECT COUNT(*) FROM Tournaments_results

-- SELECT tournament_id, COUNT(*) AS num_players
-- FROM Tournaments_results
-- GROUP BY tournament_id

SELECT tournament_id, Games.title
FROM Tournaments
INNER JOIN Games USING(game_id)
GROUP BY tournament_id
-- ------------------------------------------------

SELECT Games.game_id, Games.title, SUM(Finances.value) AS dochod, COUNT(*) AS game_num, GROUP_CONCAT(DATEDIFF(return_date,rental_date) SEPARATOR ",") AS rental_day
FROM Rentals
INNER JOIN Finances USING(payment_id)
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Games USING(game_id)
WHERE return_date IS NOT NULL
GROUP BY Games.game_id
ORDER BY dochod DESC;

--  *12. zrobienie podsumowania na podział kobiety/men i jakieś procentowe coś
-- ile kobiet było klientkami sklepu, a ile men
