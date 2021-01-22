# author Cowen Hames

#Program to create a database in MySQL, create two tables and populate those with data.

#Step 1: Change your host, user and password to your localhost mySQL info.
#Step 2: Create the Database
#Step 3: Create the Tables
#Step 4: Insert the data
#Step 5: Use SQL Statements to obtain the database information

import mysql.connector

def create_database():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password")
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE Vid_Game_Cheat_DB")

def create_game_table():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute("DROP TABLE IF EXISTS games")
    cursor.execute(
    "CREATE TABLE game_table (Title VARCHAR(50) PRIMARY KEY, release_year INT, gaming_platform VARCHAR(50))")
    
def create_cheat_table():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute(
    "CREATE TABLE cheat_table (Cheat VARCHAR(50) PRIMARY KEY, cheat_process VARCHAR (500), Title VARCHAR(50), FOREIGN KEY(Title) REFERENCES game_table(Title))")

def populate_game_table():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    sql_statement = "INSERT INTO game_table (Title, release_year, gaming_platform) VALUES ('The Sims 3', 2009, 'PC'),('The Last of Us Part II', 2020, 'PS4'),('GTA San Andreas', 2004, 'PS2')"
    cursor.execute(sql_statement)
    mydb.commit()

def populate_cheat_table():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    sql = "INSERT INTO cheat_table (Cheat, cheat_process, Title) VALUES ('Motherlode', 'Press CNTRL and SHFT and C to open the command menu while on lot. This code gives you $50000', 'The Sims 3')"
    cursor.execute(sql)
    mydb.commit()

def delete_from_game_table():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM game_table WHERE Title = 'value'")
    mydb.commit()


def delete_from_cheat_table():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM cheat_table WHERE Cheat = 'value'")
    mydb.commit()

def show_game_data():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM game_table")
    print(cursor.fetchall())

def show_cheat_data():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database = "Vid_Game_Cheat_DB")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM cheat_table")
    print(cursor.fetchall())