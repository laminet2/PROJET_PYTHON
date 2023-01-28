#Programme principal client
import function as fct
import clientFunction as cF

commandes=[]
view=None
while True:

    if(view==None):
         PlatName,info,view=cF.render_view((cF.MenuPrincipal()))
    else:
         PlatName,info,view=cF.render_view(view)

    if(PlatName==0):
        #Il a fini il veut sortir  
        break
    else:
        if(fct.yesNoQuestion("Voulez-vous voir les details")):
            print(cF.details(PlatName))

            if(not fct.yesNoQuestion("Voulez-vous commander")):
                continue
        qte_voulue=fct.saisir_entier(1,1,"entrer le nombre de plat\n")
        
        if(qte_voulue>int(info["qte"])):
            print("la quantité demandé est superieur au nombre de plat dispo coreespondent à",info["qte"])
            if(fct.yesNoQuestion("Vouliez vous changer la qantite voulue")):
                qte_voulue=fct.saisir_entier(1,info["qte"],"entrer une nouvelle quantite")
        
        if(not fct.yesNoQuestion(f"voulez vous un autre {view}")):
            view=None
        
        if(qte_voulue<=int(info["qte"])):
            commande={"nom":PlatName,"qte":qte_voulue,"prix":info["prix"]}
            commandes.append(commande)

if(commandes!=[]):

    cF.generation_ticket(commandes)
    cF.uptade_file_vente(commandes)
    cF.soustraction_qte(commandes)