INSERT INTO Veterinaire(id,nom,prenom,dateNaissance,adresse,telephone) VALUES (0,'Macron','Emmanuel','1977-12-21','55 rue du Faubourg-Saint-Honoré 75008 Paris', 0654736719); 
INSERT INTO Veterinaire(id,nom,prenom,dateNaissance,adresse,telephone) VALUES (1,'Borne','Elisabeth','1961-04-18','Hôtel de Matignon, 57, rue de Varenne 75007 Paris', 0654667898); 

INSERT INTO Assistant(id,nom,prenom,dateNaissance,adresse,telephone) VALUES (0,'Biden','Joe','1942-11-20','The White House 1600 Pennsylvania Avenue NW Washington',+1667453421);
INSERT INTO Assistant(id,nom,prenom,dateNaissance,adresse,telephone) VALUES (1,'Harris','Kamala','1964-10-20','Number One Observatory Circle (Washington D.C.)',+187998765); 

INSERT INTO Espece VALUES ('canidé');
INSERT INTO Espece VALUES ('reptile');
INSERT INTO Espece VALUES ('félin');
INSERT INTO Espece VALUES ('rongeur');
INSERT INTO Espece VALUES ('oiseau');
INSERT INTO Espece VALUES ('autre');

INSERT INTO SpecialiteVeterinaire(espece,veterinaire) VALUES ('félin',0);
INSERT INTO SpecialiteVeterinaire(espece,veterinaire) VALUES ('canidé',1);

INSERT INTO SpecialiteAssistant(espece,assistant) VALUES ('rongeur',0);
INSERT INTO SpecialiteAssistant(espece,assistant) VALUES ('reptile',1);

INSERT INTO DossierMedical VALUES (0);
INSERT INTO DossierMedical VALUES (1);

INSERT INTO Consultation(id,dossier,observation,dateSaisie,veterinaire) VALUES (0,0,'Patte blessée',NOW(),0);
INSERT INTO Consultation(id,dossier,observation,dateSaisie,veterinaire) VALUES(1,0,NULL,NOW()+interval '1 hour',1);
INSERT INTO Consultation(id,dossier,observation,dateSaisie,veterinaire) VALUES(0,1,'Fracture',NOW()+interval '2 hours',0);


INSERT INTO Procedure(id, dateSaisie, description,dossier,consultation) VALUES (0,NOW(),'Examen du pouls',0,0);
INSERT INTO Procedure(id, dateSaisie, description,dossier,consultation) VALUES (1,NOW()+interval '1 hour','Examen de la tension',0,1);
INSERT INTO Procedure(id, dateSaisie, description,dossier,consultation) VALUES (2,NOW()+interval '2 hours','Analyse du taux de glycémie',1,0);

INSERT INTO Resultat(id,lien,dateSaisie,procedure) VALUES (0,'http://www.resultats.com/pouls/0',NOW(),0);
INSERT INTO Resultat(id,lien,dateSaisie,procedure) VALUES (1,'http://www.resultats.com/pouls/1',NOW()+interval '1 hour' ,0);
INSERT INTO Resultat(id,lien,dateSaisie,procedure) VALUES (2,'http://www.resultats.com/tension/0',NOW()+interval '2 hours' ,1);
INSERT INTO Resultat(id,lien,dateSaisie,procedure) VALUES (3,NULL,NOW()+interval '3 hours' ,2);

INSERT INTO Mesure(id,dateSaisie,taille,poids,dossier,consultation) VALUES (0,NOW(),50.5,8.5,0,0); 
INSERT INTO Mesure(id,dateSaisie,taille,poids,dossier,consultation) VALUES (1,NOW()-interval '15 days',50.5,8.0,0,1);
INSERT INTO Mesure(id,dateSaisie,taille,poids,dossier,consultation) VALUES (2,NOW()-interval '30 days',100.25,13.1,1,0);

INSERT INTO Traitement(id,description,dateSaisie,dossier,consultation,veterinaire) VALUES (0,'Vitamines',NOW(),0,0,0); 
INSERT INTO Traitement(id,description,dateSaisie,dossier,consultation,veterinaire) VALUES (1,'Medicaments',NOW()  + interval '1 hour',0,1,1); 
INSERT INTO Traitement(id,description,dateSaisie,dossier,consultation,veterinaire) VALUES (2,'Vitamines+Medicaments',NOW() + interval '2 hours',1,0,1); 

INSERT INTO Patient(id, nom, dateNaissance,puceIdentification, numeroPasseport, espece,dossier) VALUES (0,'Yuki','2016-08-17', NULL, NULL, 'félin',0);
INSERT INTO Patient(id, nom, dateNaissance,puceIdentification, numeroPasseport, espece,dossier) VALUES (1,'Snoopy','2018-10-19', '250261091827364', NULL, 'canidé',1);

INSERT INTO Suivi(dateSuivi,veterinaire,patient) VALUES('2023-11-11', 0, 0); 
INSERT INTO Suivi(dateSuivi,veterinaire,patient) VALUES('2023-11-11', 1, 0); 
INSERT INTO Suivi(dateSuivi,veterinaire,patient) VALUES('2023-11-11', 0, 1); 
INSERT INTO Suivi(dateSuivi,veterinaire,patient) VALUES('2023-11-11', 1, 1); 

INSERT INTO Proprietaire(id,nom,prenom,dateNaissance,adresse,telephone,t) VALUES (0,'Scholz','Olaf','1958-06-14','1 Willy-Brandt-Straße','+491802721234','C');
INSERT INTO Proprietaire(id,nom,prenom,dateNaissance,adresse,telephone,t) VALUES (1,'Matarella','Sergio',NULL,NULL,NULL,'P');

INSERT INTO Possession(dateDebut,dateFin,proprietaire,patient) VALUES ('2016-11-20','2020-08-21',1,0);
INSERT INTO Possession(dateDebut,dateFin,proprietaire,patient)  VALUES ('2020-08-21',NULL,0,0);
INSERT INTO Possession(dateDebut,dateFin,proprietaire,patient)  VALUES ('2021-09-22',NULL,0,1);

INSERT INTO Medicament(molecule,description) VALUES ('Praziquantel','Elimine les vers'); 
INSERT INTO Medicament(molecule,description)  VALUES ('Oxime de milbémycine','Antiparasitaire'); 

INSERT INTO MedicamentEspece(espece,medicament) VALUES('canidé','Praziquantel');
INSERT INTO MedicamentEspece(espece,medicament) VALUES('canidé','Oxime de milbémycine');
INSERT INTO MedicamentEspece(espece,medicament) VALUES('félin','Praziquantel');

INSERT INTO Prescription(quantite,dateDebut,duree,traitement,medicament) VALUES (1,'2023-11-18',10,1,'Praziquantel');
INSERT INTO Prescription(quantite,dateDebut,duree,traitement,medicament)  VALUES (2,'2023-08-29',30,1,'Oxime de milbémycine');