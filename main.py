# to do
# emploees ADDRESS TABLE!
# emploees: address id




from generate import *

import pandas as pd 
from sqlalchemy import create_engine
from urllib.parse import quote  

username = "team02"
password = "te@m0z"
database = "team02"


if __name__ == "__main__":
    proportions = np.array([0.4, 0.25, 0.35]) # ALL_ENG, W_PL, M_PL
    names_lists = (eng_first_names, eng_last_names, pl_first_names_w, pl_first_names_m,pl_last_names_w, pl_last_names_m)

    games_tbl = generate_games_tbl(new_games_df)
    tournament_games = random_games(games_tbl)

    phone_numbers = generate_ALL_phone_numbers(CUSTOMERS_AMOUNT+EMPLOYEES_AMOUNT)
    customers_tbl = generate_customers_tbl(names_lists, phone_numbers, proportions)
    employees_tbl = generate_employees_tbl(phone_numbers)
    payoffs_tbl, temp_payoff_pay = generate_payoffs()
    termines_tbl = generate_schedule_tbl()
    tournaments_tbl = generate_tournaments_tbl(tournament_games)
    results_tbl = generate_results_table(tournaments_tbl, customers_tbl)
    rentals_tbl = generate_rentals_tbl(customers_tbl["customer_id"])
    last_rent_inventory_id = len(np.unique(rentals_tbl["inventory_id"]))
    sales_tbl = generate_sales_tbl(customers_tbl, last_rent_inventory_id)

    temp_rent_pay = temp_rent_payments(rentals_tbl)
    temp_sales_pay = temp_sales_payments(sales_tbl, games_tbl)
    temp_fee_pay = temp_entry_fee_payments()
    print(temp_fee_pay)
    payments_tbl = concat_payments( temp_payoff_pay, temp_sales_pay, temp_rent_pay, temp_fee_pay)

    temp_rent = temp_rent_invent(rentals_tbl)
    temp_sales =  temp_sales_invent(sales_tbl, last_rent_inventory_id)
    temp_tour =  temp_tour_invent(tournament_games, temp_rent, temp_sales)
    inventory_tbl = generate_inventory_tbl(temp_rent,temp_sales,temp_tour)
    
    sales_tbl = drop_from_sales(sales_tbl)
    rentals_tbl = drop_from_rentals(rentals_tbl)

    engine = create_engine("mysql+pymysql://team02:%s@giniewicz.it:3306/team02" %quote(password))
    connection = engine.connect()
    games_tbl.to_sql("Games", con =  connection, if_exists='append', index=False)
    customers_tbl.to_sql("Customers", con =  connection, if_exists='append', index=False)
    employees_tbl.to_sql("Employees", con =  connection, if_exists='append', index=False)
    termines_tbl.to_sql("Tournament_schedule", con =  connection, if_exists='append', index=False)
    tournaments_tbl.to_sql("Tournaments", con =  connection, if_exists='append', index=False)
    results_tbl.to_sql("Tournaments_results", con =  connection, if_exists='append', index=False)
    rentals_tbl.to_sql("Rentals", con =  connection, if_exists='append', index=False)
    sales_tbl.to_sql("Sales", con =  connection, if_exists='append', index=False)
    inventory_tbl.to_sql("Inventory", con =  connection, if_exists='append', index=False)
    payments_tbl.to_sql("Finances", con =  connection, if_exists='replace', index=False)
    payoffs_tbl.to_sql("Payoffs", con =  connection, if_exists='replace', index=False)
    connection.close()