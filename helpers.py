import sqlite3

def get_data():

    # Create a connection to the SQLite database
    conn = sqlite3.connect('database.db')

    # Create a cursor object
    cur = conn.cursor()

    cur.execute(f"""
        SELECT *
        FROM data
        ORDER BY rowid DESC
        LIMIT 1;
    """)

    row = cur.fetchone()

    conn.close()

    return row