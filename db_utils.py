import sqlite3
from sqlite3 import Error

records_table_query = """
CREATE TABLE IF NOT EXISTS records (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  timestamp INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total_time INTEGER NOT NULL,
  avg_time INTEGER NOT NULL,
  times TEXT,
  n_exercises INTEGER,
  n_correct INTEGER,
  n_incorrect INTEGER,
  notes TEXT
);
"""


def create_connection(path):
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    return 0


def create_records_table(connection):
    execute_query(connection, records_table_query)


def add_record(connection, record):
    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO records (total_time, avg_time, times, n_exercises, n_correct, n_incorrect, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, record)
        connection.commit()
        print(f"Record '{record}' added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def select_all_records(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM records")
    return cursor.fetchall()


if __name__ == '__main__':
    connection = create_connection("sem_app.sqlite")
    create_records_table(connection)
    add_record(connection, (100, 50, '100, 50, 75', 3, 3, 0, 'good'))
    print(select_all_records(connection))
