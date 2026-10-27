# generate_data.py
# Génère 1000 lignes de données de ventes fictives / Generiert 1000 fiktive Verkaufsdaten

import pandas as pd
import numpy as np
import os

# Reproductibilité / Reproduzierbarkeit
np.random.seed(42)

# Paramètres / Parameter
N = 1000
produits = ["Laptop", "Smartphone", "Tablette", "Écouteurs", "Montre connectée"]
regions  = ["Nord", "Sud", "Est", "Ouest", "Centre"]

data = {
    "date":     pd.date_range(start="2024-01-01", periods=N, freq="8h"),
    "produit":  np.random.choice(produits, N),
    "region":   np.random.choice(regions, N),
    "quantite": np.random.randint(1, 20, N),
    "prix_unitaire": np.random.uniform(50, 1500, N).round(2),
}

df = pd.DataFrame(data)
df["chiffre_affaires"] = (df["quantite"] * df["prix_unitaire"]).round(2)
df["mois"] = df["date"].dt.to_period("M").astype(str)

# Sauvegarde / Speichern
os.makedirs("Data", exist_ok=True)
df.to_csv("Data/sales_data.csv", index=False)
print(f" {N} lignes générées → Data/sales_data.csv")
