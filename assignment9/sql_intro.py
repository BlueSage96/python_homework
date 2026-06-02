import sqlite3

#Task 1 - create Magazines database
#Task 2 - create tables
#Task 3 - populate tables

#Functions for each table
def create_publisher(cursor, name, year):
    cursor.execute("SELECT * FROM Publisher WHERE name = ?",(name,)) #search db
    results = cursor.fetchall() #Get results
    try:
        if len(results) > 0:
            print("Publisher already exists!")
        else:
            cursor.execute("INSERT INTO Publisher (name, year) VALUES (?,?)",(name,year))    
    except sqlite3.IntegrityError:
        print(f"{name} already exist in the database!")

def create_magazine(cursor, name, year):
    cursor.execute("SELECT * FROM Magazines WHERE name = ?",(name,)) #search db
    results = cursor.fetchall() #Get results
    try:
        if len(results) > 0:
            print("Magazine already exists!")
        else:
            cursor.execute("INSERT INTO Magazines (name, year) VALUES (?,?)",(name,year))    
    except sqlite3.IntegrityError:
        print(f"{name} already exist in the database!")
        
def create_subscribers(cursor, name, year):
    cursor.execute("SELECT * FROM Subscribers WHERE name = ?",(name,)) #search db
    results = cursor.fetchall() #Get results
    try:
        if len(results) > 0:
            print("Subscribers already exists!")
        else:
            cursor.execute("INSERT INTO Subscribers (name, year) VALUES (?,?)",(name,year))    
    except sqlite3.IntegrityError:
        print(f"{name} already exist in the database!")
        
def create_subscriptions(cursor, subscriber_id, magazine_id, expiration_date):
    cursor.execute("SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?",(subscriber_id, magazine_id)) #search db

    results = cursor.fetchall() #Get results
    try:
        if len(results) > 0:
            print("Subscriber and/or magazine and already exists!")
        else:
            cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)",(subscriber_id, magazine_id, expiration_date))    
    except sqlite3.IntegrityError:
        print(f"Subscription already exist in the database!")

# connect to SQLite database
with sqlite3.connect("../db/Magazines.db") as conn:
    try:
        conn.execute("PRAGMA foreign_keys = 1") #turns on foreign key constraint
        cursor = conn.cursor()
        
        #create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publisher (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            year INTEGER
        )               
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            year INTEGER,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES Publisher (publisher_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )      
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            expiration_date STRING NOT NULL,
            magazine_id INTEGER,
            subscriber_id INTEGER,
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id)
        )       
        """)
        print("Table created successfully")
    except EOFError: #Handle Ctrl-D (EOF) gracefully
        print("\nExiting...") 
    except KeyboardInterrupt: #Handle Ctrl-C (Interrupt)
        print("\nCommand canceled.")
conn.close()
    