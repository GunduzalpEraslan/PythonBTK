# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_comboboxForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from _comboboxForm import U


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(80, 40, 211, 91))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(350, 50, 201, 71))
        self.lblResult.setObjectName("lblResult")
        self.btnGetItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItem.setGeometry(QtCore.QRect(80, 150, 211, 71))
        self.btnGetItem.setObjectName("btnGetItem")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 150, 211, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 26))
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
        self.lblResult.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItem.setText(_translate("MainWindow", "Get Item"))
        self.pushButton_2.setText(_translate("MainWindow", "Load Item"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())