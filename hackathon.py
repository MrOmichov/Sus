# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hackathon.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import openai

openai.api_key = "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"



conn = sqlite3.connect('code.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS codes;")

cur.execute("""CREATE TABLE IF NOT EXISTS codes(
   title TEXT,
   code TEXT);
""")
conn.commit()


def insert():
    cur.execute("INSERT INTO codes(title, code) VALUES('few_lines_of_code.py', 'few_lines_of_code.py');")
    cur.execute("INSERT INTO codes(title, code) VALUES('index.html', 'index.html');")
    cur.execute("INSERT INTO codes(title, code) VALUES('style.css', 'style.cs');")
    cur.execute("INSERT INTO codes(title, code) VALUES('script.js', 'script.js');")
    conn.commit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.isChecked = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(800, 600)
        MainWindow.setMinimumSize(800, 500)
        MainWindow.setStyleSheet("background-color: #D7E1EC;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgb(255, 255, 255), stop:1 rgb(215, 225, 236));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 90, 550, 40))
        self.plainTextEdit.setStyleSheet("background-color: white;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 90, 50, 40))
        self.pushButton.setStyleSheet("background-color: grey;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.request)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(600, 50, 5, 550))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 150, 600, 70))
        # self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("background-color: white;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 60, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        # self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 100, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        # self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 140, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        # self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 180, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        # self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.btns = [self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5]
        self.btns[0].clicked.connect(lambda: self.get(self.btns[0].text()))
        self.btns[1].clicked.connect(lambda: self.get(self.btns[1].text()))
        self.btns[2].clicked.connect(lambda: self.get(self.btns[2].text()))
        self.btns[3].clicked.connect(lambda: self.get(self.btns[3].text()))
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(430, 450, 160, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.clicked.connect(self.save)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sus"))
        self.pushButton.setText(_translate("MainWindow", "→"))
        self.label_2.setText(_translate("MainWindow", "Введите запрос:"))
        self.pushButton_2.setText(_translate("MainWindow", "few_lines_of_code.py"))
        self.pushButton_3.setText(_translate("MainWindow", "index.html"))
        self.pushButton_4.setText(_translate("MainWindow", "style.css"))
        self.pushButton_5.setText(_translate("MainWindow", "script.js"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))


    def save(self):
        text = self.textEdit.toPlainText()
        title = ''
        for i in self.btns:
            if i.text() == self.isChecked:
                title = i.text()
        data = [text, title]
        cur.execute("""UPDATE codes SET code = ? WHERE title = ?;""", data)
        conn.commit()

    def get(self, text):
        for i in self.btns:
            if i.text() == text:
                self.isChecked = i.text()
        cur.execute("SELECT code FROM codes WHERE title = ?;", (text,))
        one_result = cur.fetchone()[0]
        print(one_result)
        self.textEdit.setText(one_result)

    def request(self):
        print('a')
        try:
            prompt = self.plainTextEdit.toPlainText()
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=1024,
                top_p=1,
                temprature=0.7,
                frequency_penalty=0,
                stop=None,
            )
            self.textEdit.setText(response)
        except:
            print('b')



if __name__ == "__main__":
    insert()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
