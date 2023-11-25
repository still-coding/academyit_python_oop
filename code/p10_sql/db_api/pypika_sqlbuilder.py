import sqlite3
from sqlite3 import Error as DBError
from pprint import pprint
from pypika import Table, Query, Column, Parameter, CustomFunction, Order


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


if __name__ == "__main__":
    conn = create_connection_sqlite("dns_ram.db")

    dns_ram = Table("dns_ram")
    ram_types = Table("ram_types")
    q = Query.from_(dns_ram).join(ram_types).on(dns_ram.type == ram_types.id).select(
        dns_ram.sku,
        ram_types.name,
        dns_ram.price
    ).orderby(dns_ram.price, order=Order.desc).limit(12)
    print(q)

    result = execute_read_query(conn, str(q))
    for r in result:
        pprint(r)
