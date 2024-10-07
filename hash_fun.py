#this function take every char in texto put it in x 
# ord convert this char to a number (unicode )
# calculate the sum and put it in s
# return s until le reste de la division par 10 egale zero then stop
#the question is why and where i can use it hhh

def hashing_funct(texto):
    s=[sum(ord(x) for x in texto)]
    return s%10