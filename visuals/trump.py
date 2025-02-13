import plotly.express as px
import pandas as pd

def show_trump_visual(screen):
    df = pd.read_csv("trump_news.csv")
    fig = px.scatter_geo(df, locations="country", size="num_articles", projection="natural earth",
                         title="Trump News Coverage weltweit")
    fig.show()
