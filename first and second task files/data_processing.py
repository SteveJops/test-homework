import pandas as pd
import sqlite3

connect = sqlite3.connect("data/test.db")

# Getting whole the table from database which I`ve made before
data = pd.read_sql("SELECT * FROM tests", connect)


# Functions with filter`s conditions
def successful(x):
    return (x > 0).sum()


def unsuccessful(x):
    return (x == 0).sum()


def allTheTests(x):
    return x.count()


# It`s showing the result with the added filter with special conditions
data_frame = data.pivot_table(index=['device type'], values='success',
                              aggfunc={allTheTests, unsuccessful, successful}).reset_index()

print(data_frame)

# All the tests are with their operators

data_frame1 = data.pivot_table(index=['device type', 'operator'], values='success',
                               aggfunc={allTheTests, unsuccessful, successful}).reset_index()

print(data_frame1)

connect.commit()
connect.close()
