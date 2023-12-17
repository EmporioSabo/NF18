-- Sélectionner les Vétérinaires aVec leurs spécialités :

SELECT id, nom, prenom, espece AS specialite
FROM Veterinaire JOIN SpecialiteVeterinaire ON (id = Veterinaire);

-- Nombre de consultations effectuées par chaque vétérinaire :

SELECT V.id, V.nom, V.prenom, COUNT(C.id) AS nbConsultations
FROM Veterinaire V JOIN Consultation C ON (V.id = C.Veterinaire)
GROUP BY V.id, V.nom, V.prenom;

-- Nombre de traitements reçus pour chaque espèce : 

SELECT P.espece, COUNT(T.id) AS nbTraitements
FROM Patient P JOIN DossierMedical D ON (P.dossier = D.id) JOIN Consultation C ON (D.id = C.dossier) JOIN Traitement T ON (C.id = T.consultation) AND (C.dossier = T.dossier)
GROUP BY P.espece;

-- Nombre de traitements effectués dans la clinique : 

SELECT COUNT(*) AS nbTraitements
FROM Traitement;

-- Nombre de procédures effectuées dans la clinique : 

SELECT COUNT(*) AS nbProcedures
FROM Procedure;


-- Quantités consommée par médicament : 

SELECT medicament, SUM(quantite)
FROM Prescription JOIN Medicament ON (medicament = molecule)
GROUP BY medicament;

-- Lister les patients de la clinique : 

SELECT id , nom , dateNaissance, espece
FROM Patient;

-- Liste des vétérinaires qui n’ont suivi aucun patient : 

SELECT id,nom, prenom
FROM Veterinaire  LEFT JOIN Suivi ON id = Veterinaire
WHERE Veterinaire IS NULL;

-- Liste des médicaments par ordre décroissant de quantité totale prescrite :

SELECT medicament AS Medicament, SUM(quantite) AS qteTotale
FROM Prescription
GROUP BY medicament
ORDER BY qteTotale DESC;

-- Nombre de consultations effectuées par chaque patient : 

SELECT P.id, P.nom, COUNT(C.id) AS nbConsultations
FROM Patient P JOIN DossierMedical D ON P.dossier = D.id JOIN Consultation C ON D.id = C.dossier
GROUP BY P.id, P.nom;

-- Obtenir la durée moyenne d’un traitement prescrit :
 
SELECT AVG(duree) AS dureeMoyenne
FROM Prescription;


-- Obtenir le nombre de patients ayant une puce d’identification : 

SELECT COUNT(puceIdentification) as nbPuces
FROM Patient
WHERE puceIdentification IS NOT NULL;

-- Liste des traitements pour lesquels aucun médicament n’est prescrit :

SELECT id, description
FROM Traitement LEFT JOIN Prescription ON id = traitement
WHERE traitement IS NULL;
