import sqlite3


def initDB():
    try:
        connection = sqlite3.connect('./data/database.db')
        with open('schema.sql') as f:
            connection.executescript(f.read())
        cur = connection.cursor()
        cur.execute("INSERT INTO products (productname, brand,category,stockstatus,store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('Iphone', 'Apple', 'Mobile Phones','In Stock', 'Grover-de', 10)
                    )
        cur.execute("INSERT INTO products (productname, brand,category, stockstatus, store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('IPad', 'Apple', 'Mobile Tablet', 'In Stock', 'Grover-de',15)
                    )
        cur.execute("INSERT INTO products (productname, brand,category, stockstatus, store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('Pixel4', 'Google', 'Mobile Phones','Out of Stock', 'Grover-de', 0)
                    )
        cur.execute("INSERT INTO products (productname, brand,category,stockstatus,store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('Galaxy A5', 'Samsung', 'Mobile Phones','In Stock', 'Grover-de', 10)
                    )
        cur.execute("INSERT INTO products (productname, brand,category,stockstatus,store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('Iphone', 'Apple', 'Mobile Phones','In Stock', 'mm-berlin', 10)
                    )
        cur.execute("INSERT INTO products (productname, brand,category, stockstatus, store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('IPad', 'Apple', 'Mobile Tablet', 'In Stock', 'mm-berlin',15)
                    )
        cur.execute("INSERT INTO products (productname, brand,category, stockstatus, store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('Pixel4', 'Google', 'Mobile Phones','Out of Stock', 'mm-berlin', 0)
                    )
        cur.execute("INSERT INTO products (productname, brand,category,stockstatus,store,quantity) VALUES (?, ?, ?, ?, ?,?)",
                    ('Galaxy A5', 'Samsung', 'Mobile Phones','Out of Stock', 'mm-berlin', 0)
                    )

        connection.commit()
        connection.close()
    except:
        print("Ignore this as this is POC")
