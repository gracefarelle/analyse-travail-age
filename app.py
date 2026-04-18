from flask import Flask, render_template, request, redirect, url_for
import database as db
import analyse
import pandas as pd

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('formulaire.html')

@app.route('/collecte', methods=['POST'])
def collecte():
    # Récupération des 15 champs
    age = int(request.form['age'])
    experience = int(request.form['experience'])
    poste = request.form['poste']
    salaire = float(request.form['salaire'])
    satisfaction = int(request.form['satisfaction'])
    niveau_etudes = request.form['niveau_etudes']
    secteur = request.form['secteur']
    teletravail = int(request.form['teletravail'])
    genre = request.form['genre']
    ville = request.form['ville']
    heures_semaine = int(request.form['heures_semaine'])
    temps_partiel = 1 if 'temps_partiel' in request.form else 0
    heures_sup = int(request.form['heures_sup'])
    trajet_minutes = int(request.form['trajet_minutes'])
    conges_annuels = int(request.form['conges_annuels'])
    
    db.inserer_donnees(age, experience, poste, salaire, satisfaction,
                       niveau_etudes, secteur, teletravail, genre, ville,
                       heures_semaine, temps_partiel, heures_sup, trajet_minutes, conges_annuels)
    return redirect(url_for('merci'))

@app.route('/merci')
def merci():
    return "<h2>Merci ! Votre participation a été enregistrée.</h2><a href='/'>Retour à l'accueil</a>"

@app.route('/analyse')
def analyse_page():
    df = db.recuperer_tous()
    if df.empty:
        return "<h2>Aucune donnée pour l'instant.</h2><a href='/'>Collectez d'abord des données</a>"
    
    stats = analyse.statistiques_desc(df)
    graphiques = analyse.generer_graphiques(df)
    return render_template('resultat.html', stats=stats, graphiques=graphiques)

@app.route('/dashboard')
def dashboard():
    # 1. On récupère les données de la base
    df = db.recuperer_tous()
    
    # 2. On demande à analyse.py de faire TOUS les calculs (stats + graphiques)
    # C'est ici que la magie opère !
    stats = analyse.statistiques_desc(df)
    graphiques = analyse.generer_graphiques(df)
    
    # 3. On envoie ces résultats tout prêts au HTML
    return render_template('dashboard.html', stats=stats, graphiques=graphiques)
    
    
    # Si on a des données, on met les vrais calculs
    if not df.empty:
        stats_rapides['total'] = len(df)
        stats_rapides['age_moyen'] = round (df['age'].mean(), 1)
        stats_rapides['heures_moyennes'] = df['heures_semaine'].mean()
        stats_rapides['satisfaction_moyenne'] = df['satisfaction'].mean()
        stats_rapides['salaire_moyen'] = df['salaire'].mean()
    
    # On envoie bien stats_rapides au template
    return render_template('dashboard.html', stats=stats_rapides)

if __name__ == '__main__':
    db.init_db()
    app.run(debug=True)
