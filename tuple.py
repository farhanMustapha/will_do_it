A={'stylo','crayon','gorme'}
""" b=input()
if b in A:
    print("exist")
else:
    print("non trouver") """
#print(len(A))
A.add("regle")
A.update(["atrouse","papier","stylo bleu"])
try:
    A.remove("atrous")
    print(A)
except :
    print("n'existe pas ")
