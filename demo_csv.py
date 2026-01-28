import csv

try:
    with open('employee_data.csv','r') as fp:
        # data = csv.reader(fp)
        # for row in data:
        #     print(row[0])
        data = csv.DictReader(fp)
        print(data.fieldnames)
        for row in data:
            print(row['NAMES'])
except FileNotFoundError:
    print("File Not Found")