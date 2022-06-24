import csv
import pandas as pd
import pyodbc

#find csv and import
data = pd.read_csv (r'C:\Users\ivyevere\Documents\Github\Amazon-Projects\AlarmTest\dataset_rbd5_gap.csv')
df = pd.DataFrame(data)
# print(df)

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DAL2-CND1231F88;'
    'Database=test_database;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()
try:
    cursor.execute('''
        CREATE TABLE gapTable (
            CartonIDS nvarchar(50),
            CartonNum nvarchar(50),
            Gap nvarchar(50),
            Length nvarchar(50),
            Barcode nvarchar(50),
            Timestamp nvarchar(50),
            Recirc nvarchar(50)
            )
               ''')
except:
    print("Table already created!")
finally:
    for row in df.itertuples():
        cursor.execute('''
                INSERT INTO gapTable (CartonIDS, CartonNum, Gap, Length, Barcode, Timestamp, Recirc)
                VALUES (?,?,?,?,?,?,?)
                ''',
                row.CartonIDS, 
                row.CartonNum,
                row.Gap,
                row.Length,
                row.Barcode,
                row.Timestamp,
                row.Recirc
                )
conn.commit()