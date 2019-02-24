
import csv

with open("Klarf.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

MEASUREMENTNAME=''
ATTRIBUTENAME=''
MEASUREMENTTYPE='Circularity'




