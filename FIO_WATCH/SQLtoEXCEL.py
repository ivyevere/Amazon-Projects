import pyodbc
import pandas as pd

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DAL2-CND1231F88;'
    'Database=FIO_WATCH;'
    'Trusted_Connection=yes;'
)

df = pd.read_sql("SELECT * FROM FIO_TABLE", conn)

df = df.drop(['Number (ID)', 'Class'], axis=1) #delete unused data

jamFault = df.loc[df["Description"] == 'Jammed'] #Find Jams for MCPs

J_MCP01 = jamFault[jamFault['Tag'].str.contains('MCP01')].Location
J_MCP02 = jamFault[jamFault['Tag'].str.contains('MCP02')].Location
J_MCP03 = jamFault[jamFault['Tag'].str.contains('MCP03')].Location
J_MCP04 = jamFault[jamFault['Tag'].str.contains('MCP04')].Location
J_MCP05 = jamFault[jamFault['Tag'].str.contains('MCP05')].Location
J_MCP06 = jamFault[jamFault['Tag'].str.contains('MCP06')].Location
J_MCP07 = jamFault[jamFault['Tag'].str.contains('MCP07')].Location
J_MCP08 = jamFault[jamFault['Tag'].str.contains('MCP08')].Location
J_MCP09 = jamFault[jamFault['Tag'].str.contains('MCP09')].Location
J_MCP11 = jamFault[jamFault['Tag'].str.contains('MCP11')].Location
J_MCP20 = jamFault[jamFault['Tag'].str.contains('MCP20')].Location
J_MCP21 = jamFault[jamFault['Tag'].str.contains('MCP21')].Location

ioFault = df.loc[df["Description"] == 'I/O Module Fault'] #Find IOFaults for MCPs

F_MCP01 = ioFault[ioFault['Tag'].str.contains('MCP01')].Location
F_MCP02 = ioFault[ioFault['Tag'].str.contains('MCP02')].Location
F_MCP03 = ioFault[ioFault['Tag'].str.contains('MCP03')].Location
F_MCP04 = ioFault[ioFault['Tag'].str.contains('MCP04')].Location
F_MCP05 = ioFault[ioFault['Tag'].str.contains('MCP05')].Location
F_MCP06 = ioFault[ioFault['Tag'].str.contains('MCP06')].Location
F_MCP07 = ioFault[ioFault['Tag'].str.contains('MCP07')].Location
F_MCP08 = ioFault[ioFault['Tag'].str.contains('MCP08')].Location
F_MCP09 = ioFault[ioFault['Tag'].str.contains('MCP09')].Location
F_MCP11 = ioFault[ioFault['Tag'].str.contains('MCP11')].Location
F_MCP20 = ioFault[ioFault['Tag'].str.contains('MCP20')].Location
F_MCP21 = ioFault[ioFault['Tag'].str.contains('MCP21')].Location

eFault = df.loc[df["Description"] == 'Actuated'] #Find Estop faults for MCPs

e_MCP01 = eFault[eFault['Tag'].str.contains('MCP01')].Location
e_MCP02 = eFault[eFault['Tag'].str.contains('MCP02')].Location
e_MCP03 = eFault[eFault['Tag'].str.contains('MCP03')].Location
e_MCP04 = eFault[eFault['Tag'].str.contains('MCP04')].Location
e_MCP05 = eFault[eFault['Tag'].str.contains('MCP05')].Location
e_MCP06 = eFault[eFault['Tag'].str.contains('MCP06')].Location
e_MCP07 = eFault[eFault['Tag'].str.contains('MCP07')].Location
e_MCP08 = eFault[eFault['Tag'].str.contains('MCP08')].Location
e_MCP09 = eFault[eFault['Tag'].str.contains('MCP09')].Location
e_MCP11 = eFault[eFault['Tag'].str.contains('MCP11')].Location
e_MCP20 = eFault[eFault['Tag'].str.contains('MCP20')].Location
e_MCP21 = eFault[eFault['Tag'].str.contains('MCP21')].Location


T_MCP01 = J_MCP01.size + F_MCP01.size + e_MCP01.size #Find total of all faults
T_MCP02 = J_MCP02.size + F_MCP02.size + e_MCP02.size
T_MCP03 = J_MCP03.size + F_MCP03.size + e_MCP03.size
T_MCP04 = J_MCP04.size + F_MCP04.size + e_MCP04.size
T_MCP05 = J_MCP05.size + F_MCP05.size + e_MCP05.size
T_MCP06 = J_MCP06.size + F_MCP06.size + e_MCP06.size
T_MCP07 = J_MCP07.size + F_MCP07.size + e_MCP07.size
T_MCP08 = J_MCP08.size + F_MCP08.size + e_MCP08.size
T_MCP09 = J_MCP09.size + F_MCP09.size + e_MCP09.size
T_MCP11 = J_MCP11.size + F_MCP11.size + e_MCP11.size
T_MCP20 = J_MCP20.size + F_MCP20.size + e_MCP20.size
T_MCP21 = J_MCP21.size + F_MCP21.size + e_MCP21.size


udf= pd.DataFrame({'MCPXX': ['MCP01', 'MCP02', 'MCP03', 'MCP04', 'MCP05', 'MCP06', 'MCP07', 'MCP08', 'MCP09', 'MCP11', 'MCP20', 'MCP21'],
                    'Total Faults': [T_MCP01, T_MCP02, T_MCP03, T_MCP04, T_MCP05, T_MCP06, T_MCP07, T_MCP08, T_MCP09, T_MCP11, T_MCP20, T_MCP21],
                    'Total Jams': [J_MCP01.size, J_MCP02.size, J_MCP03.size, J_MCP04.size, J_MCP05.size, J_MCP06.size, J_MCP07.size, J_MCP08.size, J_MCP09.size, J_MCP11.size, J_MCP20.size, J_MCP21.size],
                    'FIO Faults': [F_MCP01.size, F_MCP02.size, F_MCP03.size, F_MCP04.size, F_MCP05.size, F_MCP06.size, F_MCP07.size, F_MCP08.size, F_MCP09.size, F_MCP11.size, F_MCP20.size, F_MCP21.size],
                    'Estop Faults': [e_MCP01.size, e_MCP02.size, e_MCP03.size, e_MCP04.size, e_MCP05.size, e_MCP06.size, e_MCP07.size, e_MCP08.size, e_MCP09.size, e_MCP11.size, e_MCP20.size, e_MCP21.size]})

print(udf)

# udf.to_excel('test.xlsx', index=False)