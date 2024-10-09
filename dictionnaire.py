""" d={
    "aladin":[12,15,17],
    "natalie":[15,13,16],
    "robert":[13,15,11]
}

for k,v in d.items():
    s=sum(v)
    moy=s/len(v)
    moy_arrond=round(moy,2)
    dd={
        k:moy_arrond
    }

    print(dd)
"""
""" 
d={
    "a1":[21,17,22,3],
    "a2":[11,15,8,13],
    "a3":[7,13,2,11],
    "a4":[22,14,7,9]
}

sorted_v={}
for k,v in d.items():
    v.sort()
    sorted_v[k]=v

print(sorted_v)

 """ 
""" 
txt="python est un langage facile"
dic={

}
split_txt=txt.split(" ")  
for v in split_txt:
    dic[v]=v[::-1]  #wow this syntax is wanderfull i have to understand it hhhh i didn't know it
                    # [debut : fin : pas] debut vide cad de debut
                    # fin vide cad continue jusq'a la fin
                    # -1 commence de la fin cad inverser l'ordre 
print(dic) 
"""

""" dic={}
v="exemple"

dic[v]=v[5::-1]
print(dic)

 """
txt=input("tapez une valeur :")
dic={}
splited_txt=txt.split(" ") # transform la chaine de caractere a une list
for x in splited_txt:
    l=len(x)
    dic[x]=l
print(dic)