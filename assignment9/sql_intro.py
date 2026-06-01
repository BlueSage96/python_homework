import sqlite3

#Task 1 - create magazines database
#Task 2 - create tables

# connect to SQLite database
with sqlite3.connect("../db/magazines.db") as conn:
    try:
        cursor = conn.cursor()
        #SELECT Students.name, Courses.course_name 
        # FROM Enrollments
        # JOIN Students ON Enrollments.student_id = Students.student_id
        # JOIN Courses ON Enrollments.course_id = Courses.course_id;
        
        #create tables
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
            FOREIGN KEY (publisher_id) REFERENCES subscribers (publisher_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL UNIQUE
        )      
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            expiration_date STRING NOT NULL UNIQUE,
            magazine_id INTEGER,
            subscriber_id INTEGER,
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id)
        )       
        """)
        print("Table created successfully")
    except EOFError: #Handle Ctrl-D (EOF) gracefully
        print("\nExiting...") 
    except KeyboardInterrupt: #Handle Ctrl-C (Interrupt)
        print("\nCommand canceled.")
conn.close()
    