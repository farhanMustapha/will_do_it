#this function take every char in texto put it in x 
# ord convert this char to a number (unicode )
# calculate the sum and put it in s
# return s until le reste de la division par 10 egale zero then stop
#the question is why and where i can use it hhh
"""
def hashing_funct(texto):
    s=sum(ord(x) for x in texto)
    return s % 10

"""
def hashing_other_way(textiiii):
    s=0
    for x in textiiii:
        s=s+ord(x)
    return s % 10

a=hashing_other_way("world")
print(a)

#it s ok if you didn't understand the point