#importing essential libraries and packages
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()

str1 = ""

# Function selected
def selected(event):
    for i in range(0, len(p_name)):
        if clicked.get() == p_name[i]:
            myLabel = Label(root, text = p_name[i]).pack()
            str1 = xlsname[i]


            # This code has been written for a specific player but we shall be using this same code for all our players
            # The idea is to get the user's selection from the drop down then read the excel file for that specific player
            # Thereby provide the analysis for that player appropriately  

    

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

            first_match_date = df['date'].dt.date.min().strftime('%B %d, %Y') # first match
            myLabel = Label(root, text = 'First match: ' + first_match_date).pack()
            last_match_date = df['date'].dt.date.max().strftime('%B %d, %Y') # last match
            myLabel = Label(root, text = 'Last match: ' + last_match_date).pack()
            number_of_matches = df.shape[0] # number of matches played in career
            myLabel = Label(root, text = 'Number of matches played: '+ str(number_of_matches)).pack()
            number_of_inns = df_new.shape[0] # number of innings
            myLabel = Label(root, text = 'Number of innings played: ' + str(number_of_inns)).pack()
            not_outs = df_new['not_out'].sum() # number of not outs in career
            myLabel = Label(root, text = 'Not outs: ' + str(not_outs)).pack()
            runs_scored = df_new['runs_scored'].sum() # runs scored in career
            myLabel = Label(root, text = 'Runs scored in career: ' + str(runs_scored)).pack()
            balls_faced = df_new['balls_faced'].sum() # balls faced in career
            myLabel = Label(root, text = 'Balls faced in career: ' + str(balls_faced)).pack()
            career_sr = (runs_scored / balls_faced)*100 # career strike rate
            myLabel = Label(root, text = 'Career strike rate: {:.2f}'.format(career_sr)).pack()
            career_avg = (runs_scored / (number_of_inns - not_outs)) # career average
            myLabel = Label(root, text = 'Career average: {:.2f}'.format(career_avg)).pack()
            highest_score_date = df_new.loc[df_new.runs_scored == df_new.runs_scored.max(), 'date'].values[0]
            highest_score = df.loc[df.date == highest_score_date, 'score'].values[0] # highest score
            myLabel = Label(root, text = 'Highest score in career: ' + str(highest_score)).pack()
            hundreds = df_new.loc[df_new['runs_scored'] >= 100].shape[0] # number of 100s
            myLabel = Label(root, text = 'Number of 100s: ' + str(hundreds)).pack()
            fifties = df_new.loc[(df_new['runs_scored']>=50)&(df_new['runs_scored']<100)].shape[0] #number of 50s
            myLabel = Label(root, text = 'Number of 50s: ' + str(fifties)).pack()
            fours = df_new['fours'].sum() # number of fours in career
            myLabel = Label(root, text = 'Number of 4s: ' + str(fours)).pack()
            sixes = df_new['sixes'].sum() # number of sixes in career
            myLabel = Label(root, text = 'Number of 6s: ' + str(sixes)).pack()


            # For graphical analysis
            # plt.plot for plotting
            # plt.xlabel and plt.ylabel for labelling the Axes
            # plt.label for labelling the graph
            # plt.show for displaying

            #Start of Analysis
            #1.  number of matches played against different oppositions
            df['opposition'].value_counts().plot(kind='bar', title='Number of matches against different oppositions', figsize=(8, 5));
            plt.show()

            #2. Runs scored against different oppositions
            runs_scored_by_opposition = pd.DataFrame(df_new.groupby('opposition')['runs_scored'].sum())
            runs_scored_by_opposition.plot(kind='bar', title='Runs scored against different oppositions', figsize=(8, 5))
            plt.xlabel(None);
            plt.show()

            #3. Batting average against each team
            innings_by_opposition = pd.DataFrame(df_new.groupby('opposition')['date'].count())
            not_outs_by_opposition = pd.DataFrame(df_new.groupby('opposition')['not_out'].sum())
            temp = runs_scored_by_opposition.merge(innings_by_opposition, left_index=True, right_index=True)
            average_by_opposition = temp.merge(not_outs_by_opposition, left_index=True, right_index=True)
            average_by_opposition.rename(columns = {'date': 'innings'}, inplace=True)
            average_by_opposition['eff_num_of_inns'] = average_by_opposition['innings'] - average_by_opposition['not_out']
            average_by_opposition['average'] = average_by_opposition['runs_scored'] / average_by_opposition['eff_num_of_inns']
            average_by_opposition.replace(np.inf, np.nan, inplace=True)
            major_nations = ['Australia', 'England', 'New Zealand', 'Pakistan', 'South Africa', 'Sri Lanka', 'West Indies']

            #Code for generating the plot
            plt.figure(figsize = (8, 5))
            plt.plot(average_by_opposition.loc[major_nations, 'average'].values, marker='o')
            plt.plot([career_avg]*len(major_nations), '--')
            plt.title('Average against major teams')
            plt.xticks(range(0, 7), major_nations)
            plt.ylim(20, 70)
            plt.legend(['Avg against opposition', 'Career average']);
            plt.show()

            #4. Matches played per year
            df['year'].value_counts().sort_index().plot(kind='bar', title='Matches played by year', figsize=(8, 5))
            plt.xticks(rotation=0);
            plt.show()

            #5. Runs scored every year 
            df_new.groupby('year')['runs_scored'].sum().plot(kind='line', marker='o', title='Runs scored by year', figsize=(8, 5))
            years = df['year'].unique().tolist()
            plt.xticks(years)
            plt.xlabel(None);
            plt.show()

            #6. Batting average progression
            df_new.reset_index(drop=True, inplace=True)
            career_average = pd.DataFrame()
            career_average['runs_scored_in_career'] = df_new['runs_scored'].cumsum()
            career_average['innings'] = df_new.index.tolist()
            career_average['innings'] = career_average['innings'].apply(lambda x: x+1)
            career_average['not_outs_in_career'] = df_new['not_out'].cumsum()
            career_average['eff_num_of_inns'] = career_average['innings'] - career_average['not_outs_in_career']
            career_average['average'] = career_average['runs_scored_in_career'] / career_average['eff_num_of_inns']

            #For plotting the curve
            plt.figure(figsize = (8, 5))
            plt.plot(career_average['average'])
            plt.plot([career_avg]*career_average.shape[0], '--')
            plt.title('Career average progression by innings')
            plt.xlabel('Number of innings')
            plt.legend(['Avg progression', 'Career average']);
            plt.show()
            



# Width X Height
root.geometry("800x600")


# Displaying the Image
img= (Image.open("cricket-stats.png"))
resized_image = img.resize((800,400), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

# photo = PhotoImage(file = "cricket-stats.png")
label1 = Label(image = new_image)
label1.pack()


#width, height
root.minsize(300, 100)


"""
myLabel = Label(text = "This is a Label")
myLabel.pack()
"""

p_name = [
    "MS Dhoni",
    "Rohit Shama",
    "VVS Laxman",
    "Shikhar Dhawan",
    "Rahul Dravid",
    "KL Rahul",
    "Sachin Tendulkar",
    "Virendar Sehwag",
    "Gautam Gambhir",
    "Sourav Ganguly",
    "Ajinkya Rahane"
]

xlsname = [
    "MS_Dhoni_ODI_record",
    "Rohit_Sharma_ODI_record",
    "VVS_Laxman_ODI_record",
    "Shikhar_Dhawan_ODI_record",
    "Rahul_Dravid_ODI_record",
    "KL_Rahul_ODI_record",
    "Sachin_Tendulkar_ODI_record",
    "Virendar_Sehwag_ODI_record",
    "Gautam_Gambhir_ODI_record",
    "Sourav_Ganguly_ODI_record",
    "Ajinkya_Rahane_ODI_record"    
]

# Storing value of clicked Name
clicked = StringVar()

# Default placeholder for Dropdown Box
clicked.set("Select a Player")

# Dropdown Box
drop = OptionMenu(root, clicked, *p_name, command = selected)
drop.pack()

root.mainloop() 
