import importlib
import matplotlib.pyplot as plt

# Module einbinden
try:
    trump = importlib.import_module("visuals.trump")
except ModuleNotFoundError:
    trump = None

try:
    musk = importlib.import_module("visuals.musk")
except ModuleNotFoundError:
    musk = None

# Diagramme anzeigen
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Trump-Diagramm
if trump and hasattr(trump, "show_trump_visual"):
    trump.show_trump_visual(axes[0])
    axes[0].set_title("Trump News")
else:
    axes[0].text(0.5, 0.5, "Trump-Daten fehlen", ha='center', va='center', fontsize=12)
    axes[0].set_xticks([])
    axes[0].set_yticks([])

# Musk-Diagramm
if musk and hasattr(musk, "show_musk_visual"):
    musk.show_musk_visual(axes[1])
    axes[1].set_title("Musk Trends")
else:
    axes[1].text(0.5, 0.5, "Musk-Daten fehlen", ha='center', va='center', fontsize=12)
    axes[1].set_xticks([])
    axes[1].set_yticks([])

# Layout anpassen und Diagramme anzeigen
plt.tight_layout()
plt.show()