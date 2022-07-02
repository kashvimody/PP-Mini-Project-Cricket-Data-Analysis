#importing essential libraries and packages
import pandas as pd
import numpy as np
impo datetime
import matplotlib.pyplot as plt
import seaborn as sns

# This code has been written for a specific player but we shall be using this same code for all our players
# The idea is to get the user's selection from the drop down then read the excel file for that specific player
# Thereby provide the analysis for that player appropriately  

str1 = "Rohit_Sharma_ODI_record"

#reading the dataset
df = pd.read_excel(str1+".xlsx")

# removing the first 2 characters in the opposition string
df['opposition'] = df['opposition'].apply(lambda x: x[2:])

# creating a feature for match year
df['year'] = df['date'].dt.year.astype(int)

# creating a feature for being not out
df['score'] = df['score'].apply(str)
df['not_out'] = np.where(df['score'].str.endswith('*'), 1, 0)

# dropping the odi_number feature because it adds no value to the analysis
df.drop(columns='odi_number', inplace=True)

# dropping those innings where Dhoni did not bat and storing in a new DataFrame
df_new = df.loc[((df['score'] != 'DNB') & (df['score'] != 'TDNB')), 'runs_scored':]

# fixing the data types of numerical columns
df_new['runs_scored'] = df_new['runs_scored'].astype(int)
df_new['balls_faced'] = df_new['balls_faced'].astype(int)
df_new['strike_rate'] = df_new['strike_rate'].astype(float)
df_new['fours'] = df_new['fours'].astype(int)
df_new['sixes'] = df_new['sixes'].astype(int)

