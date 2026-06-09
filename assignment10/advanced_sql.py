import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
        try:
            conn.execute("PRAGMA foreign_keys = 1") #turns on foreign key constraint
            cursor = conn.cursor()
            
            #Task 1
            task1 = cursor.execute("""
            SELECT orders.order_id,
            SUM(products.price * line_items.quantity)
            FROM orders
            JOIN line_items
                ON orders.order_id = line_items.order_id
            JOIN products
                ON products.product_id = line_items.product_id
            GROUP BY orders.order_id
            ORDER BY orders.order_id
            LIMIT 5;
            """)
            
            for row in task1:
                print(row)
            
        except sqlite3.Error: #Handle Ctrl-D (EOF) gracefully
            print("\nAn error has occurred...") 
        
        conn.close()