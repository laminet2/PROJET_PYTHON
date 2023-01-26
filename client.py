#CONSTANTES
MENU_PRINCIPAL_DIRECTORY="MENU PRINCIPAL"
PLAT_DIRECTORY="plat.txt"
VENTES_DIRECTORY="ventes.txt"
DEVISE="FCFA"

#FONCTION
import os
from genericpath import exists
from time import sleep
import sys
from pprint import pprint
from datetime import datetime

#Variable globales 
commandes=[]

def yesNoQuestion(question:str)->bool :
    rep=input(f"{question} ? [Oui /Non] \n")
    while(rep.lower() not in('oui','non')):
        rep=input(f"Votre choix est incomprehensible,refaite une nouvelle saisie\n")
    return rep=="oui"
        

def effacer_ecran():

    """
        cette fonction permet d'effacer l'écran
    """
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')


def creerFichier(nomFichier,ext="txt"):
    fichier=f"{nomFichier}.{ext}"
    if(not exists(fichier)):
        f=open(fichier,"w")
        f.close()

def saisir_entier(min,max,expression="Faite un choix\n"):

    choix=input(expression)
    if choix.isdigit()==True:
        choix=int(choix)
    else:
        print("Votre saisie doit etre un entier")
        return saisir_entier(min,max,expression)
    if(min==max and min<choix) or ((choix>=min and choix<=max)):
        return choix
    else:
        print("Votre saisie n'est pas valide")
        return saisir_entier(min,max,expression)


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
        f=open(nom_du_fichier,"w")
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
        return 0,0

    menu_afficher=find_all_data(view)

    #AFFICHAGE EN TETE
    effacer_ecran()
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


            #TRAITEMENT DU CAS OU LA QTE RESTANTE EST EGALE A 0
            if(qte=='0'):
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
            print(f"{i}{nom.upper():.>40} {prix} {DEVISE} ")
            i+=1

    print(f"{i}{'Retourner':.>50}")

    print(50*"-")

    #partie choix et traitement du choix

    choix=saisir_entier(1,i,"Faites votre choix :\n")
    if i==choix:
        return render_view(MenuPrincipal())

        #je dois recuperer l'indice de l'affichage 
        # de la clé du choix effectuable par enumerate()
    for indice,keys in enumerate(menu_reel_a_afficher):
        if(indice+1 ==choix):
            return keys,menu_reel_a_afficher[keys],view

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

def MenuPrincipal():

    menu_afficher=find_all_data(MENU_PRINCIPAL_DIRECTORY)
    effacer_ecran()
    i=1
    print('*'*50)
    print(f"{MENU_PRINCIPAL_DIRECTORY.upper(): ^50}")
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

    choix=saisir_entier(1,i,"Faites votre choix :\n")

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
    entete=" RESTO DIMENSION ALLOCO "

    #Name fichier ticket
    datenow=datetime.now()
    dateticket=datenow.strftime("%d%m%Y%H%M%S")
    fileticket="ticket/"+dateticket+"txt"

    #reference bas de page
    dateBas_de_page=datenow.strftime("%d/%m/%Y à %H:%M")
    bas_de_page="\nImprimé le "+dateBas_de_page+"       "+" merci"

    #Corp du ticket
    ecriture=""
    somme=0
    with open(fileticket,"r",encoding="utf-8") as f:
        for commande in commandes:
            ecriture=ecriture + commande["nom"] + '(' + commande["qte"] + ')' +"   "+ commande["prix"]*commande["qte"] +"\n"
            somme+=commande['prix']*commande["qte"]

        ecriture+=f"TOTAL:   {somme}"
        f.write(entete)
        f.write(ecriture)
        f.write(bas_de_page)


def uptade_file_vente(commandes):

    ecriture=""
    with open(VENTES_DIRECTORY,"a") as f:
        for commande in commandes:
            ecriture=ecriture+commande["nom"]+";"+commande["qte"]+";"+commande["prix"]+"\n"
        f.write(ecriture)

def soustraction_qte(commandes):

    with open(MENU_PRINCIPAL_DIRECTORY,'r',encoding="utf-8") as f:
        views=f.read().splitlines()

    for view in views:

        view=view.lower().replace(" ","_")
        view=view+"txt"
        new_menu=[]


        with open(view,"r") as f:
                different_plat=f.read().split("\n")
                for plat_with_deux_point in different_plat():
                    plat=plat_with_deux_point.split(":")
                    for i in range(len(commandes)-1):

                        if(plat[0].strip()==commandes[i]["nom"]):
                            newQte=int(plat[3])-int(commandes[i]["qte"])
                            plat_with_deux_point=f"{plat[0]}:{plat[1]}:{newQte}"
                            break

                    new_menu.append(plat_with_deux_point)

        with open(view,"w",encoding="utf-8") as f:
            f.write(new_menu)
                    
#Fonction caisse

def listerVentes():
    with open(VENTES_DIRECTORY,"r",encoding="utf-8") as f:
       line=f.readline()
       while line:
        print(line)
        line=f.readlines()   

def MontantVentes():
    somm=0
    with open(VENTES_DIRECTORY) as f:
        ventes=f.read().splitlines()
        for vente in ventes:
            vente=vente.split(";")
            somm+=int(vente[2].strip())*int(vente[1].strip())
    print(f"la sommes des Ventes d'aujourd'hui vaut {somm}")

#Programme PRINCIPAL caisse
while True:
    print("-"*50)
    entete="menu caise"
    print(f"{entete: .^50}")
    i=1
    action=["Lister la liste des ventes","le montant total des ventes"]
    for poss in action:
        print(f"{i} {poss}")
    choix=saisir_entier(1,i+1,"Faite un choix")
    if(choix>len(action)):
        break
    else:

        if(action[choix]=="Lister la liste des ventes"):
            listerVentes()
        elif(action[choix]=="Le montant total des ventes"):
            MontantVentes()

    if(not yesNoQuestion("Voulez vous retourner au menu Principal ?")):
        break


#Programme principal client
view=None
while True:

    if(view==None):
         PlatName,info,view=render_view((MenuPrincipal()))
    else:
         PlatName,info,view=render_view(view)

    if(PlatName==0):
        #Il a fini il veut sortir  
        break
    else:
        if(yesNoQuestion("Voulez-vous voir les details")):
            details(PlatName)
            if(not yesNoQuestion("Voulez-vous commander ?")):
                continue

        qte_voulue=saisir_entier("entrer le nombre de plat",1,1)

        if(qte_voulue>info["qte"]):
            print("la quantité demandé est superieur au nombre de plat dispo coreespondent à",info["qte"])
            if(yesNoQuestion("Vouliez vous changer la qantite voulue")):
                qte_voulue=saisir_entier("entrer une nouvelle quantite",1,info["qte"])
        
        if(not yesNoQuestion("voulez vous un autre",view)):
            view=None
        
        if(qte_voulue<=info["qte"]):
            commande={"nom":PlatName,"qte":qte_voulue,"prix":info["prix"]}
            commandes.append(commande)

if(commandes!=[]):

    generation_ticket(commandes)
    uptade_file_vente(commandes)
    soustraction_qte(commandes)
    



#le renvoyer keleke part d'autre si le menu n'existe pas
#ProgrammmmmeeeeeeeeeeeeeeeeeeeeeeeeePrinncipppalee

################ ---Burger-----

# if choix_utilisateur>len(menus)-1:
#     #sortir du programme
#     pass
# else:
#     menu_afficher=menus[choix_utilisateur-1]
