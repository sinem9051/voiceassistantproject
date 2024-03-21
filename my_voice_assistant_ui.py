from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(800, 600)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(330, 280, 131, 61))
            self.pushButton.setObjectName("pushButton")
            self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit.setGeometry(QtCore.QRect(240, 200, 331, 41))
            self.lineEdit.setObjectName("lineEdit")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(310, 150, 191, 31))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.microphoneButton = QtWidgets.QPushButton(self.centralwidget)
            self.microphoneButton.setGeometry(QtCore.QRect(360, 350, 71, 71))
            self.microphoneButton.setObjectName("microphoneButton")
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Enter a command:"))
        self.microphoneButton.setText(_translate("MainWindow", "🎤"))