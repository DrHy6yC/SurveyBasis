import random
from symbol import parameters
from PyQt5.QtWidgets import *
import ReadFile
import WriteFile
import Constant
class User():
    def __init__(self):
        self.idUser = Constant.idLast
        self.nameUser = "User_" + str(Constant.numberLastRegUnknownUser)
        self.passUser = self.generatedPass()
        self.levelUser = "Unknown (A0)"
        self.accessRights = Constant.accessRights[0]
        self.emailUser = "dr.hy6yc@gmail.com"
        self.phone = 89181385293
        self.loginTelegram = "dr.hy6yc"

    def generatedPass(self):
        x = random.randint(9000000000000, 10000000000000000000000)
        return str(x)
       
    def addUser(self, user, password):
        fileNameCSV = "users.csv"
        listColumns = ["id", "nameUser", "passUser"]
        WriteFile.CSV.setColumns(fileNameCSV,listColumns, 
                            id = Constant.idLast, 
                            nameUser = user,
                            passUser = password
        )

    def isUserInCSV(self, filename, user):
            isUserInCSV = user in ReadFile.CSV.getListOneColumn(filename, "name")
            return isUserInCSV       

    def isInUsers(self, user):
        textLoginLE = user
        isInUsers = False
        if textLoginLE in self.getUsersList():
            isInUsers = True
        return isInUsers
    
    def isInPasswords(self, user, password, win):
        textLoginLE = user
        textPassLE = password
        dictUsers = self.getUsersDict()
        isInUsersPass = False
        if textLoginLE in dictUsers:
            if textPassLE ==  dictUsers[textLoginLE]:
                isInUsersPass = True
            else:
                QMessageBox.about(win, "Ошибка", "Пароль не верный")
                #todo Добавить логирование что пароль не верный
        else:
            QMessageBox.about(win, "Ошибка", "Пользователь не зарегистрирован")
             #todo Добавить логирование что нет пользователя
        return isInUsersPass
    
    def getUsersList(self):
        usersList = ReadFile.CSV.getListOneColumn("users.csv", "nameUser")
        return usersList
    
    def getUsersDict(self):
        usersDict = ReadFile.CSV.getDictTwoColumns("users.csv", "nameUser", "passUser")
        return usersDict