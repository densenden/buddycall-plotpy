import plotly.io as pio
import visuals.trump as trump
import visuals.musk as musk

# Übersicht
print("\n=====📊 NEWS DASHBOARD 📊=====")
print("1️⃣ Trump News Map  - Lädt...")
print("2️⃣ Musk Trends Plot - Lädt...")

# Trump
trump_fig = trump.show_trump_visual()
if trump_fig:
    print("✅ Trump News Map bereit! Öffne im Browser...")
    pio.show(trump_fig)
else:
    print("⚠️ Trump News Map konnte nicht geladen werden.")

# Musk
musk_fig = musk.show_musk_visual()
if musk_fig:
    print("✅ Musk Trends Plot bereit! Öffne im Browser...")
    pio.show(musk_fig)
else:
    print("⚠️ Musk Trends Plot konnte nicht geladen werden.")

print("\n📌 Hinweis: Falls keine Visualisierungen erscheinen, prüfe die CSV-Daten.")