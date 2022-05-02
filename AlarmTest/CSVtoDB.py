import csv
import pandas as pd
import pyodbc

#find csv and import
data = pd.read_csv (r'C:\Users\ivyevere\Documents\Github\Amazon-Projects\AlarmTest\active.csv')
df = pd.DataFrame(data)
# print(df)

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DAL2-CND1231F88;'
    'Database=AlarmTest;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()
try:
    cursor.execute('''
		CREATE TABLE alarmTable (
			Number nvarchar(50) primary key,
			Event_Timestamp nvarchar(50),
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
    for row in df.itertuples():
        cursor.execute('''
                INSERT INTO alarmTable (Number, Event_Timestamp, Duration, Class, Location, Description, Tag)
                VALUES (?,?,?,?,?,?,?)
                ''',
                row.Number, 
                row.Event_Timestamp,
                row.Duration,
                row.Class,
                row.Location,
                row.Description,
                row.Tag
                )
conn.commit()