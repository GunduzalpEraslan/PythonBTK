# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_sayi2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sayi2.setGeometry(QtCore.QRect(50, 50, 55, 16))
        self.label_sayi2.setObjectName("label_sayi2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 55, 16))
        self.label_2.setObjectName("label_2")
        self.txt_sayi1 = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(110, 40, 511, 41))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(110, 90, 511, 41))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_toplama = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toplama.setGeometry(QtCore.QRect(110, 150, 121, 51))
        self.btn_toplama.setObjectName("btn_toplama")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(240, 150, 121, 51))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(370, 150, 121, 51))
        self.btn_bolme.setObjectName("btn_bolme")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(500, 150, 121, 51))
        self.btn_carpma.setObjectName("btn_carpma")
        self.label_sayi2_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sayi2_2.setGeometry(QtCore.QRect(120, 220, 71, 51))
        self.label_sayi2_2.setObjectName("label_sayi2_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 26))
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
        self.label_sayi2.setText(_translate("MainWindow", "Sayı 1 :"))
        self.label_2.setText(_translate("MainWindow", "Sayı 2 :"))
        self.btn_toplama.setText(_translate("MainWindow", "Toplama"))
        self.btn_cikarma.setText(_translate("MainWindow", "Çıkarma"))
        self.btn_bolme.setText(_translate("MainWindow", "Bölme"))
        self.btn_carpma.setText(_translate("MainWindow", "Çarpma"))
        self.label_sayi2_2.setText(_translate("MainWindow", "Sonuç :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
