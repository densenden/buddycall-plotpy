from data import get_csv_path
import pandas as pd
import plotly.express as px
import os

def show_trump_visual(name):
    """https://plotly.com/python/bubble-maps/ Prepared Function for mapping data"""

    file_path = get_csv_path(name + "_news.csv")

    try:
        df = pd.read_csv(file_path) # read csv via pandas -> create dataframe

        # Debugging: Zeige die Spaltennamen und erste Zeilen
        # print(df)

        # Sicherstellen, dass die relevanten Spalten existieren
        pass

        # Erstelle die Weltkarte mit den Erwähnungen
        pass # px.scatter_geo

        return fig

    except FileNotFoundError:
        print("⚠️ Trump CSV fehlt!")
        return None
    except KeyError as e:
        print(f"⚠️ Fehlende Spalten in Trump CSV: {e}")
        return None

show_trump_visual("trump")