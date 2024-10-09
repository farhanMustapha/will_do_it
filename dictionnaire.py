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

    print(dd) """
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

txt="python est un langage facile"
dic={

}
split_txt=txt.split(" ")  
for v in split_txt:
    dic[v]=v[::-1]
print(dic)

    
    