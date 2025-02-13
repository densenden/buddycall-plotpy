import plotly.express as px

fig = px.bar(x=["1999","2003", "2010", "2019"], y=[52, 55, 51, 42], title="Test-Plotly Heidis Gewicht")
fig.show()