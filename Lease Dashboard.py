# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:05:06 2020

@author: mishaun
"""

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_excel("BLM Leases.xlsx", header = 9)

#dropping rows that have no lease number
df.dropna(subset = ["LEASE NO."], inplace = True)

#getting today's date and converting to pandas timestamp data type
today = pd.Timestamp(dt.date.today())

current = df[df["EXPIRATION DATE"]>today]
total_acres = current.ACRES.sum()

acres_byState = current.groupby("ST").sum().reset_index()

sns.barplot(x="ST", y="ACRES", data = acres_byState)

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


#import for plotly to view data offline
import plotly.express as px
from plotly.offline import plot

#creating usa heatmap colred by sum of acres per state
fig = px.choropleth(
        acres_byState,
        locations=acres_byState["ST"], 
        color="ACRES",
        locationmode="USA-states", 
        scope="usa"
        )



plot(fig)








