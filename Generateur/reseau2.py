
import numpy as np
import turtle
import PIL
import matplotlib.pyplot as plt

caractere = "L"
code = ord(caractere)
print(code)

code = 76
caractere = chr(code)
print(caractere)

def base2(n):
    return bin(n)[2:]
print(base2(22))

def base10(n):
    return int(str(n), 2)
print(base10(110))

def convertire(lettre):
    if (lettre == '00'):
        return 'R'
    if (lettre == '01'):
        return 'G'
    if (lettre == '10'):
        return 'B'
    if (lettre == '11'):
        return 'W'
    
def lire_lettre(caractere):
    n = ord(caractere)
    b = base2(n)
    c = ''
    i = 0
    tab = []
    if (len(b)%2 != 0):
        c = "0"
    c += str(b)
    for i in range (0, len(c), 2):
        tab.append(convertire(c[i] + c[i+1]))
    if(len(tab) < 4):
      tab.append('R')
    return tab
        
#print(lire_lettre('A'))


def mot(chaine):
    charMot = []
    for j in range(0, len(chaine)):
        charMot.append(lire_lettre(chaine[j]))
    return charMot


def KBcode(Mat):
    KB = Mat
    for i in range(0,len(Mat)):
        for j in range(0, len(Mat[i])):
            if (Mat[i][j] == 'R'):
                KB[i][j] = (255, 0, 0)
            if (Mat[i][j] == 'G'):
                KB[i][j] = (0, 255, 0)
            if (Mat[i][j] == 'B'):
                KB[i][j] = (0, 0, 255)
            if (Mat[i][j] == 'W'):
                KB[i][j] = (255, 255, 255)
    return KB
            
"""def transpose(Tab):
    mat_t = []
    for i in range(0, len(Tab)):
        for j in range(0, len(Tab[i])):
            mat_t.append(Tab[i][j])
    return mat_t"""
              
    
carre = [["W","W","W","W","W","W","W","W"],
         ["W","R","R","R","R","R","R","W"],
         ["W","R","W","W","W","W","R","W"],
         ["W","R","W","R","R","W","R","W"],
         ["W","R","W","R","R","W","R","W"],
         ["W","R","W","W","W","W","R","W"],
         ["W","R","R","R","R","R","R","W"],
         ["W","W","W","W","W","W","W","W"],
         ["W","W","W","W","W","W","W","W"],
         ["W","R","R","R","R","R","R","W"],
         ["W","R","W","W","W","W","R","W"],
         ["W","R","W","R","R","W","R","W"],
         ["W","R","W","R","R","W","R","W"],
         ["W","R","W","W","W","W","R","W"],
         ["W","R","R","R","R","R","R","W"],
         ["W","W","W","W","W","W","W","W"]]
                            
            
Mat = mot("LE KBCode est le future de QRCode")
KB = KBcode(Mat)
#KBC = transpose(KB)
KB = KBcode(carre)

print(mot("LE KBCode est le future de QRCode"))
print(KB)
print(len(Mat))
#print(KBC)

plt.imshow(Mat)
plt.axis('off')
plt.show()

plt.imshow(carre)
plt.axis('off')
plt.show()

def transpose(Tab):
    lenth = len(Tab)   #longueur
    taille = lenth
    #resultat.append((((len(Tab)*4)%16)/4)*"0")
    for i in range(0, lenth):
      lenth_2 = len(Tab[i])
    """print(lenth)
    print(lenth_2)"""
    resultat = [['W'] * lenth_2 for i in range(lenth)]
    resultat = Tab
    if((lenth % 16) != 0):
      while((taille % 16) != 0):
        resultat.append(['W'] * lenth_2)
        taille = taille+1
    res = np.reshape(resultat, (16, -1))
    return res.tolist()

    

print(transpose(Mat))
print("_________________________________________________________")
final = KBcode(transpose(Mat))
print(final)
#_____________________________________________________________
"""def fin(Tab):
  res = Tab
  for i in range(0,len(Tab)):
    for j in range(0,len(Tab[i])):
      res[j][i] = Tab[i][j]
  return res

print(fin(final))
"""
#_____________________________________________________________
plt.imshow(final)
plt.axis('off')
plt.show()