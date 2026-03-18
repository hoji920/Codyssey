import csv

with open('Mars_Base_Inventory_List.csv','r',encoding='utf-8') as file:
    reader = csv.reader(file)
    for readers in reader:
        print(readers)
