import csv
class Survey():
    def __init__(self):
        self.questions = {}
        self.answers = {}
        self.answersTrue = {}
        self.answersUser = {}
        self.resultSurvey = False

    def inputSurvey(self, objectFile):
        FILENAME = objectFile
        with open(FILENAME, "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_NONE)
            i = 1
            for row in reader:
                self.questions[i] = row["Question"]
                self.answers[i] = {
                    1: row["Answer1"],
                    2: row["Answer2"],
                    3: row["Answer3"],
                    4: row["Answer4"]}
                self.answersTrue[i] = int(row["TrueAnswer"])
                i+=1
    
    def getAnswerUser (self,numberQuestion, numberAnswer):
        self.answersUser[numberQuestion] = numberAnswer
    
    def endSurvey(self):
        isEnd = False
        if len(self.answers) == len(self.answersUser):
            isEnd = True
        return isEnd
    
    def compareAnswer(self):
        if self.endSurvey:
            for i in self.questions:
                if self.answersTrue[i] == self.answersUser[i]:
                    self.resultSurvey = True
                else:
                    self.resultSurvey = False
                    break


    def takingSurvey(self):
        for i in self.questions:
            print(self.questions[i])
            for a in self.answers[i]:
                print(a, self.answers[i][a])
            self.getAnswerUser(i, int(input("Введите номер ответа: ")))

    def getResultSurvey(self):
        if self.resultSurvey:
            print("Тест пройден")
        else:
            print("Тест не пройден")



test = Survey()
test.inputSurvey("users.csv")
test.takingSurvey()
test.compareAnswer()
test.getResultSurvey()