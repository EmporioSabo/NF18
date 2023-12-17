import connexion

##############################################################   
                 # Gerer assistant # 
##############################################################

def ajouterAssistant(id, nom, prenom, date_naissance, adresse, telephone):
    """
    Fonction qui ajoute un assistant.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Assistant (id, nom, prenom, dateNaissance, adresse, telephone)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (id, nom, prenom, date_naissance, adresse, telephone))

    conn.commit()
    print("L'assistant a été ajouté avec succès.")

    connexion.deconnexion(conn)


def listerAssistants():
    """
    Fonction qui affiche la liste des assistants.
    """
    conn = connexion.connexion()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM Assistant;")
    rows = cur.fetchall()
    print("Liste des assistants :")
    for row in rows:
        print(row)
    connexion.deconnexion(conn)


def updateAssistant(assistant_id, new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone):
    """
    Fonction qui met à jour les informations d'un assistant.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        UPDATE Assistant
        SET nom = %s, prenom = %s, dateNaissance = %s, adresse = %s, telephone = %s
        WHERE id = %s;
    """, (new_nom, new_prenom, new_date_naissance, new_adresse, new_telephone, assistant_id))

    conn.commit()
    print("Les informations de l'assistant ont été mises à jour avec succès.")

    connexion.deconnexion(conn)


def supprimerAssistant(nom,prenom): 
    """
    Fonction qui supprime un assistant.
    """
    conn = connexion.connexion()
    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        DELETE FROM Assistant
        WHERE nom = %s AND prenom = %s;
    """, (nom,prenom))
    if cur.rowcount == 0:
        print("L'assistant n'existe pas.")
        return
    else :
        conn.commit()
        print("L'assistant a été supprimé avec succès.")
    

    connexion.deconnexion(conn)

