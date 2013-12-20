import os
path="." # insert the path to the directory of interest
dirList=os.listdir(path)
import re
import base64
def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
"z23a" -> ["z", 23, "a"]
"""
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

dirList.sort(key=alphanum_key)

def writeindex(compteur,stri,taille):
    plusun = compteur + 1
    moinsun = compteur - 1
    moinsun = str(moinsun)
    if compteur == 0 :
        filef = open('index.html', 'w')
        moinsun = "index.html"
    else :
        if compteur == taille - 1 :
            plusun = compteur
        filef = open('%d.html'%compteur, 'w')


    filef.write("<html><body><center>\r\n")
    filef.write("<a href='http://shiniez.deviantart.com/'>http://shiniez.deviantart.com/</a><br>\r\n")
    filef.write("<a href='index.html'><<</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href='%s.html'><</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href='%d.html'>></a>&nbsp;&nbsp;&nbsp;&nbsp;<a href='%d.html'>>></a><br>\r\n"%(moinsun,plusun,taille-1))
    filef.write("<img src='data:image/jpg;base64,%s'><br>\r\n"%stri)
    stri = ""
    filef.write("<a href='index.html'><<</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href='%s.html'><</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href='%d.html'>></a>&nbsp;&nbsp;&nbsp;&nbsp;<a href='%d.html'>>></a><br>\r\n"%(moinsun,plusun,taille-1))
    filef.write("<center></body></html>\r\n")

    filef.close()

compteur = 0
listimg = []
for fname in dirList:
    if "jpg" in fname :
        listimg.append(fname)

taille = len(listimg)
for img in listimg :
            image_file = open(img, "rb")
            stri = base64.b64encode(image_file.read())
            image_file.close()
            
            writeindex(compteur,stri,taille)
            compteur += 1
            stri = ""