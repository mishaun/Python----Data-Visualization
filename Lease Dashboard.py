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

acres_byState = current.groupby("ST").sum()

sns.barplot(x="ST", y="ACRES", data = acres_byState.reset_index())