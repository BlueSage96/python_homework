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
                print(f"Task 1: {row} \n")
            
            #Task 2
            task2 = cursor.execute("""
                  SELECT customer_name, average_price
                  FROM customers
                  LEFT JOIN (    
                        SELECT  orders.customer_id as customer_id_b,
                                avg(c.total_price) as average_price
                        FROM    orders
                        LEFT JOIN (
                                SELECT      line_items.order_id,
                                            sum(products.price*line_items.quantity) as total_price
                                FROM        products
                                LEFT JOIN   line_items
                                ON          products.product_id = line_items.product_id 
                                GROUP BY    line_items.order_id
                        ) as c
                        ON orders.order_id = c.order_id
                        GROUP BY orders.customer_id
                        ORDER BY orders.customer_id
                   ) as b
                 ON customers.customer_id = b.customer_id_b;                 
            """)
            for row in task2:
                print(f"Task 2: {row} \n")
            
            customer = cursor.execute("""
                SELECT customer_id, customer_name
                FROM   customers
                WHERE  customer_name = 'Perez and Sons'
                
            """).fetchone() #only need one customer
            
            products = cursor.execute("""
                SELECT product_id, price
                FROM    products
                ORDER BY price
                LIMIT 5                      
            """).fetchall()
                 
            employee = cursor.execute("""
                  SELECT employee_id, first_name, last_name
                  FROM   employees
                  WHERE first_name = 'Miranda' AND last_name = 'Harris'                      
            """).fetchone()
            

            order = cursor.execute("""
                INSERT INTO orders
                (customer_id, employee_id)
                VALUES (?, ?)
                RETURNING order_id

            """, (customer[0], employee[0]))

            order_id = order.fetchone()[0]
            
            for product in products:
                cursor.execute("""
                    INSERT INTO line_items
                    (order_id, product_id, quantity)
                    VALUES (?, ?, ?)
                """, (order_id, product[0], 10))

            task3 = cursor.execute("""
                SELECT line_items.line_item_id,
                    line_items.quantity,
                    products.product_name
                FROM line_items
                JOIN products
                    ON line_items.product_id = products.product_id
                WHERE line_items.order_id = ?
            """, (order_id,))
            
            for row in task3:
                print(f"Task 3: {row} \n")
                
            task4 = cursor.execute("""
                 SELECT first_name, last_name, employees.employee_id, count(order_id) as all_orders
                FROM employees
                JOIN  orders ON employees.employee_id = orders.employee_id
                GROUP BY employees.employee_id
                HAVING all_orders > 5                  
            """)
            
            for row in task4:
                print(f"Task 4: {row}")
                
        except sqlite3.Error as e:
            print(f"\nSQLite error: {e}")