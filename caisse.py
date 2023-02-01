#Programme PRINCIPAL caisse
import function as fct
import caisseFunction as cF

while True:

    fct.effacer_ecran()
    print("-"*50)
    entete="menu caise"
    print(f"{entete:.^50}")
    i=1
    action=["Lister la liste des ventes","Le montant total des ventes","Quitter"]
    for poss in action:
        print(f"{i}) {poss}")
        i+=1
    choix=fct.saisir_entier(1,i+1,"Faite un choix\n")
    if(choix>len(action)-1):
        break
    else:
        fct.effacer_ecran()
        if(action[choix-1]=="Lister la liste des ventes"):
            cF.listerVentes()
        elif(action[choix-1]=="Le montant total des ventes"):
            cF.MontantVentes()

    if(not fct.yesNoQuestion("Voulez vous retourner au menu Principal ")):
        break