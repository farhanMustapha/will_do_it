d={
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
    
    