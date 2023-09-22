#for csv files operation
import csv
from openpyxl import load_workbook

#database handling
from sqlite3 import *

#for youtube data scraping



#-----------extracting dataset------------------
def csv_datasheet():
    wb = load_workbook(filename='CONTENT  SHEET__GYAAN CONNECT.xlsx')

    sheet = wb.active

    csv_data = []

    for value in sheet.iter_rows(values_only = True):
        csv_data.append(list(value))

    with open("datasheet.csv",'w') as csv_obj:
        writer = csv.writer(csv_obj, delimiter = ',')
        for line in csv_data:
            writer.writerow(line)
        csv_obj.close()
    return csv_data
#-----------------dataset loaded for comparision----------------------

sub = []
channel_link = []
rec_link = []
expertise = []
lang = []
course = []
level = []

for link in csv_datasheet():
    sub.append(link[0])
    channel_link.append(link[1])
    rec_link.append(link[2])
    expertise.append(link[3])
    lang.append(link[4])
    course.append(link[5])
    level.append(link[6])
    