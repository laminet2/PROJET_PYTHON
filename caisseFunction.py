#Fonction caisse
import constante as cst

def listerVentes():
    with open(cst.VENTES_DIRECTORY,"r",encoding="utf-8") as f:
       line=f.readline()
       while line:
        print(line)
        line=f.readlines()   

def MontantVentes():
    somm=0
    with open(cst.VENTES_DIRECTORY) as f:
        ventes=f.read().splitlines()
        for vente in ventes:
            vente=vente.split(";")
            somm+=int(vente[2].strip())*int(vente[1].strip())
    print(f"la sommes des Ventes d'aujourd'hui vaut {somm}")
