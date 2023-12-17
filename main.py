import menus
import connexion

def main():
    conn = connexion.connexion()
    PROMPT = """ Quel est votre rôle au sein de la clinique ?
    1. Gestionnaire
    2. Vétérinaire
    3. Assistant
    4. Quitter """
    choix = None
    print("Bienvenue sur le système de gestion de la base de données de la clinique vétérinaire")
    while(choix != "4"):
        choix = input(PROMPT)
        if(choix == "1"):
            menus.menuGestionnaire()
        elif(choix == "2"):
            print("Menu pas encore implémenté")
        elif(choix == "3"):
            print("Menu pas encore implémenté")
        elif(choix == "4"):
            print("Au revoir !")
            connexion.deconnexion(conn)
        else:
            print("Erreur de saisie.")
    
    
if __name__ == '__main__':
    main()