# Sales Analytics Dashboard 

Analyse de 1 000 données de ventes fictives avec visualisations et prévision ML.
My most complete project so far. I built an end-to-end data analytics pipeline in Python: first generating 1,000 synthetic sales records with Pandas and NumPy, then running exploratory analysis and producing 4 visualizations with Matplotlib and Seaborn (monthly revenue trends, sales by product, regional breakdown, and an ML prediction chart). Finally, I trained a Linear Regression model with Scikit-learn to forecast revenue, achieving an R² score of 0.80 — meaning the model explains 80% of revenue variance. This project reflects my interest in combining data analysis with machine learning


## Technologien / Technologies
- Python 3.10+
- Pandas, NumPy — Datenverarbeitung
- Matplotlib, Seaborn — Visualisierung
- Scikit-learn — Machine Learning (Linear Regression, R² = 0.80)

## Ausführen / Exécution

```bash
pip install -r requirements.txt
python generate_data.py   # Daten generieren
python dashboard.py       # Analyse starten
```

## Ausgaben / Sorties
| Datei | Inhalt |
|-------|--------|
| `outputs/01_ca_mensuel.png` | Umsatz pro Monat |
| `outputs/02_ca_produit.png` | Umsatz nach Produkt |
| `outputs/03_ca_region.png`  | Regionale Verteilung |
| `outputs/04_ml_prediction.png` | ML-Prognose vs. Real |

---
*Projekt von Orlane Nono Mabou — BSc Wirtschaftsinformatik, HRW*
