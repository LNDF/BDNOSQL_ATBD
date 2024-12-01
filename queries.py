import pymongo
import time

def time_execution(name):
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'Execution time ({name}): {end - start} seconds')
            return result
        return wrapped_func
    return wrapper

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://root:root@localhost:27017/')
db = client['football-female']
collection = db['players']

# Convert all player names to uppercase
@time_execution('uppercase')
def uppercase_names():
    for player in collection.find():
        collection.update_one(
            {'_id': player['_id']},
            {'$set': {'Player': player['Player'].upper()}}
        )
uppercase_names()

# Get the first player with start year greater than 2020 and print to console
@time_execution('start_year')
def get_players_start_year():
    player = collection.find_one({'Starting_Year': {'$gt': 2020}})
    if player:
        print(player)
get_players_start_year()

# Get the first player whose team name starts with 'Manchester' and print to console
@time_execution('team_name')
def get_players_team_name():
    player = collection.find_one({'Squad': {'$regex': '^Manchester', '$options': 'i'}})
    if player:
        print(player)
get_players_team_name()


# Get the country of the first player
@time_execution('first_player_country')
def get_country():
    player = collection.find_one()
    if player:
        print(player['Nation'])
get_country()
