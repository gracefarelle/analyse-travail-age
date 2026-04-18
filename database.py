import sqlite3
import pandas as pd

DB_NAME = "travailleurs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS travailleurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER NOT NULL,
            experience INTEGER NOT NULL,
            poste TEXT NOT NULL,
            salaire REAL,
            satisfaction INTEGER CHECK(satisfaction BETWEEN 1 AND 5),
            niveau_etudes TEXT,
            secteur TEXT,
            teletravail INTEGER CHECK(teletravail BETWEEN 0 AND 5),
            genre TEXT,
            ville TEXT,
            heures_semaine INTEGER,
            temps_partiel BOOLEAN,
            heures_sup INTEGER,
            trajet_minutes INTEGER,
            conges_annuels INTEGER,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def inserer_donnees(age, experience, poste, salaire, satisfaction,
                    niveau_etudes, secteur, teletravail, genre, ville,
                    heures_semaine, temps_partiel, heures_sup, trajet_minutes, conges_annuels):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO travailleurs (
            age, experience, poste, salaire, satisfaction,
            niveau_etudes, secteur, teletravail, genre, ville,
            heures_semaine, temps_partiel, heures_sup, trajet_minutes, conges_annuels
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (age, experience, poste, salaire, satisfaction,
          niveau_etudes, secteur, teletravail, genre, ville,
          heures_semaine, temps_partiel, heures_sup, trajet_minutes, conges_annuels))
    conn.commit()
    conn.close()

def recuperer_tous():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM travailleurs", conn)
    conn.close()
    return df