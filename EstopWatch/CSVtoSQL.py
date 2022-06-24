import csv
import pandas as pd
import pyodbc

#find csv and import
data = pd.read_csv (r'C:\Users\ivyevere\Documents\Github\Amazon-Projects\EstopWatch\estop.csv')
df = pd.DataFrame(data)
# print(df)

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DAL2-CND1231F88;'
    'Database=estop_database;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()
try:
    cursor.execute('''
        CREATE TABLE EstopTable (
            Number nvarchar(50),
            Start_Time nvarchar(50),
            End_Time nvarchar(50),
            Duration nvarchar(50),
            Class nvarchar(50),
            Location nvarchar(50),
            Description nvarchar(50),
            Tag nvarchar(50)
            )
               ''')
except:
    print("Table already created!")
finally:
    print(df.info())
    print (data.columns)
    for row in df.iterrows():
        cursor.execute('''
                INSERT INTO EstopTable
                VALUES (?,?,?,?,?,?,?,?)
                ''',
                row["Number"],
                row["Start Timestamp"],
                row["End Times"],
                row["Duration"],
                row["Class"],
                row["Location"],
                row["Description"],
                row["Tag"]
                )
conn.commit()