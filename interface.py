import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Monthly data for every year
cases_2015_month = pd.read_csv("data/cases_2015_month.csv", sep=";")
cases_2016_month = pd.read_csv("data/cases_2016_month.csv", sep=";")
cases_2017_month = pd.read_csv("data/cases_2017_month.csv", sep=";")
cases_2018_month = pd.read_csv("data/cases_2018_month.csv", sep=";")
cases_2019_month = pd.read_csv("data/cases_2019_month.csv", sep=";")
cases_2020_month = pd.read_csv("data/cases_2020_month.csv", sep=";")
cases_months_per_year = pd.concat([cases_2015_month, cases_2016_month, cases_2017_month, cases_2018_month, cases_2019_month, cases_2020_month])
cases_months_per_year.reset_index()

# Yearly data
cases_2015_year = pd.read_csv("data/cases_2015_year.csv", sep=";")
cases_2016_year = pd.read_csv("data/cases_2016_year.csv", sep=";")
cases_2017_year = pd.read_csv("data/cases_2017_year.csv", sep=";")
cases_2018_year = pd.read_csv("data/cases_2018_year.csv", sep=";")
cases_2019_year = pd.read_csv("data/cases_2019_year.csv", sep=";")
cases_2020_year = pd.read_csv("data/cases_2020_year.csv", sep=";")
cases_years = pd.concat([cases_2015_year, cases_2016_year, cases_2017_year, cases_2018_year, cases_2019_year, cases_2020_year])
cases_years.reset_index()

def create_years_plot(key_list, title):
    sns.set(style="whitegrid")
    sns.despine()
    
    input_data = cases_years[cases_years["Schlüssel"].isin(key_list)]
    input_data = input_data.groupby("Jahr").sum().reset_index()
    input_data = input_data.rename(columns={"Jahr":"Year","erfasste Fälle":"Reported cases"})

    plot = sns.catplot(x="Year", 
                       y="Reported cases", 
                       data=input_data, 
                       kind="point",
                       height=6.5,
                       aspect=1.7,
                       color="#0b559f")
    plot.fig.suptitle(title, y=1.06)

    return plot

def create_months_plot(key_list, title, marked = True, marked2 = False, start_at_zero = True, marked3 = True, mrange=[2,4.5,9.5,11], m_label="Lockdown", m2_label=None, m2_range=[4.5,9.5]):
    sns.set(style="whitegrid")
    sns.despine()
    
    custom_palette = ["#addaf7","#80c8f7","#4ca2da","#287cb3","#145a89","#ff0000"]
    input_data = cases_months_per_year[cases_months_per_year["Schlüssel"].isin(key_list)]
    input_data = input_data.groupby("Jahr").sum().reset_index()
    input_data = input_data.melt(id_vars=["Jahr"])
    input_data = input_data.rename(columns={"Jahr":"Year","variable":"Month","value":"Reported cases"})
    translate_months(input_data)
    
    avg_per_year = input_data.groupby("Year").mean().reset_index()
    avg_per_year = avg_per_year.rename(columns={"Reported cases" : "Average cases"})

    input_data = pd.merge(input_data, avg_per_year, how="left")

    input_data["Average case difference (-)"] = input_data["Reported cases"]-input_data["Average cases"]
    input_data["Average case difference (/)"] = input_data["Reported cases"]/input_data["Average cases"]

    
    plot = sns.catplot(x="Month",
                    y="Reported cases",
                    hue="Year",                  
                    data=input_data,
                    kind="point",
                    height=6.5,
                    aspect=1.7,
                    palette=custom_palette,
                    legend=False)
    plot.fig.suptitle(title, y=1.06)
    
    max_val = input_data["Reported cases"].max()
    
    # Determine, if the y-axis starts at value 0 or the lowest value in the dataset
    start_val = 0
    if start_at_zero is False:
        start_val = input_data["Reported cases"].min()
    
    #mark lockdown features
    if marked is True:
        plt.axvspan(mrange[0], mrange[1], ymin=start_val, ymax=max_val, alpha=0.2, color='red', label=m_label)
        
    if marked3 is True:
        plt.axvspan(mrange[2], mrange[3], ymin=start_val, ymax=max_val, alpha=0.2, color='red')
    
    if marked2 is True:
        plt.axvspan(m2_range[0], m2_range[1], ymin=start_val, ymax=max_val, alpha=0.1, color='red', label=m2_label)

    plt.legend(loc=7, bbox_to_anchor=(1.12, 0.5))

    return plot

def save_plot(plot, name, marked=False):
    if marked is True:
        if not os.path.exists("plots_marked"):
            os.makedirs("plots_marked")
        plot.savefig("plots_marked/%s" % name, bbox_inches="tight")
        return
    if not os.path.exists("plots_unmarked"):
        os.makedirs("plots_unmarked")
    plot.savefig("plots_unmarked/%s" % name, bbox_inches="tight")
    plt.clf
    
    return


def translate_months(input_data):
    input_data.loc[input_data["Month"] == "Januar", "Month"] = "January"
    input_data.loc[input_data["Month"] == "Februar", "Month"] = "February"
    input_data.loc[input_data["Month"] == "März", "Month"] = "March"
    input_data.loc[input_data["Month"] == "Mai", "Month"] = "May"
    input_data.loc[input_data["Month"] == "Juni", "Month"] = "June"
    input_data.loc[input_data["Month"] == "Juli", "Month"] = "July"
    input_data.loc[input_data["Month"] == "Oktober", "Month"] = "October"
    input_data.loc[input_data["Month"] == "Dezember", "Month"] = "December"

