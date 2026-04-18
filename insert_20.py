import sqlite3
from database import DB_NAME

data = [
    (24,2,"Développeur",38000,4,"Bac+5","Privé",4,"H","Paris",40,0,5,30,25),
    (29,6,"Data Scientist",52000,5,"Bac+5","Privé",3,"F","Lyon",42,0,8,20,28),
    (34,10,"Chef de projet",55000,4,"Bac+5","Privé",2,"H","Marseille",45,0,10,35,22),
    (41,15,"DevOps",60000,3,"Bac+5","Privé",5,"H","Toulouse",38,0,2,15,30),
    (48,20,"Développeur",58000,4,"Bac+2","Public",1,"F","Bordeaux",37,0,0,25,32),
    (53,25,"Chef de projet",65000,5,"Bac+5","Public",2,"H","Lille",35,0,0,20,35),
    (59,30,"Autre",62000,4,"Doctorat","Indépendant",0,"H","Nice",30,1,0,10,40),
    (62,35,"DevOps",68000,4,"Bac+5","Privé",0,"F","Strasbourg",32,1,0,15,38),
    (22,1,"Développeur",35000,3,"Bac+2","Privé",5,"H","Nantes",45,0,12,40,20),
    (26,3,"Data Scientist",48000,4,"Bac+5","Privé",4,"F","Montpellier",44,0,10,25,22),
    (31,7,"DevOps",54000,4,"Bac+5","Privé",3,"H","Rennes",42,0,6,30,25),
    (37,12,"Chef de projet",58000,5,"Bac+5","Public",2,"F","Reims",39,0,3,20,28),
    (44,18,"Développeur",56000,3,"Bac+2","Privé",1,"H","Saint‑Étienne",40,0,2,15,27),
    (51,22,"Autre",55000,4,"Bac","Public",0,"F","Le Havre",33,0,0,10,34),
    (56,28,"Data Scientist",70000,5,"Doctorat","Privé",1,"H","Grenoble",36,0,0,12,30),
    (63,38,"Chef de projet",72000,4,"Bac+5","Indépendant",0,"F","Dijon",28,1,0,5,42),
    (27,4,"DevOps",50000,4,"Bac+5","Privé",4,"H","Paris",46,0,15,35,18),
    (33,8,"Développeur",47000,4,"Bac+2","Privé",3,"F","Lyon",41,0,7,22,24),
    (45,16,"Data Scientist",64000,4,"Bac+5","Public",2,"H","Toulouse",40,0,4,18,26),
    (60,32,"Autre",60000,5,"Bac+5","Public",1,"F","Marseille",31,0,0,8,36)
]

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
for d in data:
    c.execute('''INSERT INTO travailleurs (
        age, experience, poste, salaire, satisfaction,
        niveau_etudes, secteur, teletravail, genre, ville,
        heures_semaine, temps_partiel, heures_sup, trajet_minutes, conges_annuels
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', d)
conn.commit()
conn.close()
print("20 participants insérés avec succès.")