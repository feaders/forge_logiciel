from tkinter import *
import string
from functools import partial
import random

main = Tk()
main.geometry("5000x400")
main.title('Application de Traduction Franc-Maconnique')

def symbole(l, mot):
    m=mot.get()+l
    mot.set(m)
def effacer(mot):
    mot.set("")


mot = StringVar()
texte1 = Label(main, text="Entrez votre code Franc-Maçonnique").pack()
textmot = Label(main, textvariable =mot).pack()
photo =[]
bouton =[]
lettres=string.ascii_lowercase
lettres =random.sample(lettres,len(lettres))
for i in range(0,26):
    path ="symbolesFM/"+lettres[i]+".png"
    photo.append(PhotoImage(file = r""+path))
    x = 150+ 50 * i
    y = 75
    l= lettres[i]
    b= Button(main, text="Symbole"+str(i), image=photo[i], command= partial(symbole,l, mot)).place(x=x,y=y)
    bouton.append(b)
mot.set("")
boutonDechiffrage = Button(main, text="Effacer", command= lambda: effacer(mot)).pack()

main.mainloop()
