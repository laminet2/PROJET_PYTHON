#Fonction caisse
import constante as cst
import function as fct

def listerVentes():
    with open(cst.VENTES_DIRECTORY,"r",encoding="utf-8") as f:
       line=f.readline()
       if(line==""):
            print("Aucune Vente realiser pour l'instant")
       while line:
        print(line)
        line=f.readline()   

def MontantVentes():
    somm=0
    with open(cst.VENTES_DIRECTORY) as f:
        ventes=f.read().splitlines()
        for vente in ventes:
            vente=vente.split(";")
            somm+=int(vente[2].strip())*int(vente[1].strip())

    print(f" {' ':.>30} \n\n")
    

    print(f"la sommes des Ventes d'aujourd'hui vaut : {fct.formatage_montant(somm)} {cst.DEVISE}\n\n")

    print(f"{' ':.>30}\n")
