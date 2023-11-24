# Python DB API
import sqlite3
from sqlite3 import Error as DBError
import dill

def create_connection_sqlite(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(f"Connection to {filename} created")
    except DBError as e:
        print("Error connecting to sqlite database:", e)
    return conn


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except DBError as e:
        print("Error executing query:", e)
    

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        print("Query executed successfully")
    except DBError as e:
        print("Error executing query:", e)
    return result


def deserialize(filename):
    with open(filename, 'rb') as f:
        return dill.load(f)
# create_connection_sqlite("dummy.db")




if __name__ == "__main__":
    data = deserialize("dns_ram_prices.dill")
    print(data[0])