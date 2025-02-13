# Übung: Bubble Maps mit Plotly (Trump Team)

import plotly.express as px
import pandas as pd

# 1️⃣ Beispiel-Daten für eine einfache Bubble Map erstellen
data = {
    "country": ["USA", "Germany", "UK", "France", "India", "China"],
    "num_articles": [120, 50, 80, 40, 100, 30]
}

df = pd.DataFrame(data)

# 2️⃣ Plotly Bubble Map erstellen
fig = px.scatter_geo(df, locations="country", size="num_articles", projection="natural earth",
                     title="Beispiel-Bubble-Map für Trump News")

# 3️⃣ Diagramm anzeigen
fig.show()

# 🔥 Aufgabe: Passe die Daten an und probiere verschiedene Projektionen!
