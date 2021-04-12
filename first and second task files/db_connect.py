import sqlite3 as sqlt
from pathlib import Path
import pandas as pd

# Creating the database
Path('data/test.db').touch()

# Connecting to db
connect = sqlt.connect("data/test.db")

# Creating the table with data that were in csv-file
cursor = connect.cursor()
cursor.execute('''CREATE TABLE tests ('device type' TEXT, operator text, time int, success int)''')


# Creating new csv-file
results = pd.read_csv('test_results.csv')
results.to_sql('tests', connect, if_exists='append', index=False)
# Placing that only created table in the csv-file
connect.execute('''SELECT * from tests''').fetchall()

# Finishing the current connection with db
connect.commit()
connect.close()
