# Python DB API
import psycopg
from psycopg import OperationalError as DBError
import dill
from pprint import pprint

def create_connection_postgres(db_name, db_user, db_password, db_host, db_port):
    conn = None
    try:
        conn = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print(f"Connection to {db_name} created")
    except DBError as e:
        print("Error connecting to PG database:", e)
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
    conn = create_connection_postgres("ram", 'ivan', 'fK5o2GnrmJN1BmrlQ7Ao', '192.168.2.2', 5433)

    execute_query(conn, "DROP TABLE IF EXISTS dns_ram;")
    execute_query(conn, "DROP TABLE IF EXISTS ram_types;")

    create_types_table = """CREATE TABLE IF NOT EXISTS ram_types
    (
        id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY
        , name TEXT NOT NULL
    );
    """

    create_ram_table = """CREATE TABLE IF NOT EXISTS dns_ram
    (
        id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY
        , name TEXT NOT NULL
        , sku TEXT NOT NULL
        , m_qty INTEGER NOT NULL
        , m_size INTEGER NOT NULL
        , price numeric(8, 2) NOT NULL
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



    insert_query = "INSERT INTO ram_types (name) VALUES (%s) RETURNING id;"
    for typ in types:
        types[typ] = execute_read_query(conn, insert_query, (typ,))[0][0]
    conn.commit()
    # print(types)
    # select_types = "SELECT * FROM ram_types;"
    # print(execute_read_query(conn, select_types))

    insert_ram = """INSERT INTO dns_ram
(name, sku, m_qty, m_size, price, type) VALUES 
(%(name)s, %(sku)s, %(m_qty)s, %(m_size)s, %(price)s, %(type)s)"""
    for row in data:
        row["type"] = types[row["type"]]
        execute_query(
            conn,
            insert_ram,
            row
        )
    conn.commit()