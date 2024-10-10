#A={'stylo','crayon','gorme'}
""" b=input()
if b in A:
    print("exist")
else:
    print("non trouver") """
#print(len(A))

""" 
A.add("regle")
A.update(["atrouse","papier","stylo bleu"])
try:
    A.remove("atrous")
    print(A)
except :
    print("n'existe pas ")
"""

""" 
A.clear()

if len(A)>0:
    print(A)
else:
    print("pas d'elements") 
"""
""" del A
try:
    print(A)
except:
    print("A n exist pas ")
     """

""" A={'a','b','c','d'}
B={'c','e','d','h'}
c=A.intersection(B)
print(c)
 """
""" 
A={'a','e','c','d'}
B={'c','e','d','h'}
c=set({})
for x in A:
    for y in B:
        if x==y:
            c.add(x)
print(c) """

""" 
A={'a','g','c','d'}
B={'c','e','d','h'}
c=set({})
for x in A:
    if x in B:
        c.add(x)
print(c) """

""" 
A={'a','g','c','d'}
B={'k','e','j','h'}

for x in B:
    A.add(x)
print(A) """


A={'1','2','3','4'}
B={'3','4','5','6'}
#c=A.intersection(B)

print((A-B).union(B-A))
