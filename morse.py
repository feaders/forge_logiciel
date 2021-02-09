from tkinter import *
import string
from functools import partial
import random

main = Tk()
main.geometry("5000x400")
main.title('Morse')

def symbole(l, mot):
    m=mot.get()+l
    mot.set(m)
def effacer(mot):
    mot.set("")

def trad():
    res=inpt.get()
    res = res.split()
    m=""
    print(morses)
    print(res)
    for i in range(0,len(res)):
        for c in range(0,26):
            if res[i]==morses[c]:
                m+=reallettres[c]
                break
    mot.set(m)
    
    
mot = StringVar()
texte1 = Label(main, text="Morse").pack()
textmot = Label(main, textvariable =mot).pack()
inpt = Entry(main, width=1000)
inpt.pack()
photo =[]
bouton =[]
reallettres=string.ascii_lowercase
morses = [ '.-', '-...', '-.-.','-..', '.','..-.', '--.', '....', '..','.---','-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-','.--', '-..-', '-.--', '--..']
lettres =random.sample(reallettres,len(reallettres))
y = 75
x=75
for i in range(0,26):
    path ="Morse/"+lettres[i]+".png"
    photo.append(PhotoImage(file = r""+path))
    x +=220
    if i%7==0:
        y+=75
        x=75
    l= lettres[i]
    b= Button(main, text="Symbole"+str(i), image=photo[i], command= partial(symbole,l, mot)).place(x=x,y=y)
    bouton.append(b)
mot.set("")
boutonDechiffrage = Button(main, text="Traduire", command= lambda: trad()).pack()
boutonDechiffrage = Button(main, text="Effacer", command= lambda: effacer(mot)).pack()

main.mainloop()
