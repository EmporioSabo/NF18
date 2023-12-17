DROP TABLE IF EXISTS Prescription;
DROP TABLE IF EXISTS MedicamentEspece;
DROP TABLE IF EXISTS Medicament;
DROP TABLE IF EXISTS Possession;
DROP TABLE IF EXISTS Proprietaire;
DROP TABLE IF EXISTS Suivi;
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS Traitement;
DROP TABLE IF EXISTS Mesure;
DROP TABLE IF EXISTS Resultat;
DROP TABLE IF EXISTS Procedure;
DROP TABLE IF EXISTS Consultation;
DROP TABLE IF EXISTS DossierMedical;
DROP TABLE IF EXISTS SpecialiteAssistant;
DROP TABLE IF EXISTS SpecialiteVeterinaire;
DROP TABLE IF EXISTS Espece;
DROP TABLE IF EXISTS Assistant;
DROP TABLE IF EXISTS Veterinaire;
DROP TYPE IF EXISTS TYPEESPECE;

CREATE TABLE Veterinaire ( 
	id INTEGER  PRIMARY KEY, 
	nom  VARCHAR(50) NOT  NULL, 
	prenom  VARCHAR(50) NOT  NULL, 
	dateNaissance DATE NOT  NULL, 
	adresse VARCHAR(255) NOT  NULL, 
	telephone VARCHAR(20) NOT  NULL
);

CREATE TABLE Assistant (
	id INTEGER  PRIMARY KEY , 
	nom  VARCHAR(50) NOT  NULL, 
	prenom  VARCHAR(50) NOT  NULL, 
	dateNaissance DATE NOT  NULL, 
	adresse VARCHAR(255) NOT  NULL, 
	telephone VARCHAR(20) NOT  NULL
);

CREATE TYPE TypeEspece AS ENUM ('félin','canidé','reptile','rongeur','oiseau','autre');
 
CREATE TABLE Espece (
	nomEspece TypeEspece PRIMARY KEY
); 


CREATE TABLE SpecialiteVeterinaire ( 
	espece TypeEspece REFERENCES Espece(nomEspece), 
	veterinaire INTEGER REFERENCES Veterinaire(id), 
	PRIMARY KEY (espece, veterinaire) 
 );
CREATE TABLE SpecialiteAssistant ( 
	espece TypeEspece REFERENCES Espece(nomEspece), 
	assistant INTEGER REFERENCES Assistant(id), 
	PRIMARY KEY (espece,assistant)
);

CREATE TABLE DossierMedical (
	id INTEGER PRIMARY KEY
);

CREATE TABLE Consultation (
	id INTEGER,
	dossier INTEGER,
	observation VARCHAR(255),
	dateSaisie TIMESTAMP NOT NULL,
	veterinaire INTEGER NOT NULL,
	FOREIGN KEY (veterinaire) REFERENCES Veterinaire(id),
	FOREIGN KEY (dossier) REFERENCES DossierMedical(id),
	PRIMARY KEY(id,dossier)
);


CREATE TABLE Procedure (
	id int PRIMARY KEY,
	dateSaisie TIMESTAMP NOT NULL,
	description VARCHAR(255) NOT NULL,
	dossier INTEGER NOT NULL,
	consultation INTEGER NOT NULL,
	FOREIGN KEY (consultation, dossier) 



REFERENCES Consultation(id,dossier)
);

CREATE TABLE Mesure ( 
	id int PRIMARY KEY,
	dateSaisie TIMESTAMP NOT NULL, 
	taille float NOT NULL, 
	poids float NOT NULL, 
	dossier INTEGER NOT NULL,
	consultation INTEGER NOT NULL,
	FOREIGN KEY (consultation, dossier) REFERENCES Consultation(id,dossier)
); 

CREATE TABLE Resultat (
	id int PRIMARY KEY,
	lien VARCHAR(255),
	dateSaisie TIMESTAMP NOT NULL,
	procedure INTEGER NOT NULL,
	FOREIGN KEY (procedure) REFERENCES Procedure(id)
);


CREATE TABLE Traitement( 
	id INTEGER PRIMARY KEY,
	description VARCHAR(255) NOT NULL,
	dateSaisie TIMESTAMP NOT NULL, 
	dossier INTEGER NOT NULL,
	consultation INTEGER NOT NULL,
	veterinaire INTEGER NOT NULL REFERENCES Veterinaire(id),  
	FOREIGN KEY (consultation,dossier) REFERENCES Consultation(id,dossier)
); 


CREATE TABLE Patient (
	id INTEGER PRIMARY KEY,
	nom VARCHAR(50) NOT NULL,
	dateNaissance DATE NOT NULL,
	puceIdentification CHAR(15),
	numeroPasseport CHAR(10),
	espece TypeEspece NOT NULL,
	dossier INTEGER UNIQUE NOT NULL,
	FOREIGN KEY (espece) REFERENCES Espece(nomEspece),
	FOREIGN KEY (dossier) REFERENCES DossierMedical(id)
);

CREATE TABLE Suivi (
	dateSuivi DATE,
	veterinaire INTEGER,
	patient INTEGER,
	FOREIGN KEY (veterinaire) REFERENCES Veterinaire(id),
	FOREIGN KEY (patient) REFERENCES Patient(id),
	PRIMARY KEY (dateSuivi,veterinaire, patient)
);

CREATE TABLE Proprietaire (
	id INTEGER PRIMARY KEY,
	nom VARCHAR(50) NOT NULL,
	prenom VARCHAR(50) NOT NULL,
	dateNaissance DATE,
	adresse VARCHAR(255),
	telephone VARCHAR(20),
	t CHAR(1) NOT NULL,
	CHECK((t='C' AND (telephone IS NOT NULL) and (dateNaissance IS NOT NULL) and (adresse IS NOT NULL)) OR (t = 'P'))
);

CREATE TABLE Possession(
	dateDebut DATE,
	dateFin DATE,
	proprietaire INTEGER,
	patient INTEGER,
    CHECK ((dateFin IS NULL) OR (dateFin > dateDebut)), 
	FOREIGN KEY (proprietaire) REFERENCES Proprietaire(id),
	FOREIGN KEY (patient) REFERENCES Patient(id), 
	PRIMARY KEY (dateDebut, proprietaire,patient)
);

CREATE TABLE Medicament (
	molecule VARCHAR(100) PRIMARY KEY,
	description VARCHAR(255)
);

CREATE TABLE MedicamentEspece (
	espece TypeEspece,
	medicament VARCHAR(100),
	FOREIGN KEY (espece) REFERENCES Espece(nomEspece),
	FOREIGN KEY (medicament) REFERENCES Medicament(molecule),
	PRIMARY KEY (espece, medicament)
);

CREATE TABLE Prescription (
	quantite INTEGER NOT NULL,
	dateDebut DATE NOT NULL, 
	duree INTEGER NOT  NULL,
	traitement INTEGER,
	medicament VARCHAR(100),
	FOREIGN KEY (traitement) REFERENCES Traitement(id),
	FOREIGN KEY (medicament) REFERENCES Medicament(molecule),
	PRIMARY KEY (traitement, medicament)
);