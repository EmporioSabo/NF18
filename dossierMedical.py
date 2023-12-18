import connexion

# INSERT INTO Consultation(id,dossier,observation,dateSaisie,veterinaire) VALUES (0,0,'Patte blessée',NOW(),0);

def ajouterConsultation(id,dossier,observation,dateSaisie,veterinaire):
    """
    Fonction qui ajoute un médicament.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Consultation(id,dossier,observation,dateSaisie,veterinaire) VALUES (%s, %s, %s, %s, %s);
    """, (id,dossier,observation,dateSaisie,veterinaire))

    conn.commit()
    print("La consultation a été ajoutée avec succès.")

    connexion.deconnexion(conn)

def updateConsultation(id,dossier,observation,dateSaisie,veterinaire):
    """
    Fonction qui met à jour les informations d'un client.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        UPDATE Consultation
        SET dossier = %s, observation = %s, dateSaisie = %s, veterinaire = %s
        WHERE id = %s;
    """, (dossier,observation,dateSaisie,veterinaire,id))

    conn.commit()
    print("Les informations de la consultation ont été mises à jour avec succès.")

    connexion.deconnexion(conn)


def supprimerConsultation(id): 
    """
    Fonction qui supprime un médicament.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        DELETE FROM Consultation
        WHERE id = %s;
    """, (id))
    if cur.rowcount == 0:
        print("La consultation n'existe pas.")
        return
    else :
        conn.commit()
        print("La consultation a été supprimée avec succès.")
    
    connexion.deconnexion(conn)


def listerConsultations():
    """
    Fonction qui affiche la liste des consultations.
    """
    conn = connexion.connexion()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM Consultation;")
    rows = cur.fetchall()
    print("Liste des consultations :")
    for row in rows:
        print(row)
    connexion.deconnexion(conn)

def listerResultats():
    """
    Fonction qui affiche la liste des résultats d'analyse.
    """
    conn = connexion.connexion()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM Resultat;")
    rows = cur.fetchall()
    print("Liste des résultats d'analyse :")
    for row in rows:
        print(row)
    connexion.deconnexion(conn)