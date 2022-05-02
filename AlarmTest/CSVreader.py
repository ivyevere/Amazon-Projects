import csv
import os
import sys

# with open(os.path.join(sys.path[0], 'active.csv'), newline='') as csvfile:
#     alarmList = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in alarmList:
#         print(', '.join(row))

# try:
#     with open('alarm.txt', 'w') as outputFile:

with open('alarm.txt', 'w') as outputFile:
    with open(os.path.join(sys.path[0], 'active.csv'), 'r') as inputFile:
        [outputFile.write(" ".join(row)+"\n") for row in csv.reader(inputFile)]
    outputFile.close()
