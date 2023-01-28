#Programme PRINCIPAL caisse
import function as fct
import caisseFunction as cF

while True:

    fct.effacer_ecran()
    print("-"*50)
    entete="menu caise"
    print(f"{entete:.^50}")
    i=1
    action=["Lister la liste des ventes","le montant total des ventes"]
    for poss in action:
        print(f"{i}) {poss}")
        i+=1
    choix=fct.saisir_entier(1,i+1,"Faite un choix\n")
    if(choix>len(action)):
        break
    else:
        fct.effacer_ecran()
        if(action[choix]=="Lister la liste des ventes"):
            cF.listerVentes()
        elif(action[choix]=="Le montant total des ventes"):
            cF.MontantVentes()

    if(not fct.yesNoQuestion("Voulez vous retourner au menu Principal ")):
        break