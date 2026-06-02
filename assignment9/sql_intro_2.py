#Task 5

import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """ SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, products.product_name, price FROM line_items JOIN products ON line_items.product_id = products.product_id"""
    df = pd.read_sql_query(sql_statement,conn)
    print("SQL:\n",df.head(5))
    
    lesson = pd.DataFrame(df)
    lesson['total'] = lesson['quantity'] * lesson['price']
    print("Total:\n",lesson.head(5))
    
    lesson.groupby('product_id')["line_item_id"].count()
    print("Groupby:\n", lesson.head(5))
    
    lesson.sort_values(by="product_name")
    lesson.to_csv("order_summary.csv",index=False)