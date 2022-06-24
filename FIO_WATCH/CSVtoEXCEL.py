from cgi import test
import csv
import pandas as pd
import xlsxwriter

#--------------Find CSV and Import--------------#

data = pd.read_csv (r'C:\Users\ivyevere\Documents\Github\Amazon-Projects\FIO_WATCH\Latest.csv')
df = pd.DataFrame(data).fillna("")
df = df.drop(['Number (ID)', 'Class'], axis=1) #delete unused data

#--------------Find Jams--------------#

jamFault = df.loc[df["Description"] == 'Jammed']

if jamFault.empty == True:
    jamArea = "None"
    topJam = "N/A"
elif jamFault.empty == False:
    test_Jam_Location = jamFault['Tag']
    test_Jam_Location = test_Jam_Location.str.slice(start=1, stop=6)
    jamArea = test_Jam_Location.mode()
    jamArea = jamArea[0]

    topJam = jamFault['Location'].mode()
    nJams = jamFault['Location'].str.contains(topJam[0]).count()
    topJam = topJam[0] + ' (' + str(nJams) + ')'

#--------------Find IOFaults--------------#

ioFault = df.loc[df["Description"] == 'I/O Module Fault']

if ioFault.empty == True:
    ioArea = "None"
    topIO = "N/A"
elif ioFault.empty == False:
    io_Location = ioFault['Tag']
    io_Location = io_Location.str.slice(start=1, stop=6)
    ioArea = io_Location.mode()
    ioArea = ioArea[0]

    topIO = ioFault['Location'].mode()
    nIO = ioFault['Location'].str.contains(topIO[0]).count()
    topIO = topIO[0] + ' (' + str(nIO) + ')'

#--------------Find Estop Faults--------------#

eFault = df.loc[df["Description"] == 'Actuated']
if eFault.empty == True:
    eArea = "None"
    topEstop = "N/A"
elif eFault.empty == False:
    e_Location = eFault['Tag']
    e_Location = e_Location.str.slice(start=1, stop=6)
    eArea = e_Location.mode()
    eArea = eArea[0]
    topEstop = eFault['Location'].mode()
    n_Estop = eFault['Location'].str.contains(topEstop[0]).count()
    topEstop = topEstop[0] + ' (' + str(n_Estop) + ')'

#--------------Find VFD Faults--------------#

vFault = df.loc[df["Location"].str.contains('VFD')]
if vFault.empty == True:
    vArea = "None"
    topVFD_fault = "N/A"
elif vFault.empty == False:
    vfd_Location = vFault['Tag']
    vfd_Location = vfd_Location.str.slice(start=1, stop=6)
    vArea = vfd_Location.mode()
    vArea = vArea[0]
    topVFD_fault = vFault['Location'].mode()
    n_vfd_fault = vFault['Location'].str.contains(topVFD_fault[0]).count()
    topVFD_fault = topVFD_fault[0] + ' (' + str(n_vfd_fault) + ')'

#--------------Create New Dataframe--------------#

udf= pd.DataFrame({'Fault Type': ['Jammed', 'FIO Comm', 'E-stop', 'VFD_Fault', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6', 'Test7', 'Test8'],
                    'Total Faults': [jamFault.size, ioFault.size, eFault.size, vFault.size, 0, 0, 0, 0, 0, 0, 0, 0],
                    'Top Area': [jamArea, ioArea, eArea, vArea, 0, 0, 0, 0, 0, 0, 0, 0],
                    'Top Location (#)': [topJam, topIO, topEstop, topVFD_fault, 0, 0, 0, 0, 0, 0, 0, 0],
                    'Runner Up': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})
 
#--------------Output DF to Excel--------------#

writer = pd.ExcelWriter("ShiftReport6-22.xlsx", engine='xlsxwriter')
udf.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '0', 'align': 'Center'})

worksheet.set_column('A:E', 18, format2)

writer.save()

#--------------Old Code--------------#

# J_MCP01 = jamFault[jamFault['Tag'].str.contains('MCP01')].Location #old total jams