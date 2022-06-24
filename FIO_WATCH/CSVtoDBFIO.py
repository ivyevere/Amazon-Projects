import csv
import pandas as pd
import pyodbc

#find csv and import
data = pd.read_csv (r'C:\Users\ivyevere\Documents\Github\Amazon-Projects\FIO_WATCH\FIO.csv')
df = pd.DataFrame(data).fillna("")
# print(df)

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DAL2-CND1231F88;'
    'Database=FIO_WATCH;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()
try:
    cursor.execute('''
        CREATE TABLE FIO_TABLE (
            "Number (ID)" int,
            Start_Timestamp nvarchar(50),
            End_Timestamp nvarchar(50),
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
    for index, row in df.iterrows():
        cursor.execute('''
                INSERT INTO FIO_TABLE
                VALUES (?,?,?,?,?,?,?,?)
                ''',
                row["Number (ID)"],
                row["Start Timestamp"],
                row["End Timestamp"],
                row["Duration"],
                row["Class"],
                row["Location"],
                row["Description"],
                row["Tag"]
                )
                # print(row[2])
conn.commit()