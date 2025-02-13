import plotly.express as px
import pandas as pd

# 1️⃣ Beispiel-Daten für ein einfaches Balkendiagramm erstellen
data = {
    "Thema": ["Tesla", "SpaceX", "X (Twitter)", "AI", "Neuralink"],
    "Häufigkeit": [80, 50, 120, 90, 30]  # Anzahl der Erwähnungen
}

df = pd.DataFrame(data) #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

# 2️⃣ Bar Chart mit Plotly erstellen
fig = px.bar(df, x="Thema", y="Häufigkeit", color="Thema",
             title="📊 Beispiel-Balkendiagramm für Musk-Themen-Trends",
             labels={"Häufigkeit": "Anzahl der Erwähnungen", "Thema": "Technologie-Themen"})

# 3️⃣ Diagramm anzeigen
fig.show()

# 🔥 Aufgabe:
# - Ändere die Häufigkeitswerte oder füge neue Themen hinzu.
# - Erstelle ein gestapeltes Balkendiagramm mit mehreren Kategorien.