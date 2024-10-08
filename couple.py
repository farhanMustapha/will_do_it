"""
def chercher_position(L,a):
    for i in range(0,len(L)):
        if L[i]==a:
            print(f"the index for a is {i}")
            return i

#the proble here if we have duplicate algo return just the first index 
b=[4,5,1,0,5,4,9]
a=chercher_position(b,5)
print(a)
"""
"""
def chercher_position(L,a):
    for i in range(0,len(L)):
        if L[i]==a:
            print(f"the index for a is {i}")
            return i
        else :
            return -1

#avec le else toujour retiurn -1 oooh mon dieu 
#cad il compare just le premier element et safi
b=[4,5,1,0,5,4,9]
a=chercher_position(b,5)
print(a)

"""
"""
def chercher_position(L,a):
    for i in range(0,len(L)):
        if L[i]==a:
            print(f"the index for a is {i}")
            return i
    else :
        return -1

#alors changer la position de elese resoudre le problem hhhhhhhhhhhhhh it s amzing crazy
b=[4,5,1,0,5,4,9]
a=chercher_position(b,9)
print(a)

"""
"""
def chercher_position(L,a):
    if a in L:
        return L.index(a)
    else:
        return -1

b=[4,5,1,0,5,4,9]
a=chercher_position(b,5)
print(a)

"""
""" 
def multiplication_item_list(L,n):
    resultat=[]
    for i in range(1,len(L)):
        multi=L[i]*n
        resultat.append(multi)
    return resultat # all time be carful with indent hhhh
    
L=[1,2,3,4,5,6,7,8,9,10]
a=multiplication_item_list(L,2)
print(a) """

""" 
def multiplication_item_list(L,n):
    resultat=[]
    for i in L:
        resultat.append(i*n)
    return resultat # all time be carful with indent hhhh
    
L=[1,2,3,4,5,6,7,8,9,10]
a=multiplication_item_list(L,2)
print(a) 
 """

""" def sum_list(L):
    s=0
    for i in L:
        s=s+i  # ici il y a un difference entre s=(s+i)/len(L) donne pas la valeur exact
        moy=s/len(L)
    return moy

L=[4,4,5]
moyen=sum_list(L)
print(f"la moyen de L  est {moyen}") """

def exist_in_list(L,a):
    if a in L:
        return True
    else :
        return False

L=[1,2,3,4,5,6,7,8,9,10] 

print(exist_in_list(L,1))  
