def chercher_position(L,a):
    for i in range(0,len(L)):
        if L[i]==a:
            return i


b=[4,5,1,0,5,4,9]
a=chercher_position(b,9)
print(a)
