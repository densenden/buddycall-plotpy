# Übung: Bubble Charts mit Plotly (Musk Team)

import plotly.express as px
import pandas as pd

# 1️⃣ Beispiel-Daten für ein einfaches Bubble Chart erstellen
data = {
    "Thema": ["Tesla", "SpaceX", "X (Twitter)", "AI", "Neuralink"],
    "Häufigkeit": [80, 50, 120, 90, 30],
    "Impact": [3, 5, 8, 6, 4]  # Größe der Blasen
}

df = pd.DataFrame(data)

# 2️⃣ Plotly Bubble Chart erstellen
fig = px.scatter(df, x="Thema", y="Häufigkeit", size="Impact", color="Thema",
                 title="Beispiel-Bubble-Chart für Musk Themen-Trends")

# 3️⃣ Diagramm anzeigen
fig.show()

# 🔥 Aufgabe: Ändere die Größenwerte oder füge neue Themen hinzu!
