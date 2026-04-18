PROJET : ANALYSE DES DYNAMIQUES DU TRAVAIL

Étudiante  :TCHATCHOUANG TANKIO GRACE FARELLE
Matricule  : 24F2749
Cours      : INF232 - Programmation Python / Analyse de Données
Date       : Avril 2026
Institution: Université de Yaoundé I



                1 )  PRESENTATION DU PROJET

Ce projet est une application web d'analyse de données RH développée avec *Flask*. Elle permet d'explorer les corrélations entre l'âge des employés, leur salaire, leur temps de travail et leur niveau de satisfaction.

L'objectif principal est de fournir une interface interactive pour comparer scientifiquement deux populations : les Jeunes (18-35 ans) et les Seniors (50+ ans).

                 2 )  FONCTIONALITES CLES

- *Collecte de données : Formulaire dynamique pour enregistrer les profils (âge, salaire, expérience, télétravail).
- *Indicateurs RH (KPIs) : Calcul automatique de l'âge moyen, du salaire moyen et du score d'activité.
- *Analyses Statistiques:
    - Calcul de la *Corrélation de Pearson* (relation âge/salaire).
    - Test de Student (*p-value*) pour comparer les heures de travail entre générations.
- *Visualisations graphiques :
    - Histogramme de distribution des âges.
    - Boxplot des heures travaillées.
    - Matrice de corrélation (Heatmap) : Vue d'ensemble des liens entre toutes les variables.

               3 )  TETCHNOLOGIE UTILISEES

- *Backend : Flask (Python 3.10)
- *Base de données : SQLite
- *Analyse de données : Pandas, SciPy
- *Visualisation : Matplotlib, Seaborn
- *Frontend : HTML5, CSS3 (Bootstrap 5)

                    4  ) INSTALLATION ET LANCEMENT

 *Cloner le projet :
       bash
   git clone [https://github.com/gracefarelle/analyse-travail-age.git](https://github.com/gracefarelle/analyse-travail-age.git)
   cd analyse-travail-age


               5 )  INSTALLER LES DEPENDANCES

pip install flask pandas matplotlib seaborn scipy  


              6  )  LANCER L'APPLICATION

python3 app.py


L'application sera accessible sur http://127.0.0.1:5000.
​
       
       7 )   STRUCTURE DU DOSSIER

*​app.py : Serveur Flask et gestion des routes.
​*analyse.py : Calculs statistiques et génération des graphiques.
*​database.py : Gestion de la base de données.
​*templates/ : Pages HTML (index, formulaire, résultats).
​*static/images/ : Stockage des graphiques générés.


       ​8  )  CONCLUSION DE L'ÉTUDE

​Grâce à cet outil, nous avons pu tirer les conclusions suivantes :
​Lien Âge/Expérience : La matrice de corrélation confirme une relation forte, montrant une progression logique de la carrière.
​Validation Statistique : L'utilisation de la p-value permet de confirmer si les différences de satisfaction entre les groupes d'âge sont significatives ou dues au hasard.
​Perspectives : Ce projet pose les bases d'un système de gestion RH intelligent capable de prédire les besoins des employés selon leur tranche d'âge.
