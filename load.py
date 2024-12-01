import pandas as pd
import pymongo

def create_document(record):
    return {
        "Player": record["Player"],
        "Nation": record["Nation"],
        "Position": record["Pos"],
        "Squad": record["Squad"],
        "Age": record["Age"],
        "Born": record["Born"],
        "Starting_Year": record["Start_Year"],
        
        "Match_Stats": {
            "Matches_Played": record["MP"],
            "Matches_Started": record["Starts"],
            "Minutes_Played": record["Min"],
            "Goals": record["Gls"],
            "Assists": record["Ast"]
        },
        
        "Performance_Stats": {
            "Expected_Goals": record["xG"],
            "Expected_Assists": record["xAG"],
            "Shots": record["Sh"],
            "Shots_on_Target": record["SoT"],
            "Dribbles_Successful": record["Dribbles_Succ"],
            "Dribbles_Attempted": record["Dribbles_Att"]
        },
        
        "Passing_Stats": {
            "Total_Passes_Completed": record["Total_Cmp"],
            "Total_Passes_Attempted": record["Total_Att"],
            "Key_Passes": record["KP"],
            "Passes_into_Penalty_Area": record["PPA"]
        },
        
        "Defensive_Stats": {
            "Tackles": record["Tackles_Tkl"],
            "Interceptions": record["Int"],
            "Blocks": record["Blocks_Blocks"],
            "Ball_Recovery": record["Recov"],
            "Aerial_Duels_Won": record["AerialDuels_Won"],
            "Aerial_Duels_Lost": record["AerialDuels_Lost"]
        }
    }

# Load data
data = pd.read_csv('all_players.csv')

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://root:root@localhost:27017/')
db = client['football-female']
collection = db['players']

# Drop collection
collection.drop()

# Insert data
documents = data.head(100).apply(create_document, axis=1).to_list()
collection.insert_many(documents)
