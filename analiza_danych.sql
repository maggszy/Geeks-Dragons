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

-- *6. Ustal dochód w każdym miesiącu z turniejów

-- Turnieje - NA TEN MOMENT BRAK POŁĄCZEŃXD
-- SELECT EXTRACT(YEAR FROM Finances.date) AS year, EXTRACT(MONTH FROM Finances.date) AS month, SUM(Finances.value) AS dochod, COUNT(*) AS game_num
-- FROM Rentals
-- INNER JOIN Finances USING(payment_id)
-- INNER JOIN Inventory USING(inventory_id)
-- GROUP BY year, month


-- *7. Wyznacz ranking najpopularniejszych gier (gry które były najczęściej wypożyczane/ największa ilośc wypożyczeń danej gry)

SELECT Games.game_id, Games.title, COUNT(*) AS game_num
FROM Rentals
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Games USING(game_id)
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


-- *10. ustal ranking klientów, którzy najdłużej przetrzymywanych gier (najdłuższe wypożyczenie)

SELECT Customers.customer_id, CONCAT(Customers.first_name, " ", Customers.last_name) AS customer_name , DATEDIFF(Rentals.return_date, Rentals.rental_date) AS day_num
FROM Rentals
INNER JOIN Inventory USING(inventory_id)
INNER JOIN Customers USING(customer_id) 
ORDER BY day_num DESC;