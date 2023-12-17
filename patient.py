import connexion

##############################################################
                    # Gerer Patients #
##############################################################
    
def listerPatients():
    """
    Fonction qui affiche la liste des patients.
    """
    conn = connexion.connexion()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patient;")
    rows = cur.fetchall()
    print("Liste des patients :")
    for row in rows:
        print(row)
    connexion.deconnexion(conn)

def ajouterPatient(id, nom, date_naissance, puceIdentification, numeroPasseport, espece, dossier):
    """
    Fonction qui ajoute un patient.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Patient (id, nom, dateNaissance,puceIdentification, numeroPasseport, espece,dossier)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (id, nom, date_naissance, puceIdentification, numeroPasseport, espece,dossier))

    conn.commit()
    print("Le patient a été ajouté avec succès.")

    connexion.deconnexion(conn)

def updatePatient(id, nom, date_naissance, numeroPasseport,puceIdentification, espece, dossier):
    """
    Fonction qui met à jour les informations d'un patient.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        UPDATE Patient
        SET nom = %s, dateNaissance = %s, numeroPasseport = %s, puceIdentification = %s, espece = %s, dossier = %s
        WHERE id = %s;
    """, (nom, date_naissance, numeroPasseport,puceIdentification, espece, dossier, id))

    conn.commit()
    print("Les informations du patient ont été mises à jour avec succès.")

    connexion.deconnexion(conn)


def supprimerPatient(nom): 
    """
    Fonction qui supprime un patient.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        DELETE FROM Patient
        WHERE id = %s;
    """, (nom))
    if cur.rowcount == 0:
        print("Le patient n'existe pas.")
        return
    else :
        conn.commit()
        print("Le patient a été supprimé avec succès.")
    
    connexion.deconnexion(conn)

