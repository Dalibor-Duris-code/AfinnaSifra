# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK
import string
import math
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
    text = text.replace('0', 'XZEROX')
    text = text.replace('1', 'XONEX') 
    text = text.replace('2', 'XTWOX')
    text = text.replace('3', 'XTHREEX')
    text = text.replace('4', 'XFOURX')
    text = text.replace('5', 'XFIVEX')
    text = text.replace('6', 'XSIXX')
    text = text.replace('7', 'XSEVENX')
    text = text.replace('8', 'XEIGHTX')
    text = text.replace('9', 'XNINEX')
    return text
    
def replaceNumberBack(text: str):
    text = text.replace('XZEROX','0')
    text = text.replace('XONEX','1')
    text = text.replace('XTWOX','2')
    text = text.replace('XTHREEX','3')
    text = text.replace('XFOURX','4')
    text = text.replace('XFIVEX','5')
    text = text.replace('XSIXX','6')
    text = text.replace('XSEVENX','7')
    text = text.replace('XEIGHTX','8')
    text = text.replace('XNINEX', '9')
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

def encrypt(vstupText, kluc):
    sifrovany = ''
    
    vstupText = upperChar(vstupText)
    vstupText = removeDlzne(vstupText)
    vstupText = replaceSpace(vstupText)
    vstupText = replaceNumber(vstupText)
    
    sifrovany = ''.join(Abeceda[(Abeceda.index(znak)*kluc[0]+kluc[1])%26] 
                    for znak in vstupText)   
    return sifrovany
     
def decrypt(sifVstupText, kluc):
    desifrovany = ''
    desifrovany = ''.join( Abeceda[multIverz(kluc[0], 26)*(Abeceda.index(znak)-kluc[1])%26] 
                   for znak in sifVstupText)
    desifrovany = returnSpace(desifrovany)
    desifrovany = replaceNumberBack(desifrovany)
    
    return desifrovany

def vypis(sifrovany):
    for i in range(int(len(sifrovany) / 5) + int(len(sifrovany) % 5) + 1):
        print(sifrovany[((i * 5) - 5 ): i * 5], " ", end="")
    print()
 
def main():
    text = 'Ahoj,25 TY DEBIL'
    key = [7, 1]
    affine_encrypted_text = encrypt(text, key )
    affine_decrypted_text = decrypt(affine_encrypted_text, key)

    
    
    print('sifrovane: '); vypis(affine_encrypted_text)
    
    print('desifrovane: ' + affine_decrypted_text)
    n = 5
      
    string = 'KOKOSOAAOSJDOADFJODSJGSODGJOSDGJOJSDGOSJDGOSJDGOSDJGO'
    
    # Using list comprehension
    affine_decrypted_text.split()
      
    # Printing output
# Main program starts here
main()