PLAT_DIRECTORY="plat.txt"

def details(PlatName:str)->str:
    with open(PLAT_DIRECTORY,"r",encoding="utf-8") as f :
        different_plat=f.read().split("\n\n")
        for plat in different_plat:

            plat=plat.split("\n",1)
            nom_du_plat=plat[0].split(":")
            nom_du_plat=nom_du_plat[1].strip()
            if(nom_du_plat==PlatName):
                return plat[1]
        return "PAS DE DETAILS RENSEIGNER POUR CE PLAT"

print(details("Aubergines façon wok asiatique"))