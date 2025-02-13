import plotly.express as px
import pandas as pd

def show_musk_visual(screen):
    df = pd.read_csv("musk_news.csv")
    fig = px.line(df, x="date", y=["Tesla", "SpaceX", "X (Twitter)", "AI", "Neuralink"],
                  title="Musk Themen-Trends über Zeit")
    fig.show()
