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

saisir_entier(1,5)