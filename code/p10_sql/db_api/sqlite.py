# Python DB API
import sqlite3
from sqlite3 import Error as DBError
import dill
from pprint import pprint

def create_connection_sqlite(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(f"Connection to {filename} created")
    except DBError as e:
        print("Error connecting to sqlite database:", e)
    return conn


def execute_query(connection, query, params=()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        # connection.commit()
        # print("Query executed successfully")
    except DBError as e:
        print("Error executing query:", e)
    

def execute_read_query(connection, query, params=()):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
        connection.commit()
        # print("Query executed successfully")
    except DBError as e:
        print("Error executing query:", e)
    return result


def deserialize(filename):
    with open(filename, 'rb') as f:
        return dill.load(f)



if __name__ == "__main__":
    data = deserialize("dns_ram_prices.dill")
    # pprint(data[0])
    conn = create_connection_sqlite("dns_ram.db")

    execute_query(conn, "DROP TABLE IF EXISTS dns_ram;")
    execute_query(conn, "DROP TABLE IF EXISTS ram_types;")

    create_types_table = """CREATE TABLE IF NOT EXISTS ram_types
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        , name TEXT NOT NULL
    );
    """

    create_ram_table = """CREATE TABLE IF NOT EXISTS dns_ram
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        , name TEXT NOT NULL
        , sku TEXT NOT NULL
        , m_qty INTEGER NOT NULL
        , m_size INTEGER NOT NULL
        , price REAL NOT NULL
        , type INTEGER NOT NULL
        , FOREIGN KEY (type) REFERENCES ram_types(id)
    );
    """

    execute_query(conn, create_types_table)
    execute_query(conn, create_ram_table)
    conn.commit()



    types = {}
    for row in data:
        types.update({row["type"]: 0})



    insert_query = "INSERT INTO ram_types (name) VALUES (?) RETURNING id;"
    for typ in types:
        types[typ] = execute_read_query(conn, insert_query, (typ,))[0][0]
    conn.commit()
    # print(types)
    # select_types = "SELECT * FROM ram_types;"
    # print(execute_read_query(conn, select_types))

    insert_ram = """INSERT INTO dns_ram
(name, sku, m_qty, m_size, price, type) VALUES 
(:name, :sku, :m_qty, :m_size, :price, :type)"""
    for row in data:
        row["type"] = types[row["type"]]
        execute_query(
            conn,
            insert_ram,
            row
        )
    conn.commit()