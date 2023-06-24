from generate import *

import pandas as pd 
from sqlalchemy import create_engine
from urllib.parse import quote  

username = "team02"
password = "te@m0z"
database = "team02"






proportions = np.array([0.4, 0.25, 0.35]) # ALL_ENG, W_PL, M_PL
names_lists = (eng_first_names, eng_last_names, pl_first_names_w, pl_first_names_m,pl_last_names_w, pl_last_names_m)

games_tbl = generate_games_tbl(new_games_df)
phone_numbers = generate_ALL_phone_numbers(CUSTOMERS_AMOUNT+EMPLOYEES_AMOUNT)
customers_tbl = generate_customers_tbl(names_lists, phone_numbers, proportions)
employees_tbl = generate_employees_tbl(phone_numbers)

termines_tbl = generate_termines_tbl()

tournament_games = random_games(games_tbl)
tournaments_tbl = generate_tournaments_tbl(tournament_games)

results_tbl = generate_results_table(tournaments_tbl, customers_tbl)

rentals_tbl = generate_rentals_tbl(customers_tbl["customer_id"])

last_rent_inventory_id = len(np.unique(rentals_tbl["inventory_id"]))
sales_tbl = generate_sales_tbl(customers_tbl, last_rent_inventory_id)
print(sales_tbl.head())

temp_rent = temp_rent_invent(rentals_tbl)
temp_sales =  temp_sales_invent(sales_tbl, last_rent_inventory_id)
temp_tour =  temp_tour_invent(tournament_games, temp_rent, temp_sales)
inventory_tbl = generate_inventory_tbl(temp_rent,temp_sales,temp_tour)


engine = create_engine("mysql+pymysql://team02:%s@giniewicz.it:3306/team02" %quote(password))
connection = engine.connect()
games_tbl.to_sql("games", con =  connection, if_exists='replace', index=False)
customers_tbl.to_sql("customers", con =  connection, if_exists='replace', index=False)
employees_tbl.to_sql("employees", con =  connection, if_exists='replace', index=False)
games_tbl.to_sql("games", con =  connection, if_exists='replace', index=False)
termines_tbl.to_sql("termines", con =  connection, if_exists='replace', index=False)
tournaments_tbl.to_sql("tournaments", con =  connection, if_exists='replace', index=False)
results_tbl.to_sql("results", con =  connection, if_exists='replace', index=False)
rentals_tbl.to_sql("rentals", con =  connection, if_exists='replace', index=False)
sales_tbl.to_sql("sales", con =  connection, if_exists='replace', index=False)
inventory_tbl.to_sql("inventory", con =  connection, if_exists='replace', index=False)