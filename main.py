import afinna
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

qtCreatorFile = "AfinnaGUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class GUICKO(QMainWindow, Ui_MainWindow):  
    
    error = "error"

    def default(self):
        self.vstupnyText.setText('Ahoj')
        self.klucA.setText('7')
        self.klucB.setText('1')
        

    def encryption(self):
        try:
            a = int(self.klucA.toPlainText())
            b = int(self.klucB.toPlainText())
            self.sifrovanyText.setText(afinna.encrypt(self.vstupnyText.toPlainText(),a , b))
        except:
            self.sifrovanyText.setText(self.error)
    def decryption(self):
        try:
            a = int(self.klucA.toPlainText())
            b = int(self.klucB.toPlainText())
            desifrovany = afinna.decrypt(self.sifrovany.toPlainText(),a , b)
            self.desifrovanyText.setText(desifrovany)
        except:
            self.sifrovanyText.setText(self.error)

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.sifruj.clicked.connect(self.encryption)
        self.desifruj.clicked.connect(self.decryption)
        self.default()
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUICKO()
    window.show()
    sys.exit(app.exec_())