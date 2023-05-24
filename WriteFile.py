import json
import csv

class CSV():
    def setColumns(fileNameCSV, columns, **kwargs):
            with open(fileNameCSV, "a", newline="") as file:
                dictCol = dict()
                writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
                for column in columns:
                    dictCol[column] = kwargs[column] 
                writer.writerow(dictCol)
    
    def chaingeValues(fileNameCSV, columns, **kwargs):
        with open(fileNameCSV, "a", newline="") as file:
            dictCol = dict()
            writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
            for column in columns:
                dictCol[column] = kwargs[column] 
            writer.writerow(dictCol)

class JSON():
    def setParametrs(fileNameCSV, data):
        with open(fileNameCSV, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pass