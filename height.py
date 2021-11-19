import plotly.figure_factory as ff
import pandas as pd
import csv
df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/c108/data.csv")
fig = ff.create_distplot([df["Height"].tolist()],["height"],show_hist=False)
fig.show()