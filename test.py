def formatage_montant(somm):
   
    t=[]
    for x in str(somm):
        t.append(x)
    x=len(t)-3
    while(x>0):
        t.insert(x,".")
        x-=3

    print(t)
    return "".join(t)

print(formatage_montant(400000))