from unicodedata import numeric
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def read_excel_file(loc):
            import xlrd 
            file = xlrd.open_workbook(loc)
            sheet = file.sheet_by_index(0)
            return sheet


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PREDICT POPULATION")
        MainWindow.resize(620, 478)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background:#2F2C2C;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LE_result = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_result.setGeometry(QtCore.QRect(10, 0, 531, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.LE_result.setFont(font)
        self.LE_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LE_result.setStyleSheet("color: #D62121")
        self.LE_result.setReadOnly(True)
        self.LE_result.setObjectName("LE_result")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(50, 120, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("color: #F4F4F4")
        self.btn_7.setObjectName("btn_7")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(180, 200, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("color: #F4F4F4")
        self.btn_5.setObjectName("btn_5")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(50, 200, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("color: #F4F4F4")
        self.btn_4.setObjectName("btn_4")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(310, 120, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("color: #F4F4F4")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(180, 120, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("color: #F4F4F4")
        self.btn_8.setObjectName("btn_8")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(310, 280, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("color: #F4F4F4")
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(180, 280, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("color: #F4F4F4")
        self.btn_2.setObjectName("btn_2")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(50, 280, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("color: #F4F4F4")
        self.btn_1.setObjectName("btn_1")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(310, 200, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("color: #F4F4F4")
        self.btn_6.setObjectName("btn_6")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(180, 360, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("color: #F4F4F4")
        self.btn_0.setObjectName("btn_0")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(50, 360, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("color: #F4F4F4\n"
"")
        self.btn_dot.setObjectName("btn_dot")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 380, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#F20D1B;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 120, 171, 71))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("color:#F20D1B;\n"
"font-size: 32px;")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 200, 171, 71))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setStyleSheet("color:#F20D1B;\n"
"font-size: 32px;")
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.label.setText(_translate("MainWindow", "CR: Parham Esmailzadeh"))
        self.pushButton.setText(_translate("MainWindow", "CONFRIM"))
        self.pushButton_2.setText(_translate("MainWindow", "CLEAR"))
        
        # my code:
        self.btn_0.clicked.connect(lambda: self.number_press('0'))
        self.btn_1.clicked.connect(lambda: self.number_press('1'))
        self.btn_2.clicked.connect(lambda: self.number_press('2'))
        self.btn_3.clicked.connect(lambda: self.number_press('3'))
        self.btn_4.clicked.connect(lambda: self.number_press('4'))
        self.btn_5.clicked.connect(lambda: self.number_press('5'))
        self.btn_6.clicked.connect(lambda: self.number_press('6'))
        self.btn_7.clicked.connect(lambda: self.number_press('7'))
        self.btn_8.clicked.connect(lambda: self.number_press('8'))
        self.btn_9.clicked.connect(lambda: self.number_press('9'))
        self.btn_dot.clicked.connect(lambda: self.number_press('.'))
        
        self.pushButton_2.clicked.connect(lambda: self.CLEAR_press())
        self.pushButton.clicked.connect(lambda: self.confrim_press())
        

# my functions:
    
    def number_press(self, number):
        expression = self.LE_result.text()
        self.LE_result.setText(expression + number)
            
    def CLEAR_press(self):
        self.LE_result.setText("")
    
    
    def confrim_press(self):
            try:
                    expression = self.LE_result.text()
                    from sklearn import linear_model
                    import numpy as np
                    # excel file address:
                    sheet = read_excel_file("C:/Users/A/Desktop/DataSet/Iran_Population.xlsx")
                    list_year = []
                    list_population = []
                    for i in range(0, sheet.nrows):
                            list_year.append([sheet.cell_value(i,0)])
                            list_population.append([sheet.cell_value(i,1)])
                    x = np.array(list_year, dtype=int)
                    y = np.array(list_population, dtype=int)
                    x = np.array(list_year, dtype=int).reshape(-1,1)
                    y = np.array(list_population, dtype=int).reshape(-1,1)
                    list_test = self.LE_result.text()
                    x_test = np.array(list_test, dtype=int)
                    x_test = np.array(list_test, dtype=int).reshape(-1,1)
                    regr = linear_model.LinearRegression()
                    regr.fit(x,y.ravel())
                    y_pred = regr.predict(x_test)
                    y_pred = int(y_pred)
                    y_pred = str(y_pred)
                    self.LE_result.setText(y_pred)

            except:
                self.LE_result.setText("invalid syntax")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.move(0,0)
    MainWindow.setWindowTitle("Predict Population OF Iran")
    MainWindow.show()
    sys.exit(app.exec_())