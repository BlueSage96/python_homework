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
                print(f"Task 1: {row}")
            
            #Task 2
            task2 = cursor.execute("""
                  select customer_name, average_price
                  from customers
                  left join (    
                        select  orders.customer_id as customer_id_b,
                                avg(c.total_price) as average_price
                        from    orders
                        left join (
                                select      line_items.order_id,
                                            sum(products.price*line_items.quantity) as total_price
                                from        products
                                left join   line_items
                                on          products.product_id = line_items.product_id 
                                group by    line_items.order_id
                        ) as c
                        on orders.order_id = c.order_id
                        group by orders.customer_id
                        order by orders.customer_id
                   ) as b
                 on customers.customer_id = b.customer_id_b;                 
            """)
            for row in task2:
                print(f"Task 2: {row}")
                
        except sqlite3.Error as e:
            print(f"\nSQLite error: {e}")