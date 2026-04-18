import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import ttest_ind

def generer_graphiques(df):
    if df.empty:
        return None
    os.makedirs("static/images", exist_ok=True)
    
    # 1. Distribution des âges
    plt.figure()
    df['age'].hist(bins=10, edgecolor='black')
    plt.title("Distribution des âges")
    plt.xlabel("Âge")
    plt.ylabel("Effectif")
    plt.savefig("static/images/age_dist.png")
    plt.close()
    
    # 2. Salaire moyen par âge
    salaire_par_age = df.groupby('age')['salaire'].mean().reset_index()
    plt.figure()
    sns.lineplot(data=salaire_par_age, x='age', y='salaire', marker='o')
    plt.title("Salaire moyen selon l'âge")
    plt.savefig("static/images/salaire_age.png")
    plt.close()
    
    # 3. Satisfaction par tranche d'âge
    df['tranche_age'] = pd.cut(df['age'], bins=[18,30,45,100], labels=['18-30','31-45','46+'])
    satisfaction_par_tranche = df.groupby('tranche_age')['satisfaction'].mean()
    plt.figure()
    satisfaction_par_tranche.plot(kind='bar')
    plt.title("Satisfaction moyenne par tranche d'âge")
    plt.savefig("static/images/satisfaction_tranche.png")
    plt.close()
    
    # ----- Nouveaux graphiques pour comparer jeunes vs seniors -----
    df['groupe_age'] = pd.cut(df['age'], bins=[18,35,50,100], labels=['Jeunes (18-35)', 'Moyens (36-49)', 'Seniors (50+)'])
    
    # 4. Heures travaillées par groupe d'âge (boxplot)
    plt.figure(figsize=(8,5))
    sns.boxplot(x='groupe_age', y='heures_semaine', data=df)
    plt.title("Heures travaillées par semaine selon l'âge")
    plt.savefig("static/images/heures_par_age.png")
    plt.close()
    
    # 5. Score d'activité par groupe d'âge
    # Score = (heures_semaine/40)*0.5 + (heures_sup/10)*0.3 - (conges_annuels/30)*0.2 + (trajet_minutes/60)*0.1
    df['score_activite'] = (df['heures_semaine'] / 40) * 0.5 + (df['heures_sup'] / 10) * 0.3 - (df['conges_annuels'] / 30) * 0.2 + (df['trajet_minutes'] / 60) * 0.1
    plt.figure()
    sns.barplot(x='groupe_age', y='score_activite', data=df, ci=95)
    plt.title("Score d'activité (plus élevé = plus actif)")
    plt.savefig("static/images/score_activite.png")
    plt.close()
    
    # 6. Histogramme superposé jeunes vs seniors (heures semaine)
    jeunes = df[df['age'] <= 35]['heures_semaine']
    seniors = df[df['age'] >= 50]['heures_semaine']
    plt.figure()
    plt.hist(jeunes, alpha=0.5, label='Jeunes (18-35)', bins=10)
    plt.hist(seniors, alpha=0.5, label='Seniors (50+)', bins=10)
    plt.legend()
    plt.title("Distribution des heures travaillées : jeunes vs seniors")
    plt.xlabel("Heures/semaine")
    plt.ylabel("Effectif")
    plt.savefig("static/images/hist_jeunes_seniors.png")
    plt.close()

    # ----- AJOUT : Heatmap de corrélation -----
    plt.figure(figsize=(10, 8))
    # On ne garde que les colonnes avec des chiffres
    colonnes_num = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(colonnes_num.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matrice de corrélation des variables")
    
    # On l'enregistre comme les autres
    plt.savefig("static/images/heatmap_corr.png")
    plt.close()
    
    return ["age_dist.png", "salaire_age.png", "satisfaction_tranche.png",
            "heures_par_age.png", "score_activite.png", "hist_jeunes_seniors.png" , "heatmap_corr.png"]

def statistiques_desc(df):
    df['score_activite'] = (df['satisfaction'] * 2) + (df['heures_semaine'] / 10)
    if df.empty:
        return {}
    
    # Jeunes et seniors pour test t
    jeunes = df[df['age'] <= 35]['heures_semaine']
    seniors = df[df['age'] >= 50]['heures_semaine']
    p_value = None
    if len(jeunes) > 1 and len(seniors) > 1:
        _, p_value = ttest_ind(jeunes, seniors)
    
    # Calcule la corrélation entre âge et salaire
    correlation = df['age'].corr(df['salaire'])

   # ... garde tes calculs de correlation juste au-dessus ...
    correlation = df['age'].corr(df['salaire'])

    return {
        "effectif_total": len(df),
        "age_moyen": df['age'].mean(),
        "experience_moyenne": df['experience'].mean(),
        "salaire_moyen": df['salaire'].mean(),
        "satisfaction_moyenne": df['satisfaction'].mean(),
        "heures_moyennes": df['heures_semaine'].mean(),
        "score_activite_moyen": df['score_activite'].mean(),
        "heures_jeunes": jeunes.mean() if not jeunes.empty else None,
        "heures_seniors": seniors.mean() if not seniors.empty else None,
        "p_value": p_value,
        "repartition_age": df['age'].value_counts().to_dict(),
        "correlation": round(correlation, 2) if not pd.isna(correlation) else 0
    }
    