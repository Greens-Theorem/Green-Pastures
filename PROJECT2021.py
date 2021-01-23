# AUTHOR COWEN HAMES (Backend)
# AUTHOR EVAN CUNNINGHAM (Frontend)
# 1/22/21
# PROJECT 2021. This project creates a database and a single table in MySQL, then uses Python to pass the database information over to HTML to display the cheat codes for The Sims 3.
# FullStack Dev Project #1 (MySQL, Python, JS, HTML, CSS)

import mysql.connector
import pandas as pd
from pandas import DataFrame

# Create the database

def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password")
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE The_Sims_3_Cheats")

# create the table

def create_The_Sims_3_Table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE The_Sims_3 (id INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(50), Release_Year INT, Platform VARCHAR(50), Cheat_Code VARCHAR(100), Cheat_Code_Description VARCHAR(100))")

# populate the table

def populate_The_Sims_3_Table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cheat_data = [  (1, 'The Sims 3', 2009, 'PC', 'CNTRL + SHFT + C', 'Open Cheat Console'), 
                    (2, 'The Sims 3', 2009, 'PC', 'fullscreen on/off', 'Adjust the game screen'), 
                    (3, 'The Sims 3', 2009, 'PC', 'constrainFloorElevation true/false', 'Unrestrict Terrain adjustments'), 
                    (4, 'The Sims 3', 2009, 'PC', 'freerealestate', 'Buy any house'), 
                    (5, 'The Sims 3', 2009, 'PC', 'enableLlamas on/off', 'Llamas message'), 
                    (6,'The Sims 3', 2009, 'PC', 'jokePlease', 'Joke message'),
                    (7,'The Sims 3', 2009, 'PC', 'hideHeadlineEffects on/off', 'Hides all meters like the skill meter'), 
                    (8, 'The Sims 3', 2009, 'PC', 'quit', 'Quits the game'), 
                    (9, 'The Sims 3', 2009, 'PC', 'help', 'Help menu'),
                    (10, 'The Sims 3', 2009, 'PC', 'slowMotionViz <0 to 8>', 'Slow motion mode'), 
                    (11, 'The Sims 3', 2009, 'PC', 'ResetLifetimeHappiness', 'Reset sims happiness'),
                    (12, 'The Sims 3', 2009, 'PC', 'resetSim <firstname> <lastname>', 'Reset the Sims settings'),
                    (13, 'The Sims 3', 2009, 'PC', 'buydebug on/off', 'Display hidden items in buy mode after testingcheats is used'),
                    (14, 'The Sims 3', 2009, 'PC', 'fps on/off', 'Displays Frames per Second'),
                    (15, 'The Sims 3', 2009, 'PC', 'HideHeadlineEffects on/off', 'Modifies thought balloons'),
                    (16, 'The Sims 3', 2009, 'PC', 'fadeObjects on/off', 'Objects fade with camera zoom'),
                    (17, 'The Sims 3', 2009, 'PC', 'testingcheatsenabled true', 'Activate Testing cheats, shift click a Sim'),
                    (18, 'The Sims 3', 2009, 'PC', 'unlockOutfits on/off', 'Unlocks outfits in Create a Sim'),
                    (19, 'The Sims 3', 2009, 'PC', 'moveobjects on/off', 'Move anything including your Sim'),
                    (20, 'The Sims 3', 2009, 'PC', 'AlwaysAllowBuildBuy true/false', 'Modes are always available'),
                    (21, 'The Sims 3', 2009, 'PC', 'familyfunds <familys last name> <amount over 0>', 'Modify familys bank account balance to number set'),
                    (22, 'The Sims 3', 2009, 'PC', 'kaching', 'Gives $1000'),
                    (23, 'The Sims 3', 2009, 'PC', 'motherlode', 'Gives $50000')
                    ]
    cursor.executemany(
        'INSERT IGNORE into The_Sims_3 VALUES(%s, %s, %s, %s, %s, %s)', cheat_data)
    mydb.commit()

#print the tables data into a Pandas DataFrame to be sent to the HTML code
def print_sql_data_as_Pandas_DF():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    query = 'SELECT * FROM The_Sims_3'
    df = pd.read_sql(query, mydb)
    print(df)

#delete the table for debugging reasons if needed:

def clear_table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute('DROP TABLE The_Sims_3')
    verify = cursor.fetchall()
    print(verify)
    
# run main

def main():
    create_database()
    create_The_Sims_3_Table()
    populate_The_Sims_3_Table()
    print_sql_data_as_Pandas_DF()
    
if __name__ == '__main__':
    main()