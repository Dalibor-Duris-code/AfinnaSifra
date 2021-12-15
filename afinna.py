import string
import math
import re

from PyQt5 import QtWidgets

from GUICKO import Ui_MainWindow
Abeceda = string.ascii_uppercase

def upperChar(text: str):
    text = text.replace('a', 'A')
    text = text.replace('b', 'B')
    text = text.replace('c', 'C')
    text = text.replace('d', 'D')
    text = text.replace('e', 'E')
    text = text.replace('f', 'F')
    text = text.replace('g', 'G')
    text = text.replace('h', 'H')
    text = text.replace('i', 'I')
    text = text.replace('j', 'J')
    text = text.replace('k', 'K')
    text = text.replace('l', 'L')
    text = text.replace('m', 'M')
    text = text.replace('n', 'N')
    text = text.replace('o', 'O')
    text = text.replace('p', 'P')
    text = text.replace('r', 'R')
    text = text.replace('s', 'S')
    text = text.replace('t', 'T')
    text = text.replace('u', 'U')
    text = text.replace('v', 'V')
    text = text.replace('w', 'W')
    text = text.replace('x', 'X')
    text = text.replace('y', 'Y')
    text = text.replace('z', 'Z')   
    return text

def removeDlzne(text: str):
    text = text.replace('á', 'A')
    text = text.replace('ľ', 'L')
    text = text.replace('š', 'S')
    text = text.replace('č', 'C')
    text = text.replace('ť', 'T')
    text = text.replace('ž', 'Z')
    text = text.replace('ý', 'Y')
    text = text.replace('í', 'I')
    text = text.replace('é', 'E')
    text = text.replace('ô', 'O')
    text = text.replace('ň', 'N')
    text = text.replace('ĺ', 'L')
    text = text.replace('ó', 'O')
    text = text.replace('ř', 'R') 
    text = text.replace('ú', 'U') 
    text = text.replace('ě', 'E') 
    return text

def replaceSpace(text: str):
    text = text.replace(' ', 'XMEZERAX')
    text = text.replace('.', 'XBODKAX')
    text = text.replace('!', 'XVYKRICNIKX')
    text = text.replace('?', 'XOTAZNIKX')
    text = text.replace(',', 'XCIARKAX')
    return text

def returnSpace(text: str):
    text = text.replace('XMEZERAX', ' ')
    text = text.replace('XBODKAX', '.')
    text = text.replace('XVYKRICNIKX', '!')
    text = text.replace('XOTAZNIKX', '?')
    text = text.replace('XCIARKAX', ',')
    return text

def replaceNumber(text: str):
    text = text.replace('0', 'XZEX')
    text = text.replace('1', 'XONX') 
    text = text.replace('2', 'XTWX')
    text = text.replace('3', 'XTHX')
    text = text.replace('4', 'XFOX')
    text = text.replace('5', 'XFVX')
    text = text.replace('6', 'XSIX')
    text = text.replace('7', 'XSEX')
    text = text.replace('8', 'XEIX')
    text = text.replace('9', 'XNIX')
    return text
    
def replaceNumberBack(text: str):
    text = text.replace('XZEX','0')
    text = text.replace('XONX','1')
    text = text.replace('XTWX','2')
    text = text.replace('XTHX','3')
    text = text.replace('XFOX','4')
    text = text.replace('XFIX','5')
    text = text.replace('XSIX','6')
    text = text.replace('XSEX','7')
    text = text.replace('XEIX','8')
    text = text.replace('XNIX', '9')
    return text

def egcd(a, b):
    x,y = 0,1
    u,v = 1,0
    while a != 0:
        q= b//a
        r = b % a
       
        m, n = x-u*q, y-v*q
        n = y-x*q
        
        b,a, = a,r
        x,y = u,v
        u,v = m,n
    gcd = b
    return gcd, x, y
 
def multIverz(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m

def encrypt(vstupText, klucA, klucB):
    sifrovany = ''
    
    vstupText = upperChar(vstupText)
    vstupText = removeDlzne(vstupText)
    vstupText = replaceSpace(vstupText)
    vstupText = replaceNumber(vstupText)
    
    sifrovany = ''.join(Abeceda[(Abeceda.index(znak)*klucA+klucB)%26] 
                    for znak in vstupText)   
    return sifrovany
    #sifrovanyOD = vypis(sifrovany)
     
def decrypt(sifVstupText, klucA, klucB):
    desifrovany = ''
    desifrovany = ''.join( Abeceda[multIverz(klucA, 26)*(Abeceda.index(znak)-klucB)%26] 
                   for znak in sifVstupText)
    desifrovany = returnSpace(desifrovany)
    desifrovany = replaceNumberBack(desifrovany)
    return desifrovany

    #bprint()
 

# def __init__(self):
#     QtWidgets.QMainWindow.__init__(self)
#     Ui_MainWindow.__init__(self)
#     self.setupUi(self)
#     self.pushButton_1.clicked.connect(self.encrypt)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
# def main():
#     text = 'Ahoj,25 TY DRAK'
#     key = [7, 1]
#     klucA = int(7)
#     klucB = int(1)
#     affine_encrypted_text = encrypt(text, klucA, klucB )
#     affine_decrypted_text = decrypt(affine_encrypted_text, klucA, klucB)

    
    
#     print('sifrovane: '); vypis(affine_encrypted_text)
    
#     print('desifrovane: ' + affine_decrypted_text)
#     n = 5
      
#     string = 'KOKOSOAAOSJDOADFJODSJGSODGJOSDGJOJSDGOSJDGOSJDGOSDJGO'
    
#     # Using list comprehension
#     affine_decrypted_text.split()
      
#     # Printing output
# # Main program starts here
# main()