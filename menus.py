from assistant import *
from veterinaire import*
from client import *
from patient import *
from medicament import *



##############################################################
                    # Menus #   
##############################################################

def menuAssistant():
    print("""\n Menu assistant :
        1. Afficher la liste des assistants
        2. Ajouter un assistant
        3. Modifier un assistant
        4. Supprimer un assistant
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerAssistants()
        menuAssistant()
    elif choix == "2":
        id = input("Id de l'assistant : ")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        adresse = input("Adresse : ")
        telephone = input("Telephone : ")
        ajouterAssistant(id,nom, prenom, date_naissance, adresse, telephone)
        menuAssistant()
    elif choix == "3":
        assistant_id = input("Id de l'assistant : ")
        new_nom = input("Nouveau nom : ")
        new_prenom = input("Nouveau prenom : ")
        new_date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        new_adresse = input("Nouvelle adresse : ")
        new_telephone = input("Nouveau telephone : ")
        updateAssistant(assistant_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone)
        menuAssistant()
    elif choix == "4":
        nom = input("Nom de l'assistant : ")
        prenom = input("Prenom de l'assistant : ")
        supprimerAssistant(nom,prenom)
        menuAssistant()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        menuAssistant()


def menuClient():
    print(""" Menu client : 
        1. Afficher la liste des clients 
        2. Ajouter un client 
        3. Modifier un client 
        4. Supprimer un client 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerClients()
        menuClient()
    elif choix == "2":
        id = input("Id du client : ")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        adresse = input("Adresse : ")
        telephone = input("Telephone : ")
        t = input("Type : ")
        ajouterClient(id, nom, prenom, date_naissance, adresse, telephone,t)
        menuClient()
    elif choix == "3":
        client_id = input("Id du client : ")
        new_nom = input("Nouveau nom : ")
        new_prenom = input("Nouveau prenom : ")
        new_date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        new_adresse = input("Nouvelle adresse : ")
        new_telephone = input("Nouveau telephone : ")
        updateClient(client_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone)
        menuClient()
    elif choix == "4":
        nom = input("Nom du client : ")
        prenom = input("Prenom du client : ")
        supprimerClient(nom,prenom)
        menuClient()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        menuClient()



def menuPatient():
    print("""\n Menu patient :
        1. Afficher la liste des patients 
        2. Ajouter un patient 
        3. Modifier un patient 
        4. Supprimer un patient 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerPatients()
        menuPatient()
    elif choix == "2":
        id = input("Id du patient : ")
        nom = input("Nom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        puce = input("Puce d'identification : ")
        passeport = input("Numéro de passeport : ")
        espece = input("Espece : ")
        dossier = input("Dossier : ")
        ajouterPatient(id, nom, date_naissance, puce, passeport, espece, dossier)
        menuPatient()
    elif choix == "3":
        id = input("Nouvel id du patient : ")
        nom = input("Nouveau nom : ")
        date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        puce = input("Nouvelle puce d'identification : ")
        passeport = input("Nouveau Numéro de passeport : ")
        espece = input("Nouvelle espèce : ")
        dossier = input("Nouvel id de dossier : ")
        updatePatient(id, nom, date_naissance, puce, espece, dossier)
        menuPatient()
    elif choix == "4":
        id = input("Id du patient : ")
        supprimerPatient(id)
        menuPatient()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        menuPatient()


def menuVeterinaire():
    print(""" Menu vétérinaire : 
        1. Afficher la liste des vétérinaires 
        2. Ajouter un vétérinaire 
        3. Modifier un vétérinaire 
        4. Supprimer un vétérinaire 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerVeterinaires()
        menuVeterinaire()
    elif choix == "2":
        id = input("Id du vétérinaire : ")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        adresse = input("Adresse : ")
        telephone = input("Telephone : ")
        specialite = input("Specialite : ")
        ajouterVeterinaire(id, nom, prenom, date_naissance, adresse, telephone, specialite)
        menuVeterinaire()
    elif choix == "3":
        veterinaire_id = input("Id du vétérinaire : ")
        new_nom = input("Nouveau nom : ")
        new_prenom = input("Nouveau prenom : ")
        new_date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        new_adresse = input("Nouvelle adresse : ")
        new_telephone = input("Nouveau telephone : ")
        new_specialite = input("Nouvelle specialite : ")
        updateVeterinaire(veterinaire_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone, new_specialite)
        menuVeterinaire()
    elif choix == "4":
        nom = input("Nom du vétérinaire : ")
        prenom = input("Prenom du vétérinaire : ")
        supprimerVeterinaire(nom,prenom)
        menuVeterinaire()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        menuVeterinaire()


def menuMedicament():
    print("""\n Menu médicament : 
        1. Afficher la liste des médicaments 
        2. Ajouter un médicament 
        3. Modifier un médicament 
        4. Supprimer un médicament 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerMedicaments()
        menuMedicament()
    elif choix == "2":
        molecule = input("Nom : ")
        description = input("Prenom : ")
        ajouterMedicament(molecule,description)
        menuMedicament()
    elif choix == "3":
        molecule = input("Nouvelle molécule : ")
        description = input("Nouvelle description : ")
        updateMedicament(molecule,description)
        menuMedicament()
    elif choix == "4":
        molecule = input("Nom de l'assistant : ")
        description = input("Prenom de l'assistant : ")
        supprimerMedicament(molecule,description)
        menuMedicament()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        menuMedicament()

def menuGestionnaire():
    print(""" Menu gestionnaire :
        1. Gerer les assistants 
        2. Gerer les vétérinaires 
        3. Gerer les patients 
        4. Gerer les clients 
        5. Gerer les médicamennts
        6. Quitter \n """) 
    choix = input("Votre choix : ")
    if choix == "1":
        menuAssistant()
    elif choix == "2":
        menuVeterinaire()
    elif choix == "3":
        menuPatient()
    elif choix == "4":
        menuClient()
    elif choix == "5":
        menuMedicament()
    elif choix == "6":
        print("Au revoir !")
        return
    else:
        print("Erreur de saisie.")
        menuGestionnaire()
