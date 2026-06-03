#Task 5

import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """ SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, products.product_name, price FROM line_items JOIN products ON line_items.product_id = products.product_id"""
    df = pd.read_sql_query(sql_statement,conn)
    print("SQL:\n",df.head(5))
    
    summary = pd.DataFrame(df)
    summary['total'] = summary['quantity'] * summary['price']
    print("Total:\n",summary.head(5))
    
    grouped = summary.groupby('product_id').agg({"line_item_id":"count","total":"sum","product_name":"first"})
    print("Groupby:\n", grouped.head(5))
    
    grouped.sort_values(by="product_name",inplace=True)
    grouped.to_csv("order_summary.csv",index=False)