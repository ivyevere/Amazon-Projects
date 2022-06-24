from cgi import test
import csv
import pandas as pd
from webhook import chimeAlert

#--------------Find CSV and Import--------------#

data = pd.read_csv (r'C:\Users\ivyevere\Documents\Github\Amazon-Projects\FIO_WATCH\Latest.csv')
df = pd.DataFrame(data).fillna("")
df = df.drop(['Number (ID)', 'Class'], axis=1) #delete unused data

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
    topIO = topIO[0]

#--------------Send to Chime--------------#

msg = topIO + ' has faulted ' + str(nIO) + ' times!'

chimeAlert(msg)