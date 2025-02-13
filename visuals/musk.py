from data import get_csv_path
import pandas as pd
import plotly.express as px
import os

def show_musk_visual(name):
    """https://plotly.com/python/bar-charts/ prepared function for map vis"""

    file_path = get_csv_path(name + "_news.csv")

    try:
        # CSV-Datei laden
        df = pd.read_csv(file_path) # read csv via pandas -> create dataframe

        # Debugging: Zeigt die Spaltennamen und erste Zeilen
        # print(df)

        # Sicherstellen, dass die Spalten existieren
        pass

        # Umwandlung für Plotly durch pandas https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.melt.html
        pass

        # Erstelle das Bar Chart (gestapelt)
        pass # px.bar

        return fig

    except FileNotFoundError:
        print("⚠️ Musk CSV fehlt!")
        return None
    except KeyError as e:
        print(f"⚠️ Fehlende Spalten in Musk CSV: {e}")
        return None


show_musk_visual("musk")