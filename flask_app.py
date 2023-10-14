from flask import Flask, render_template, request, redirect
import sqlite3
from helpers import get_data, insert_data, delete_data

app = Flask(__name__)

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db')

# Create a cursor object
cur = conn.cursor()

# Create the `data` table if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT
)''')

# Close the cursor object
cur.close()

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()

# Define a route to display the data in the database
@app.route('/', methods=['GET', 'POST'])
def index():
    data = get_data()
    # Create a connection to the SQLite database
    conn = sqlite3.connect('database.db')

    # Create a cursor object
    cur = conn.cursor()

    # Query the database for all rows in the `data` table
    cur.execute('SELECT * FROM data')

    # Get the results of the query
    data = cur.fetchall()

    # Close the cursor object
    cur.close()

    # Close the connection to the database
    conn.close()

    if request.method == 'POST':
        # Create a connection to the SQLite database
        conn = sqlite3.connect('database.db')

        # Create a cursor object
        cur = conn.cursor()

        # Get the data from the request form
        data = request.form['data']

        # Insert the data into the `data` table
        cur.execute('INSERT INTO data (data) VALUES (?)', (data,))

        # Commit the changes to the database
        conn.commit()

        # Close the cursor object
        cur.close()

        # Close the connection to the database
        conn.close()

        # Redirect the user back to the main page
        return redirect('/')

    # Render the index.html template with the data from the database
    return render_template('index.html', data=data)

# Define a route to add a new row to the database
@app.route('/add', methods=['POST'])
def add():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('database.db')

    # Create a cursor object
    cur = conn.cursor()

    # Get the data from the request form
    data = request.form['data']

    # Insert the data into the `data` table
    cur.execute('INSERT INTO data (data) VALUES (?)', (data,))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor object
    cur.close()

    # Close the connection to the database
    conn.close()

    # Redirect the user back to the main page
    return redirect('/')

# Define a route to delete a row from the database
@app.route('/delete/<int:id>')
def delete(id):
    # Create a connection to the SQLite database
    conn = sqlite3.connect('database.db')

    # Create a cursor object
    cur = conn.cursor()

    # Delete the row with the specified ID from the `data` table
    cur.execute('DELETE FROM data WHERE id = ?', (id,))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor object
    cur.close()

    # Close the connection to the database
    conn.close()

    # Redirect the user back to the main page
    return redirect('/')


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
