import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):

    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,700,700)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayi1: ")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi2: ")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapma)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(250,130)
        self.btn_cikar.clicked.connect(self.hesapma)

        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.setText("Çarpma")
        self.btn_carpma.move(150,170)
        self.btn_carpma.clicked.connect(self.hesapma)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText("Bölme")
        self.btn_bolme.move(250,170)
        self.btn_bolme.clicked.connect(self.hesapma)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuç: ")
        self.lbl_sonuc.move(65,230)

    def hesapma(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Topla':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == 'Çıkar':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == 'Çarpma':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender == 'Bölme':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())

        self.lbl_sonuc.setText('sonuç: '+ str(result))
    

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())

app()

