import json
import csv

class CSV():
    def getSurvey(fileNameCSV, columnSurwey):
        questions = dict()
        answers = dict()
        answersTrue = dict()

        with open(fileNameCSV, "r", newline="") as file:
            dictReaderExt = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_NONE)
            keyDict = 1
            for rowDictExt in dictReaderExt:
                questions[keyDict] = rowDictExt[columnSurwey[0]]
                answers[keyDict] = {
                    1: rowDictExt[columnSurwey[1]],
                    2: rowDictExt[columnSurwey[2]],
                    3: rowDictExt[columnSurwey[3]],
                    4: rowDictExt[columnSurwey[4]]}
                answersTrue[keyDict] = int(rowDictExt[columnSurwey[5]])
                keyDict += 1
        return [questions, answers, answersTrue]

    def getDictTwoColumns(fileNameCSV, columnNameKey, columnNameValues):
        usersDict = dict()
        with open(fileNameCSV, "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                    usersDict[row[columnNameKey]] = row[columnNameValues]
        return usersDict
        
    def getListOneColumn(fileNameCSV, columnName):
        usersList = list()
        with open(fileNameCSV, "r", newline="") as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    usersList.append(row[columnName])
        return usersList
    
    def getValueOnParam(key, fileNameCSV, columnNameKey, columnNameValues):
        value = ""
        dictUsers = CSV.getDictTwoColumns(fileNameCSV, columnNameKey, columnNameValues)
        value = dictUsers[key]
        return value
                

class JSON():
    def getDict(filename):
        with open(filename, "r", ) as file:
            data = json.load(file)
        return data

if __name__ == "__main__":
    print(CSV.getValueOnParam("adminwf", "users.csv", "nameUser", "levelUser"))