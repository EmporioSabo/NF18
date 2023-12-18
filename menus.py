from assistant import *
from veterinaire import*
from client import *
from patient import *
from medicament import *
from dossierMedical import *



##############################################################
                    # Menus #   
##############################################################

def gererAssistant():
    print("""\n Gérer les assistants :
        1. Afficher la liste des assistants
        2. Ajouter un assistant
        3. Modifier un assistant
        4. Supprimer un assistant
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerAssistants()
        gererAssistant()
    elif choix == "2":
        id = input("Id de l'assistant : ")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        adresse = input("Adresse : ")
        telephone = input("Telephone : ")
        ajouterAssistant(id,nom, prenom, date_naissance, adresse, telephone)
        gererAssistant()
    elif choix == "3":
        assistant_id = input("Id de l'assistant : ")
        new_nom = input("Nouveau nom : ")
        new_prenom = input("Nouveau prenom : ")
        new_date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        new_adresse = input("Nouvelle adresse : ")
        new_telephone = input("Nouveau telephone : ")
        updateAssistant(assistant_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone)
        gererAssistant()
    elif choix == "4":
        nom = input("Nom de l'assistant : ")
        prenom = input("Prenom de l'assistant : ")
        supprimerAssistant(nom,prenom)
        gererAssistant()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        gererAssistant()


def gererClient():
    print(""" Gérer les clients : 
        1. Afficher la liste des clients 
        2. Ajouter un client 
        3. Modifier un client 
        4. Supprimer un client 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerClients()
        gererClient()
    elif choix == "2":
        id = input("Id du client : ")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        adresse = input("Adresse : ")
        telephone = input("Telephone : ")
        t = input("Type : ")
        ajouterClient(id, nom, prenom, date_naissance, adresse, telephone,t)
        gererClient()
    elif choix == "3":
        client_id = input("Id du client : ")
        new_nom = input("Nouveau nom : ")
        new_prenom = input("Nouveau prenom : ")
        new_date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        new_adresse = input("Nouvelle adresse : ")
        new_telephone = input("Nouveau telephone : ")
        updateClient(client_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone)
        gererClient()
    elif choix == "4":
        nom = input("Nom du client : ")
        prenom = input("Prenom du client : ")
        supprimerClient(nom,prenom)
        gererClient()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        gererClient()



def gererPatient():
    print("""\n Gérer les patients :
        1. Afficher la liste des patients 
        2. Ajouter un patient 
        3. Modifier un patient 
        4. Supprimer un patient 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerPatients()
        gererPatient()
    elif choix == "2":
        id = input("Id du patient : ")
        nom = input("Nom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        puce = input("Puce d'identification : ")
        passeport = input("Numéro de passeport : ")
        espece = input("Espece : ")
        dossier = input("Dossier : ")
        ajouterPatient(id, nom, date_naissance, puce, passeport, espece, dossier)
        gererPatient()
    elif choix == "3":
        id = input("Nouvel id du patient : ")
        nom = input("Nouveau nom : ")
        date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        puce = input("Nouvelle puce d'identification : ")
        passeport = input("Nouveau Numéro de passeport : ")
        espece = input("Nouvelle espèce : ")
        dossier = input("Nouvel id de dossier : ")
        updatePatient(id, nom, date_naissance, puce, espece, dossier)
        gererPatient()
    elif choix == "4":
        id = input("Id du patient : ")
        supprimerPatient(id)
        gererPatient()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        gererPatient()


def gererVeterinaire():
    print(""" Gérer les vétérinaires : 
        1. Afficher la liste des vétérinaires 
        2. Ajouter un vétérinaire 
        3. Modifier un vétérinaire 
        4. Supprimer un vétérinaire 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerVeterinaires()
        gererVeterinaire()
    elif choix == "2":
        id = input("Id du vétérinaire : ")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
        adresse = input("Adresse : ")
        telephone = input("Telephone : ")
        specialite = input("Specialite : ")
        ajouterVeterinaire(id, nom, prenom, date_naissance, adresse, telephone, specialite)
        gererVeterinaire()
    elif choix == "3":
        veterinaire_id = input("Id du vétérinaire : ")
        new_nom = input("Nouveau nom : ")
        new_prenom = input("Nouveau prenom : ")
        new_date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) : ")
        new_adresse = input("Nouvelle adresse : ")
        new_telephone = input("Nouveau telephone : ")
        new_specialite = input("Nouvelle specialite : ")
        updateVeterinaire(veterinaire_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone, new_specialite)
        gererVeterinaire()
    elif choix == "4":
        nom = input("Nom du vétérinaire : ")
        prenom = input("Prenom du vétérinaire : ")
        supprimerVeterinaire(nom,prenom)
        gererVeterinaire()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        gererVeterinaire()


def gererMedicament():
    print("""\n Gérer les médicaments : 
        1. Afficher la liste des médicaments 
        2. Ajouter un médicament 
        3. Modifier un médicament 
        4. Supprimer un médicament 
        5. Retour \n""")
    choix = input("Votre choix : ")
    if choix == "1":
        listerMedicaments()
        gererMedicament()
    elif choix == "2":
        molecule = input("Nom : ")
        description = input("Prenom : ")
        ajouterMedicament(molecule,description)
        gererMedicament()
    elif choix == "3":
        molecule = input("Nouvelle molécule : ")
        description = input("Nouvelle description : ")
        updateMedicament(molecule,description)
        gererMedicament()
    elif choix == "4":
        molecule = input("Nom de l'assistant : ")
        description = input("Prenom de l'assistant : ")
        supprimerMedicament(molecule,description)
        gererMedicament()
    elif choix == "5":
        menuGestionnaire()
    else:
        print("Erreur de saisie.")
        gererMedicament()

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
        gererAssistant()
    elif choix == "2":
        gererVeterinaire()
    elif choix == "3":
        gererPatient()
    elif choix == "4":
        gererClient()
    elif choix == "5":
        gererMedicament()
    elif choix == "6":
        print("Au revoir !")
        return
    else:
        print("Erreur de saisie.")
        menuGestionnaire()

def menuVeterinaire():
    print(""" Menu vétérinaire :
        1. Lister les consultations
        2. Lister les résultats d'analyse
        3. Ajouter une consultation 
        4. Modifier une consultation 
        5. Supprimer une consultation
        6. Quitter \n """) 
    choix = input("Votre choix : ")
    if choix == "1":
        listerConsultations()
        menuVeterinaire()
    elif choix == "2":
        listerResultats()
        menuVeterinaire()
    elif choix == "3":
        id = input("Id de la consultation à ajouter")
        dossier = input("Id du dossier lié à la consultation : ")
        observation = input("Observation : ")
        dateSaisie = input("Date de la consultation (AAAA-MM-JJ)")
        veterinaire = input("Id du vétérinaire ayant effectué la consultation : ")
        ajouterConsultation(id,dossier,observation,dateSaisie,veterinaire)
        menuVeterinaire()
    elif choix == "4":
        id = input("Id de la consultation à modifier")
        dossier = input("Nouvel id du dossier lié à la consultation : ")
        observation = input("Nouvelle observation : ")
        dateSaisie = input("Nouvelle date de la consultation (AAAA-MM-JJ)")
        veterinaire = input("Nouvel id du vétérinaire ayant effectué la consultation : ")
        updateConsultation(id,dossier,observation,dateSaisie,veterinaire)
        menuVeterinaire()
    elif choix == "5":
        id = input("Id de la consultation à supprimer")
        supprimerConsultation(id)
        menuVeterinaire()
    elif choix == "6":
        print("Au revoir !")
        return
    else:
        print("Erreur de saisie.")
        menuVeterinaire()

def menuAssistant():
    print(""" Menu Assistant :
        1. Lister les assistants 
        2. Lister les résultats d'analyse 
        3. Quitter \n """) 
    choix = input("Votre choix : ")
    if choix == "1":
        listerConsultations()
        menuAssistant()
    elif choix == "2":
        listerResultats()
        menuAssistant()
    elif choix == "3":
        print("Au revoir !")
        return
    else:
        print("Erreur de saisie.")
        menuAssistant()
