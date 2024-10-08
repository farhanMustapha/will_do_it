from tkinter import *

def b_action():
    print('not work')
    maFenetre.quit()
    print('fenetre fermer')
    
maFenetre=Tk()
var=StringVar()
a=input()
var.set(a)
b=Button(maFenetre,text="save info dans la base de donne",command=b_action).pack()
l=Label(maFenetre,textvariable=var).pack()
maFenetre.mainloop()