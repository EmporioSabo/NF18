import connexion

##############################################################   
                 # Gerer veterinaire #
##############################################################

def listerVeterinaires():
    """
    Fonction qui affiche la liste des vétérinaires.
    """
    conn = connexion.connexion()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM Veterinaire;")
    rows = cur.fetchall()
    print("Liste des vétérinaires :")
    for row in rows:
        print(row)
    connexion.deconnexion(conn)


def updateVeterinaire(veterinaire_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone, new_specialite):
    """
    Fonction qui met à jour les informations d'un vétérinaire.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        UPDATE Veterinaire
        SET nom = %s, prenom = %s, dateNaissance = %s, adresse = %s, telephone = %s, specialite = %s
        WHERE id = %s;
    """, (new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone, new_specialite, veterinaire_id))

    conn.commit()
    print("Les informations du vétérinaire ont été mises à jour avec succès.")

    connexion.deconnexion(conn)


def supprimerVeterinaire(nom,prenom):
    """
    Fonction qui supprime un vétérinaire.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        DELETE FROM Veterinaire
        WHERE nom = %s AND prenom = %s;
    """, (nom,prenom))
    if cur.rowcount == 0:
        print("Le vétérinaire n'existe pas.")
        return
    else :
        conn.commit()
        print("Le vétérinaire a été supprimé avec succès.")
    

    connexion.deconnexion(conn)

def ajouterVeterinaire(id, nom, prenom, date_naissance, adresse, telephone, specialite):
    """
    Fonction qui ajoute un vétérinaire.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Veterinaire (id, nom, prenom, dateNaissance, adresse, telephone, specialite)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (id, nom, prenom, date_naissance, adresse, telephone, specialite))

    conn.commit()
    print("Le vétérinaire a été ajouté avec succès.")

    connexion.deconnexion(conn)

