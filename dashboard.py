# dashboard.py
# Tableau de bord analytique des ventes / Analyse-Dashboard für Verkaufsdaten

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# --- Chemin automatique / Automatischer Pfad ---
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ── 1. Chargement des données / Daten laden ───────────────────────────────
df = pd.read_csv("Data/sales_data.csv", parse_dates=["date"])
print(f" {len(df)} lignes chargées")

# ── 2. KPIs globaux / Globale KPIs ───────────────────────────────────────
total_ca    = df["chiffre_affaires"].sum()
ca_moyen    = df["chiffre_affaires"].mean()
total_units = df["quantite"].sum()
print(f"\n KPIs globaux:")
print(f"   Chiffre d'affaires total : {total_ca:,.2f} €")
print(f"   CA moyen par transaction : {ca_moyen:,.2f} €")
print(f"   Unités vendues           : {total_units:,}")

os.makedirs("outputs", exist_ok=True)
sns.set_theme(style="whitegrid")

# ── 3. Graphique 1 : CA mensuel / Monatlicher Umsatz ────────────────────
ca_mensuel = df.groupby("mois")["chiffre_affaires"].sum().reset_index()
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=ca_mensuel, x="mois", y="chiffre_affaires", marker="o", color="#2E5FA3", ax=ax)
ax.set_title("Chiffre d'affaires mensuel", fontsize=14, fontweight="bold")
ax.set_xlabel("Mois")
ax.set_ylabel("CA (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/01_ca_mensuel.png", dpi=150)
plt.close()
print(" Graphique 1 sauvegardé")

# ── 4. Graphique 2 : CA par produit / Umsatz nach Produkt ───────────────
ca_produit = df.groupby("produit")["chiffre_affaires"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=ca_produit.values, y=ca_produit.index, palette="Blues_d", ax=ax)
ax.set_title("CA par produit", fontsize=14, fontweight="bold")
ax.set_xlabel("CA (€)")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("outputs/02_ca_produit.png", dpi=150)
plt.close()
print(" Graphique 2 sauvegardé")

# ── 5. Graphique 3 : CA par région / Umsatz nach Region ─────────────────
ca_region = df.groupby("region")["chiffre_affaires"].sum()
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(ca_region, labels=ca_region.index, autopct="%1.1f%%",
       colors=sns.color_palette("Blues", len(ca_region)))
ax.set_title("Répartition du CA par région", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/03_ca_region.png", dpi=150)
plt.close()
print(" Graphique 3 sauvegardé")

# ── 6. Régression linéaire / Lineare Regression ──────────────────────────
df_ml = df.groupby("mois").agg(
    ca=("chiffre_affaires", "sum"),
    quantite=("quantite", "sum")
).reset_index()
df_ml["mois_num"] = range(len(df_ml))

X = df_ml[["mois_num", "quantite"]]
y = df_ml["ca"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"\n Modèle ML — R² = {r2:.2f}")

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(y_test.values, y_pred, color="#2E5FA3", alpha=0.7)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
ax.set_title(f"Prévision vs Réel (R² = {r2:.2f})", fontsize=14, fontweight="bold")
ax.set_xlabel("CA réel (€)")
ax.set_ylabel("CA prédit (€)")
plt.tight_layout()
plt.savefig("outputs/04_ml_prediction.png", dpi=150)
plt.close()
print(" Graphique 4 sauvegardé")
print("\n Dashboard complet ! Résultats dans le dossier outputs/")
