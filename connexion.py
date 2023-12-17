import psycopg2

HOST = "tuxa.sme.utc"
USER = "nf18a063"
PASSWORD = "4xN6OyUtdyA8"
DATABASE = "dbnf18a063"

def connexion():
    """
    Fonction qui permet de se connecter à la base de données.
    """
    try:
        conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        return conn
    except psycopg2.Error as e:
        print("Erreur lors de la connexion à la base de données : ", e)
        return None
    
def deconnexion(conn):
    """
    Fonction qui permet de se déconnecter de la base de données.
    """
    try:
        conn.close()
    except psycopg2.Error as e:
        print("Erreur lors de la déconnexion à la base de données : ", e)



