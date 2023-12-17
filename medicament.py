import connexion


##############################################################
                    # Gestion Medicaments #
##############################################################

def listerMedicaments():
    """
    Fonction qui affiche la liste des médicaments.
    """
    conn = connexion.connexion()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM Medicament;")
    rows = cur.fetchall()
    print("Liste des patients :")
    for row in rows:
        print(row)
    connexion.deconnexion(conn)

def ajouterMedicament(molecule,description):
    """
    Fonction qui ajoute un médicament.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Medicament(molecule,description) VALUES (%s, %s);
    """, (molecule, description))

    conn.commit()
    print("Le médicament a été ajouté avec succès.")

    connexion.deconnexion(conn)

def updateMedicament(molecule,description):
    """
    Fonction qui met à jour les informations d'un client.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        UPDATE Medicament
        SET molecule = %s, description = %s
        WHERE molecule = %s;
    """, (molecule,description,molecule))

    conn.commit()
    print("Les informations du médicament ont été mises à jour avec succès.")

    connexion.deconnexion(conn)

def supprimerMedicament(molecule): 
    """
    Fonction qui supprime un médicament.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        DELETE FROM Medicament
        WHERE molecule = %s;
    """, (molecule))
    if cur.rowcount == 0:
        print("Le médicament n'existe pas.")
        return
    else :
        conn.commit()
        print("Le médicament a été supprimé avec succès.")
    
    connexion.deconnexion(conn)
