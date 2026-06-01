import sqlite3

#Task 1 - create magazines database

# connect to SQLite database
with sqlite3.connect("../db/magazines.db") as conn:
    try:
        cursor = conn.cursor()
    except EOFError: #Handle Ctrl-D (EOF) gracefully
        print("\nExiting...") 
    except KeyboardInterrupt: #Handle Ctrl-C (Interrupt)
        print("\nCommand canceled.")
conn.close()
    