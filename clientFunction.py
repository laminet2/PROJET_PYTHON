
#FONCTION
from genericpath import exists
from time import sleep
from datetime import datetime

import constante as cst
import function as fct
#Variable globales 

#PROGRAMME PRINCIPAL

def find_all_data(view):
    view=view.lower()
    view=view.replace(" ","_")
    nom_du_fichier=view+".txt"
    if(exists(nom_du_fichier)):
        with open(nom_du_fichier,"r",encoding="utf-8") as f:
            data=f.read()
            data=data.splitlines()
    else:
        f=open(nom_du_fichier,"w",encoding="utf-8")
        data=[]
        f.close

    return data

def render_view(view):

    #COEUR DU PROJET 

    """
        Cette fonction est identique a l'image de render view en php
        elle te charge le model , la vue correspondante et elle t'affiche la vue
        mais en plus elle te retourne le plat du choix qu'il a fait dans un tableau
    """
    
    if view==0:
        return 0,0,0

    menu_afficher=find_all_data(view)

    #AFFICHAGE EN TETE
    fct.effacer_ecran()
    print('*'*50)
    print(f"{view.upper(): ^50}")
    print('*'*50)
    
    #TRAITEMENT DU CAS OU IL YA AUCUN PLAT AU MENU PRICIPAL OU FAST FOOD OU UN NEW MENU
    if menu_afficher==[]:
        print("AUCUN PLAT DISPONIBLE POUR L'INSTANT POUR CE MENU ")
        print("DESOLE DU DESAGREMENT")
        print("NOUS VOUS RAMENONS AU MENU PRINCIPAL")
        sleep(4)
        return render_view(MenuPrincipal())

    menu_reel_a_afficher={}
    for m in menu_afficher:

            m=m.split(":")
            #traitement du cas ou il ya un deux point ki manque
            
            if(len(m)!=3 ):
                continue
            nom=m[0].strip()
            prix=m[1].strip()
            qte=m[2].strip()

            #traitement du cas ou le prix ou la qte soit inconvertible en entier
            #ce plat est ignorer
            test=prix.replace(",","")
            if(test.isdigit()==False or qte.isdigit()==False):
                continue
            

            #TRAITEMEN T DU CAS OU LA QTE EST SUPERIEUR AUX PRIX
            #ON SUPPOSE QUE SES UNE 
            #ERREUR
            # if(int(qte)>int(prix)):
            #     qte,prix=prix,qte

            prix=int(prix)
            qte=int(qte)

            #TRAITEMENT DU CAS OU LA QTE RESTANTE EST EGALE A 0
            if(qte==0):
                continue
            else:

                #CREATION D'UNE STRUCTURE DE DONNE COMPLEXE EMPECHANT
                #L'AFFICHAGE DE DEUX PLAT AYANT DES NOMS IDENTIQUES
                #EN EFFET ELLE SERA SOUS CETTE FORME 
                # { "nom_du_plat0":{"prix":500 ,"qte":10},
                #    "nom_du_plat1":{"prix":700 ,"qte":8},
                #     "nom_du_plat1":{"prix":700 ,"qte":14},
                #    }
                
                plat={"prix":prix,"qte":qte}
                nom=nom.lower()
                menu_reel_a_afficher[nom]=plat
    
    #partie affichage du menu
    
    i=1   
    for nom in menu_reel_a_afficher:
            prix=menu_reel_a_afficher[nom]["prix"]
            print(f"{i}{nom.upper():.>40} {prix} {cst.DEVISE} ")
            i+=1

    print(f"{i}{'Retourner':.>50}")

    print(50*"-")

    #partie choix et traitement du choix

    choix=fct.saisir_entier(1,i,"Faites votre choix :\n")
    if i==choix:
        return render_view(MenuPrincipal())

        #je dois recuperer l'indice de l'affichage 
        # de la clé du choix effectuable par enumerate()
    for indice,keys in enumerate(menu_reel_a_afficher):
        if(indice+1 ==choix):
            return keys,menu_reel_a_afficher[keys],view

def details(PlatName:str)->str:
    fct.effacer_ecran()
    with open(cst.PLAT_DIRECTORY,"r",encoding="utf-8") as f :
        different_plat=f.read().split("\n\n")
        for plat in different_plat:

            plat=plat.split("\n",1)
            nom_du_plat=plat[0].split(":")
            nom_du_plat=nom_du_plat[1].strip()

            if(nom_du_plat.lower()==PlatName):
                return plat[1]
        return "PAS DE DETAILS RENSEIGNER POUR CE PLAT"

def MenuPrincipal():

    menu_afficher=find_all_data(cst.MENU_PRINCIPAL_NAME)
    fct.effacer_ecran()
    i=1
    print('*'*50)
    print(f"{cst.MENU_PRINCIPAL_NAME.upper(): ^50}")
    print('*'*50)

    #AFIN D'EVITER LA REDONDANCE
    #au cas ou le user ecrit un mm menu plusieurs fois
    menu_reel_afficher=set()
    menu_reel_afficher.update([mots.lower() for mots in menu_afficher])

    for m in menu_reel_afficher:
        print(f"{i}{m.upper():.>50}")
        i+=1

    print(f"{i}{'Quitter':.>50}")

    print(50*"-")

    choix=fct.saisir_entier(1,i,"Faites votre choix :\n")

    if(choix==i):

        return 0
        #quitter le programme
        # if os.name=='posix':
        #     os.system("pkill -f 'python'")
        # else:
        #     os.system("taskkill /im cmd.exe")
    
    for indice,value in enumerate(menu_reel_afficher):

        if(choix==indice+1):
            return value


def generation_ticket(commandes):

    #Entete
    entete=f"{'RESTO DIMENSION ALLOCO':.^40}\n"

    #Name fichier ticket
    datenow=datetime.now()
    dateticket=datenow.strftime("%d%m%Y%H%M%S")
    fileticket="ticket/"+dateticket+".txt"

    #reference bas de page
    dateBas_de_page=datenow.strftime("%d/%m/%Y à %H:%M")
    bas_de_page="\nImprimé le "+dateBas_de_page+"      "+" MERCI"

    #Corp du ticket
    ecriture=""
    somme=0
    with open(fileticket,"w",encoding="utf-8") as f:
        for commande in commandes:
            ecriture=ecriture + "{} ( {} ) {} \n".format(commande["nom"],commande["qte"],commande["prix"]*commande["qte"])
            somme+=commande['prix']*commande["qte"]

        ecriture+=f"TOTAL:   {fct.formatage_montant(somme)}{cst.DEVISE}"
        f.write(entete)
        f.write(ecriture)
        f.write(bas_de_page)


def uptade_file_vente(commandes):

    ecriture=""
    with open(cst.VENTES_DIRECTORY,"a",encoding="utf-8") as f:
        for commande in commandes:
            ecriture=ecriture+"{} ; {} ; {}\n".format(commande["nom"],commande["qte"],commande["prix"])
        f.write(ecriture)

def soustraction_qte(commandes):

            CommandesByView={}
            for commande in commandes:
                if(commande["view"] not in CommandesByView):
                    CommandesByView[commande["view"]]=[]

                CommandesByView[commande["view"]].append(commande)

            for viewOriginale in CommandesByView:

                view=viewOriginale.replace(" ","_")
                view=view+".txt"

                with open(view,"r",encoding="utf-8") as f:
                    new_menu=[]
                    oldmenu=f.read().split("\n")
                    for platWDP in oldmenu:
                        plat=platWDP.split(":")
                        nomPlat=plat[0].strip()

                        for commande in CommandesByView[viewOriginale]:
                            
                            if(commande["nom"]==nomPlat.lower()):
                                platWDP="{} : {} : {}".format(commande["nom"],commande["prix"],int(plat[2].strip())-commande["qte"])
                                break

                        new_menu.append(platWDP)

                with open(view,"w",encoding="utf-8") as f:
                    for menu in new_menu:
                        f.write(f"{menu}\n")

# def soustraction_qte(commandes):
#     views=set()
#     with open(cst.MENU_PRINCIPAL_DIRECTORY,'r',encoding="utf-8") as f:
#         test=f.read().splitlines()
#         for i in test:
#             views.add(i.lower())

#     for view in views:

#         view=view.replace(" ","_")
#         view=view+".txt"
#         new_menu=[]

#         if(exists(view)):
#             with open(view,"r",encoding="utf-8") as f:

#                     different_plat=f.read().split("\n")

#                     for plat_with_deux_point in different_plat:

#                         plat=plat_with_deux_point.split(":")
#                         nomplat=plat[0].strip()
#                         for i in range(len(commandes)):
#                             print("coucou")
#                             if(nomplat.lower()==commandes[i]["nom"]):

#                                 newQte=int(plat[3])-int(commandes[i]["qte"])
#                                 plat_with_deux_point=f"{plat[0]}:{plat[1]}:{newQte}"
#                                 break

#                         new_menu.append(plat_with_deux_point)

#             with open(view,"w",encoding="utf-8") as f:
#                 for menu in new_menu:
#                     f.write(f"{menu}\n")
                    

if __name__=="__main__":
    render_view("plat du jour")