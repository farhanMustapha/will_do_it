'''
============ demo 1 ===============
f=open("txtfile","r")
contenu=f.read()
print(contenu)
f.close()

'''

"""

============ demo 2 ===============
f=open("txtfile","r")
contenu=f.read()
elmt=contenu.split(",")
for x in elmt:
    print(x)

f.close()

"""
"""
================== demo 3 =================
f=open("txtfile","r")
contenu=f.read()
elmt=contenu.split(",")

list=[]
list.append(elmt)

for x in list:
    print(x)

f.close()
"""

""" 
================demo 4 ==============

f=open("txtfile","r")
for x in f.read().split(","):
    print(x)
f.close()

"""

"""

f=open("txtfile","r")
lire_par_line=f.readline()
print(lire_par_line)
print(lire_par_line)
"""

"""

f=open("txtfile","r")
s=""
while 1:
    ligne=f.readline()
    if ligne=="":
        break
    s=s+ligne
print(s)
"""
counter=int(input('tapez un numero : '))
f=open("txtfile","r")

if counter==0:
    lines=f.readlines()[0]
    print(lines)
    cptd=input("cpt de debit : ")
    cptc=input("cpt de credit : ")
    mntd=int(input("montant de debit : "))
    mntc=int(input("montant de credit : "))
    if cptd=="6111" and cptc=="4411" and mntd==6000 and mntc==6000:
        print("good answer")
    else:
        print("wrong answerr")
    



if counter==1:
    lines=f.readlines()[1]
    print(lines)
    cptd=input("cpt de debit : ")
    cptc=input("cpt de credit : ")
    mntd=int(input("montant de debit : "))
    mntc=int(input("montant de credit : "))
    if cptd=="5161" and cptc=="5141" and mntd==4000 and mntc==4000:
        print("good answer")
    else:
        print("wrong answerr")


if counter==2:
    lines=f.readlines()[2]
    print(lines)
    cptd=input("cpt de debit : ")
    cptc=input("cpt de credit : ")
    mntd=int(input("montant de debit : "))
    mntc=int(input("montant de credit : "))
    if cptd=="3421" and cptc=="7111" and mntd==8000 and mntc==8000:
        print("good answer")
    else:
        print("wrong answerr")



if counter==3:
    lines=f.readlines()[3]
    print(lines)
    cptd=input("cpt de debit : ")
    cptc=input("cpt de credit : ")
    mntd=int(input("montant de debit : "))
    mntc=int(input("montant de credit : "))
    if cptd=="5161" and cptc=="5141" and mntd==4000 and mntc==4000:
        print("good answer")
    else:
        print("wrong answerr")

    
    







