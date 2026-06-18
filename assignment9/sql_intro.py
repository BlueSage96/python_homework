import sqlite3

#Task 1 - create Magazines database
#Task 2 - create tables
#Task 3 - populate tables
#Task 4 - SQL Queries (below)
def main():
    #Task 3 - functions for each table
    def create_publishers (cursor, name, year):
        cursor.execute("SELECT * FROM publishers WHERE name = ?",(name,)) #search db
        results = cursor.fetchall() #Get results
        try:
            if len(results) > 0:
                print("Publisher already exists!")
            else:
                cursor.execute("INSERT INTO publishers (name, year) VALUES (?,?)",(name,year))    
        except sqlite3.IntegrityError:
            print(f"{name} already exist in the database!")

    def create_magazines (cursor, name, year, publisher_id):
        cursor.execute("SELECT * FROM magazines WHERE name = ?",(name,)) #search db
        results = cursor.fetchall() #Get results
        try:
            if len(results) > 0:
                print("Magazine already exists!")
            else:
                cursor.execute("INSERT INTO magazines (name, year,publisher_id) VALUES (?,?,?)",(name,year,publisher_id))    
        except sqlite3.IntegrityError:
            print(f"{name} already exist in the database!")
            
    def create_subscribers (cursor, name, address):
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?",(name,address)) #search db
        results = cursor.fetchall() #Get results
        try:
            if len(results) > 0:
                print("Subscriber already exists!")
            else:
                cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)",(name,address))    
        except sqlite3.IntegrityError:
            print(f"{name} already exist in the database!")
            
    def create_subscriptions (cursor, subscriber_id, magazine_id, expiration_date):
        cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",(subscriber_id, magazine_id)) #search db

        results = cursor.fetchall() #Get results
        try:
            if len(results) > 0:
                print("Subscriber and/or magazine and already exists!")
            else:
                cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)",(subscriber_id, magazine_id, expiration_date))    
        except sqlite3.IntegrityError:
            print(f"Subscription already exist in the database!")

    # connect to SQLite database
    with sqlite3.connect("../db/magazines.db") as conn:
        try:
            conn.execute("PRAGMA foreign_keys = 1") #turns on foreign key constraint
            cursor = conn.cursor()
            
            #Task 2 - create tables
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                year INTEGER
            )               
            """)
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                year INTEGER,
                publisher_id INTEGER,
                FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            )
            """)
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )      
            """)
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER,
                magazine_id INTEGER,
                expiration_date STRING NOT NULL,
                FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
                FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id)
            )       
            """)
            print("Table created successfully")
            
        except sqlite3.Error: #Handle Ctrl-D (EOF) gracefully
            print("\nAn error has occurred...") 
            
        #Task 3 
        #Create publishers
        create_publishers(cursor, "Times", 2009)
        create_publishers(cursor,"Life", 2012)
        create_publishers(cursor, "New York Times", 1928)
        
        #Create magazines
        create_magazines(cursor,"Smithsonian",1996, publisher_id = 1)
        create_magazines(cursor,"National Geographic",1977, publisher_id = 3)
        create_magazines(cursor, "Rolling Stone", 1963, publisher_id = 2)
        
        #Create subscribers
        create_subscribers(cursor, "Jonah", "123 Raspberry Lane")
        create_subscribers(cursor, "Camille", "456 Kitty Street")
        create_subscribers(cursor, "Derek", "789 Indigo Boulevard")
        
        #Create subscriptions
        create_subscriptions(cursor, subscriber_id = 2, magazine_id = 1, expiration_date = "07/08/2027")
        create_subscriptions(cursor, subscriber_id = 3, magazine_id = 2, expiration_date = "03/08/2034")
        create_subscriptions(cursor, subscriber_id = 1, magazine_id = 3, expiration_date = "01/05/2031")
        
        #Task 4
        # 1.
        cursor.execute("SELECT * FROM subscribers")
        rows = cursor.fetchall()
        for row in rows:
            print(f"All subscribers: {row}")
            
        # 2.
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Order magazines: {row}")
            
        # 3.
        cursor.execute("SELECT * FROM magazines INNER JOIN publishers ON magazines.publisher_id = publishers.publisher_id WHERE publishers.name = 'New York Times'")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Publisher: {row}")
            
        conn.commit()
        
if __name__ == "__main__":
    main()