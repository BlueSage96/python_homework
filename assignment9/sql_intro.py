import sqlite3

#Task 1 - create Magazines database
#Task 2 - create tables
#Task 3 - populate tables

def main():
    #Functions for each table
    def create_publisher (cursor, name, year):
        cursor.execute("SELECT * FROM Publisher WHERE name = ?",(name,)) #search db
        results = cursor.fetchall() #Get results
        try:
            if len(results) > 0:
                print("Publisher already exists!")
            else:
                cursor.execute("INSERT INTO Publisher (name, year) VALUES (?,?)",(name,year))    
        except sqlite3.IntegrityError:
            print(f"{name} already exist in the database!")

    def create_magazine (cursor, name, year, publisher_id):
        cursor.execute("SELECT * FROM Magazines WHERE name = ?",(name,)) #search db
        results = cursor.fetchall() #Get results
        try:
            if len(results) > 0:
                print("Magazine already exists!")
            else:
                cursor.execute("INSERT INTO Magazines (name, year,publisher_id) VALUES (?,?,?)",(name,year,publisher_id))    
        except sqlite3.IntegrityError:
            print(f"{name} already exist in the database!")
            
    def create_subscriber (cursor, name, address):
        cursor.execute("SELECT * FROM Subscribers WHERE name = ? AND address = ?",(name,address)) #search db
        results = cursor.fetchall() #Get results
        try:
            if len(results) > 0:
                print("Subscriber already exists!")
            else:
                cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)",(name,address))    
        except sqlite3.IntegrityError:
            print(f"{name} already exist in the database!")
            
    def create_subscription (cursor, subscriber_id, magazine_id, expiration_date):
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
                subscriber_id INTEGER,
                magazine_id INTEGER,
                expiration_date STRING NOT NULL,
                FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
                FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id)
            )       
            """)
            print("Table created successfully")
            
        except EOFError: #Handle Ctrl-D (EOF) gracefully
            print("\nExiting...") 
        except KeyboardInterrupt: #Handle Ctrl-C (Interrupt)
            print("\nCommand canceled.")
            
        # #Create publishers
        create_publisher(cursor, "Times", 2009)
        create_publisher(cursor,"Life", 2012)
        create_publisher(cursor, "New York Times", 1928)
        
        #Create magazines
        create_magazine(cursor,"Smithsonian",1996, publisher_id = 1)
        create_magazine(cursor,"National Geographic",1977, publisher_id = 3)
        create_magazine(cursor, "Rolling Stone", 1963, publisher_id = 2)
        
        #Create subscribers
        create_subscriber(cursor, "Jonah", "123 Raspberry Lane")
        create_subscriber(cursor, "Camille", "456 Kitty Street")
        create_subscriber(cursor, "Derek", "789 Indigo Boulevard")
        
        #Create subscriptions
        create_subscription(cursor, subscriber_id = 2, magazine_id = 1, expiration_date = "07/08/2027")
        create_subscription(cursor, subscriber_id = 3, magazine_id = 2, expiration_date = "03/08/2034")
        create_subscription(cursor, subscriber_id = 1, magazine_id = 3, expiration_date = "01/05/2031")
        conn.commit()
        
if __name__ == "__main__":
    main()