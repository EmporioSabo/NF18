#!/usr/bin/python3

import psycopg2

def afficheVeterinaire(conn, id):

  cur = conn.cursor()
  sql = "SELECT id, nom, prenom, espece AS specialite FROM Veterinaire JOIN SpecialiteVeterinaire ON (id = veterinaire) WHERE id=%d;" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  prenom = raw[2]
  specialite = raw[3]
  print ("Prénom : %s Nom : %s Spécialité : %s" % (prenom, nom, specialite))

def affichePatient(conn, id):

  cur = conn.cursor()
  sql = "SELECT id , nom , dateNaissance, espece FROM Patient WHERE id=%d;" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  dateNaissance = raw[2]
  espece = raw[3]
  print ("Nom : %s Date de naissance : %s Espece : %s" % (nom, dateNaissance,espece))


def insereVeterinaire(conn, id,nom,prenom,dateNaissance,adresse,telephone):

  cur = conn.cursor()
  sql = "INSERT INTO Veterinaire(id,nom,prenom,dateNaissance,adresse,telephone) VALUES (0,'Macron','Emmanuel','1977-12-21','55 rue du Faubourg-Saint-Honoré 75008 Paris', 0654736719);" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  prenom = raw[2]
  specialite = raw[3]
  print ("Prénom : %s Nom : %s Spécialité : %s" % (prenom, nom, specialite))

def insereAssistant(conn, id):

  cur = conn.cursor()
  sql = "INSERT INTO Assistant(id,nom,prenom,dateNaissance,adresse,telephone) VALUES (0,'Biden','Joe','1942-11-20','The White House 1600 Pennsylvania Avenue NW Washington',+1667453421);" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  prenom = raw[2]
  specialite = raw[3]
  print ("Prénom : %s Nom : %s Spécialité : %s" % (prenom, nom, specialite))

def insereClient(conn, id):

  cur = conn.cursor()
  sql = "INS id, nom, prenom, espece AS specialite FROM Veterinaire JOIN SpecialiteVeterinaire ON (id = veterinaire) WHERE id=%d;" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  prenom = raw[2]
  specialite = raw[3]
  print ("Prénom : %s Nom : %s Spécialité : %s" % (prenom, nom, specialite))

def inserePatient(conn, id):

  cur = conn.cursor()
  sql = "SELECT id, nom, prenom, espece AS specialite FROM Veterinaire JOIN SpecialiteVeterinaire ON (id = veterinaire) WHERE id=%d;" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  prenom = raw[2]
  specialite = raw[3]
  print ("Prénom : %s Nom : %s Spécialité : %s" % (prenom, nom, specialite))

def insereMedicament(conn, id):

  cur = conn.cursor()
  sql = "SELECT id, nom, prenom, espece AS specialite FROM Veterinaire JOIN SpecialiteVeterinaire ON (id = veterinaire) WHERE id=%d;" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  prenom = raw[2]
  specialite = raw[3]
  print ("Prénom : %s Nom : %s Spécialité : %s" % (prenom, nom, specialite))

def insererPersonnel(conn, id):

  cur = conn.cursor()
  sql = "SELECT id, nom, prenom, espece AS specialite FROM Veterinaire JOIN SpecialiteVeterinaire ON (id = veterinaire) WHERE id=%d;" % id
  cur.execute(sql)
  raw = cur.fetchone()
  nom = raw[1]
  prenom = raw[2]
  specialite = raw[3]
  print ("Prénom : %s Nom : %s Spécialité : %s" % (prenom, nom, specialite))