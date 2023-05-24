from PyQt5.QtWidgets import *
import ReadFile
import WriteFile
import Constant
class User():
    def __init__(self):
        self.idUser = Constant.idLast
        self.nameUser = "User_" + str(Constant.numberLastRegUnknownUser)
        self.passUser = Constant.generatedPass()
        self.levelUser = "Unknown (A0)"
        self.accessRights = Constant.accessRights[0]
        self.emailUser = ""
        self.phone = 0
        self.loginTelegram = self.nameUser

       
    def addUser(self, user, password):
        fileNameCSV = "users.csv"
        listColumns = ["id", "nameUser", "passUser"]
        self.nameUser = user
        self.passUser = password
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
    
    def setUserParam(self, param):
        pass