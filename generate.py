
import datetime
import random
from itertools import chain

import numpy as np
import pandas as pd
from faker import Faker

# CONSTANTS 
GAMES_AMOUNT = 50
CUSTOMERS_AMOUNT = 1000
EMPLOYEES_AMOUNT = 6
YEAR = 2022
PRICE_FOR_DAY = 10

new_games_df = pd.read_csv("data/games.csv", encoding= 'unicode_escape', sep = ";")
eng_first_names_df = pd.read_csv("data/english_first_names.csv").sort_values(by = ["Rank"])
eng_last_names_df = pd.read_csv("data/english_last_names.csv", sep=";")
pl_first_names_w_df = pd.read_csv("data/polish_female_names.csv")
pl_first_names_m_df = pd.read_csv("data/polish_male_names.csv")
pl_last_names_w_df = pd.read_csv("data/polish_female_last_names.csv")
pl_last_names_m_df = pd.read_csv("data/polish_male_last_names.csv")

eng_first_names = eng_first_names_df["Child's First Name"][0:2000]
eng_last_names = eng_last_names_df["SURNAME"] # only 1000 most popular
pl_first_names_w = pl_first_names_w_df["IMIĘ PIERWSZE"][0:100]
pl_first_names_m = pl_first_names_m_df["IMIĘ PIERWSZE"][0:100]
pl_last_names_w= pl_last_names_w_df["Nazwisko aktualne"][0:500]
pl_last_names_m = pl_last_names_m_df["Nazwisko aktualne"][0:500]



def generate_list_with_occurrences(numbers, occurrences):
    result = [number  for number, occurrence in zip(numbers, occurrences) for _ in range(occurrence)]
    return result

def generate_date_from_day_number(row):
    return datetime.datetime.strptime(str(YEAR) + "-" + str(row["rent_day"]), "%Y-%j").strftime("%d.%m.%Y")

def generate_return_date(row):
    rental_date = datetime.datetime.strptime(row["rental_date"], "%d.%m.%Y")
    return_date = rental_date  + datetime.timedelta(days = row["duration"] ) # maksymalnie tydzien 
    return  return_date.strftime("%d.%m.%Y") if return_date.year == rental_date.year else None

def generate_employee_id(year_day):
    if year_day % 3 == 0:
        return random.randint(1,2)
    elif year_day % 3 == 1:
        return random.randint(1,2)
    elif year_day % 3 == 2:
        return random.randint(5,6)

def generate_games_tbl(new_games_df):
    games_df = new_games_df[[ "details.name","details.yearpublished", 'details.playingtime', 'details.minage',  "details.minplayers", "details.maxplayers" , "details.description", "game.type"]]
    games_df.rename(columns = {"details.name":"Name", "details.yearpublished": "Year Published", 'details.playingtime':"Playing Time", 'details.minage': "Min Age", "details.minplayers": "Min Players", "details.maxplayers": "Max Players", "details.description":"Description", "game.type":"Type"}, inplace=True)
    games_tbl = games_df.sample(n = GAMES_AMOUNT)
    games_tbl.insert(0, "game_id", np.arange(1, GAMES_AMOUNT+1))
    games_tbl["Price"] = np.round(np.random.uniform(50, 200, GAMES_AMOUNT)) + 0.99
    return games_tbl

def generate_birth_dates(n):
    fake = Faker()
    birth_dates = [fake.date_between(start_date = "-50y", end_date = "-20y").strftime("%d.%m.%Y") for _ in range(n)]
    return birth_dates

def generate_ALL_phone_numbers(n):
    phone_numbers = random.sample(range(100000000, 999999999), n)
    return phone_numbers

def generate_email(row):
    return row["first_name"].lower()+"."+ row["last_name"].lower() + str(np.random.randint(0,1000))+ "@mail.com"

def generate_customers_tbl( names_lists,phone_numbers, proportions = np.array([0.4, 0.25, 0.35])):
    numbers = proportions * CUSTOMERS_AMOUNT
    customers_tbl = pd.DataFrame()
    (eng_first_names, eng_last_names, pl_first_names_w, pl_first_names_m,pl_last_names_w, pl_last_names_m) = names_lists
    customers_tbl["customer_id"] = np.arange( 1, CUSTOMERS_AMOUNT+1)
    customers_tbl["first_name"]= np.concatenate([np.random.choice(eng_first_names,int( numbers[0])), np.random.choice(pl_first_names_w,int( numbers[1])), np.random.choice(pl_first_names_m,int( numbers[2]))])
    customers_tbl["last_name"]= np.concatenate([np.random.choice(eng_last_names,int( numbers[0])), np.random.choice(pl_last_names_w,int( numbers[1])), np.random.choice(pl_last_names_m,int( numbers[2]))])
    customers_tbl["first_name"] = customers_tbl["first_name"].apply(str.capitalize)
    customers_tbl["last_name"] = customers_tbl["last_name"].apply(str.capitalize)
    customers_tbl["birth_date"] = generate_birth_dates(CUSTOMERS_AMOUNT)
    customers_tbl["email"] = customers_tbl.apply(lambda row: generate_email(row), axis=1)
    customers_tbl["phone_number"] = phone_numbers[0:CUSTOMERS_AMOUNT]
    return customers_tbl



def generate_employees_tbl(phone_numbers):
    fake = Faker()
    employees_tbl = pd.DataFrame()
    women_amount = random.randint(1, EMPLOYEES_AMOUNT)
    men_amount = EMPLOYEES_AMOUNT - women_amount
    employees_tbl["employee_id"] = np.arange( 1, EMPLOYEES_AMOUNT+1)
    employees_tbl["first_name"] = np.concatenate( [np.random.choice(pl_first_names_w,int(women_amount)), np.random.choice(pl_first_names_m,int( men_amount ))])
    employees_tbl["last_name"] = np.concatenate( [np.random.choice(pl_last_names_w,int(women_amount)), np.random.choice(pl_last_names_m,int( men_amount))])
    employees_tbl["email"] = employees_tbl.apply(lambda row: generate_email(row), axis=1)
    employees_tbl["phone_number"] = phone_numbers[-EMPLOYEES_AMOUNT-1: -1]
    employees_tbl["birth_date"] = [fake.date_between(start_date = "-50y", end_date = "-20y").strftime("%d.%m.%Y") for _ in range(EMPLOYEES_AMOUNT)]
    employees_tbl["start_work_date"] = [fake.date_between(start_date = "-80y", end_date = "-2y").strftime("%d.%m.%Y") for _ in range(EMPLOYEES_AMOUNT)]
    return employees_tbl


payoff_tbl = pd.DataFrame()

def generate_termines_tbl():
    termines_tbl = pd.DataFrame()
    termines_tbl["tournament_id"] = range(1, 13)
    first_thursdays = [(datetime.date(YEAR, month, 1) + datetime.timedelta(days=((6 - datetime.date(YEAR, month, 1).weekday()) % 7))).strftime("%d.%m.%y") for month in range(1, 13)]
    termines_tbl["date"] = first_thursdays
    return termines_tbl

def random_games(games_tbl):
    # Z gier które zostały wyznaczone dla sklepu losuję 5 gier, które będą grami turniejowymi. (typ = board game, max graczy >= 4)
    return random.sample( games_tbl[( games_tbl["Type"] == "boardgame") & ( games_tbl["Max Players"] >= 4) ]["game_id"].to_list(), 5)

def generate_tournaments_tbl(tournament_games):
    tournaments_tbl = pd.DataFrame()
    tournaments_tbl["tournament_id"] = range(1, 13)
    tournaments_tbl["game_id"] = random.choices(tournament_games, k = 12)
    tournaments_tbl["max_players"] = 16 * 4
    tournaments_tbl["entry_fee"] = 20
    tournaments_tbl["prize"] = 150
    return tournaments_tbl

def generate_results_table(tournaments_tbl, customers_tbl):
    results_tbl = pd.DataFrame()
    tournament_ids = [64 * [i] for i in tournaments_tbl["tournament_id"]]
    results_tbl["tournament_id"] = [i for i in chain.from_iterable(tournament_ids)]
    results_tbl["position"] = [place for place  in range(1,65)] * 12
    results = [random.sample(customers_tbl["customer_id"].to_list(), k = 64) for _ in range(1, 13)]
    results_tbl["customer_id"] = [i for i in chain.from_iterable(results)]
    results_tbl.insert(0,"result_id", range(1,len(results_tbl)+1))
    return results_tbl

def simulate_inventory(rentals_tbl):

    inventory = {} # game_id : [inventory_id]
    available = {} # game_id : [inventory_id]
    will_return = {} # return day : {inventory_id}

    inv_counter = 1
    for day in range(1, 366):

        #print(f"day:{day}")
        temp = rentals_tbl[rentals_tbl["rent_day"] == day ]
        games_needed = temp["game_id"]
        #print(f"games needed: {games_needed.to_list()}")
        for game_id in games_needed:
            rentals_tbl.loc[(rentals_tbl["rent_day"] == day)&(rentals_tbl["game_id"] == game_id), "employee_id"] = generate_employee_id(day)
            try : # if available  set inv_id
                inv_id = available[game_id].pop()
            except : # if not available add to inventory and set inv_id
                if game_id in inventory.keys():
                    inventory[game_id].append(inv_counter)
                else:
                    inventory[game_id] = [inv_counter]
                    available[game_id] = []
                inv_id = inv_counter
                inv_counter += 1

            #set inv_id in rentals_tbl
            rentals_tbl.loc[(rentals_tbl["rent_day"] == day)&(rentals_tbl["game_id"] == game_id), "inventory_id"] = inv_id
            # add current inv_id to will return
            return_day = rentals_tbl.loc[(rentals_tbl["rent_day"] == day) & (rentals_tbl["inventory_id"] == inv_id), "return_day"].to_list()[0] 
            if return_day in will_return.keys():
                will_return[return_day].append((game_id, inv_id))
            else:
                will_return[return_day] = [(game_id, inv_id)]
        #move from will return to available
        try:
            #print(f"returns today: {will_return[day]}")
            for key, value in enumerate( will_return[day]):
                game_id, inv_id = will_return[day][key]
                available[game_id].insert(0, inv_id)

            del will_return[day]
        except:
            pass


    ##print(f"available: {available}")
    #print(f"current inventory: {inventory}")
    #print(f"will return: {will_return}")
    return rentals_tbl

def generate_rentals_tbl(customers:list):
    rentals_tbl = pd.DataFrame()
    day_of_year = np.arange(1, pd.Timestamp(YEAR, 12, 31).dayofyear + 1)
    rent_daily = [np.random.poisson(3) for _ in range(pd.Timestamp(YEAR, 12, 31).dayofyear)]
    rentals_tbl["customer_id"] =  random.choices(customers, k = np.sum(rent_daily) )
    rentals_tbl["game_id"] = random.choices(range(1,GAMES_AMOUNT+1), k = np.sum(rent_daily) )
    rentals_tbl["rent_day"]= generate_list_with_occurrences(day_of_year, rent_daily)
    rentals_tbl["duration"] = np.random.poisson(3, rentals_tbl.shape[0]) + 1
    rentals_tbl["return_day"] = rentals_tbl["rent_day"] + rentals_tbl["duration"]
    rentals_tbl = rentals_tbl.sort_values(by = ["rent_day", "return_day"])
    rentals_tbl["rental_date"] = rentals_tbl.apply(lambda row: generate_date_from_day_number(row), axis=1)
    rentals_tbl["return_date"] = rentals_tbl.apply(lambda row: generate_return_date(row), axis=1)
    rentals_tbl.insert(0, "rental_id", np.arange(1, rentals_tbl.shape[0]+1))
    rentals_tbl["inventory_id"] = np.repeat(None, rentals_tbl.shape[0])
    rentals_tbl["employee_id"] = np.repeat(None, rentals_tbl.shape[0])
    rentals_tbl = simulate_inventory(rentals_tbl)
    return rentals_tbl

def generate_sales_tbl(customers_tbl, last_rent_inventory_id):
    sales_tbl = pd.DataFrame()
    day_of_year = np.arange(1, pd.Timestamp(YEAR, 12, 31).dayofyear + 1)
    sold_daily = [np.random.poisson(4) for _ in range(pd.Timestamp(YEAR, 12, 31).dayofyear)]
    sales_tbl["customer_id"] =  random.choices(customers_tbl["customer_id"].to_list(), k = np.sum(sold_daily) )
    sales_tbl["game_id"] = random.choices(range(1,GAMES_AMOUNT+1), k = np.sum(sold_daily) )
    sales_tbl["rent_day"]= generate_list_with_occurrences(day_of_year, sold_daily)
    sales_tbl["date"] = sales_tbl.apply(lambda row: generate_date_from_day_number(row), axis=1)
    sales_tbl = sales_tbl.drop("rent_day", axis = 1)
    sales_tbl["inventory_id"] = np.arange(last_rent_inventory_id + 1, sales_tbl.shape[0] + last_rent_inventory_id+1)
    sales_tbl.sort_values(["inventory_id"])
    return sales_tbl

def temp_rent_invent(rentals_tbl):
    temp_rent_invent = pd.DataFrame()
    temp_rent_invent["game_id"] = rentals_tbl["game_id"]
    temp_rent_invent["inventory_id"] = rentals_tbl["inventory_id"]
    temp_rent_invent["type"] = np.repeat("R", temp_rent_invent.shape[0])

    temp_rent_invent = temp_rent_invent.sort_values(["inventory_id"])
    temp_rent_invent.drop_duplicates(inplace=True)
    return temp_rent_invent

def temp_sales_invent(sales_tbl, last_rent_inventory_id):
    inventory_sales_tbl = pd.DataFrame()
    inventory_sales_tbl["game_id"] = sales_tbl["game_id"]
    inventory_sales_tbl["inventory_id"] = sales_tbl["inventory_id"]
    inventory_sales_tbl["type"] = np.repeat("B", inventory_sales_tbl.shape[0])
    return inventory_sales_tbl

def temp_tour_invent(tournament_games, temp_rent_inv, temp_sales_inv):
    inventory_tour_tbl = pd.DataFrame()
    inventory_tour_tbl["game_id"] = generate_list_with_occurrences(tournament_games, [8 for _ in range(12)])
    inventory_tour_tbl["inventory_id"] = np.arange(temp_rent_inv.shape[0] + temp_sales_inv.shape[0]+1, temp_rent_inv.shape[0] + temp_sales_inv.shape[0] + inventory_tour_tbl.shape[0] +1 )
    inventory_tour_tbl["type"] = np.repeat("T", inventory_tour_tbl.shape[0])
    return inventory_tour_tbl

def generate_inventory_tbl(temp_rent_inv, temp_sales_inv, temp_tour_inv):
    inventory_tbl = pd.concat([temp_rent_inv, temp_sales_inv, temp_tour_inv], axis = 0)
    return inventory_tbl

# names_lists = (eng_first_names, eng_last_names, pl_first_names_w, pl_first_names_m,pl_last_names_w, pl_last_names_m)
# games_tbl = generate_games_tbl(new_games_df)
# print(f"Games tbl:\n {games_tbl.head()}")
# proportions = np.array([0.4, 0.25, 0.35]) # ALL_ENG, W_PL, M_PL
# phone_numbers = generate_ALL_phone_numbers(CUSTOMERS_AMOUNT+EMPLOYEES_AMOUNT)
# customers_tbl = generate_customers_tbl(names_lists, proportions)
# print(f"Customers tbl:\n {customers_tbl.head()}")
# employees_tbl = generate_employees_tbl()
# print(f"Employyes tbl:\n {employees_tbl.head()}")
# termines_tbl = generate_termines_tbl()
# print(f"Termines tbl:\n {termines_tbl.head()}")
# tournament_games = random_games(games_tbl)
# tournaments_tbl = generate_tournaments_tbl(tournament_games)
# print(tournaments_tbl.head())
# results_tbl = generate_results_table(tournaments_tbl, customers_tbl)
# print(results_tbl.head())
# rentals_tbl = generate_rentals_tbl(customers_tbl["customer_id"])
# print(rentals_tbl.head())
# last_rent_inventory_id = len(np.unique(rentals_tbl["inventory_id"]))
# sales_tbl = generate_sales_tbl(last_rent_inventory_id)
# print(sales_tbl.head())

# temp_rent = temp_rent_invent(rentals_tbl)
# temp_sales =  temp_sales_invent(sales_tbl, last_rent_inventory_id)
# temp_tour =  temp_tour_invent(tournament_games, temp_rent, temp_sales)
# inventory_tbl = generate_inventory_tbl(temp_rent,temp_sales,temp_tour)
# print(inventory_tbl.head())


























