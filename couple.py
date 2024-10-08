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

def chercher_position(L,a):
    if a in L:
        return L.index(a)
    else:
        return -1

b=[4,5,1,0,5,4,9]
a=chercher_position(b,5)
print(a)
