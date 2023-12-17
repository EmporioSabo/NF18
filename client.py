import connexion

#############################################################
                    # Gerer Clients #   
##############################################################

def listerClients():
    """
    Fonction qui affiche la liste des clients.
    """
    conn = connexion.connexion()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM Proprietaire;")
    rows = cur.fetchall()
    print("Liste des clients :")
    for row in rows:
        print(row)
    connexion.deconnexion(conn)


def ajouterClient(id, nom, prenom, date_naissance, adresse, telephone, t ):
    """
    Fonction qui ajoute un client.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Proprietaire (id, nom, prenom, dateNaissance, adresse, telephone)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (id, nom, prenom, date_naissance, adresse, telephone,t))

    conn.commit()
    print("Le client a été ajouté avec succès.")

    connexion.deconnexion(conn)


def updateClient(client_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone):
    """
    Fonction qui met à jour les informations d'un client.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        UPDATE Proprietaire
        SET nom = %s, prenom = %s, dateNaissance = %s, adresse = %s, telephone = %s
        WHERE id = %s;
    """, (new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone, client_id))

    conn.commit()
    print("Les informations du client ont été mises à jour avec succès.")

    connexion.deconnexion(conn)



def supprimerClient(nom,prenom): 
    """
    Fonction qui supprime un client.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        DELETE FROM Proprietaire
        WHERE nom = %s AND prenom = %s;
    """, (nom,prenom))
    if cur.rowcount == 0:
        print("Le client n'existe pas.")
        return
    else :
        conn.commit()
        print("Le client a été supprimé avec succès.")
    
    connexion.deconnexion(conn)
