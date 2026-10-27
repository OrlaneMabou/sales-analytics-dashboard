# Sales Analytics Dashboard 📊

Analyse de 1 000 données de ventes fictives avec visualisations et prévision ML.

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
