import os
from genericpath import exists

def yesNoQuestion(question:str)->bool :
    rep=input(f"{question} ? [Oui /Non] \n")
    while(rep.lower() not in('oui','non')):
        rep=input(f"Votre choix est incomprehensible,refaite une nouvelle saisie\n")
    return rep.lower()=="oui"
        

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
        f=open(fichier,"w",encoding="utf-8")
        f.close()

def saisir_entier(min:int,max:int,expression="Faite un choix\n"):

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