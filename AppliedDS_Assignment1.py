# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def lineplot(width, height, country1, country2, country3, country4, country5):
    
    """
    To plot life expectancy lineplot of any 5 countries from 
    Population_Indicators.xlsx file.
    Width, height of line plot to be plotted has to be provided along with the 
    five country names as arguments for the function lineplot.
    
    """
    # import and read the excel file and print the data from the file.
    Life_exp = pd.read_excel("Population_Indicators.xlsx")
    print("Data of Life expectancy of Countries from 2000-2015", "\n")
    print(Life_exp, "\n")
    plt.figure(figsize=(width, height)) #To make the figure size fit in.
    
    
    #Plotting lineplot using matplotlib 
    plt.plot(Life_exp["Year"], Life_exp[country1], label= country1)
    plt.plot(Life_exp["Year"], Life_exp[country2], label= country2)
    plt.plot(Life_exp["Year"], Life_exp[country3], label= country3)
    plt.plot(Life_exp["Year"], Life_exp[country4], label= country4)
    plt.plot(Life_exp["Year"], Life_exp[country5], label= country5)

    # Labelling x and y axis
    plt.xlabel("YEARS")
    plt.ylabel("AGE")

    # Marking x and y axis limits as 2000-2015 & 30-100 respectively.
    plt.xlim([2000, 2015]) 
    plt.ylim([30, 100]) 
    plt.xticks([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
                2010,2011, 2012, 2013, 2014, 2015]) 
    plt.title("Life Expectancy of Countries from 2000-2015") 
    plt.legend(title = "Countries", loc = "upper right", edgecolor = "black")
    plt.savefig("lineplot.png")
    plt.show()
    return


def barplot(wid, figwidth, figheight):
    
    """
    Arguments in the above barplot function contains width of the bar, graph 
    height and width.
    Plots Grouped barchart of top 5 medals won countries in Tokyo Olympics 2021 
    """ 
    # imports and reads the excel file which contains the data of medals won
    # Lists top 5 countries from all countries participated and prints the data
    Medals = pd.read_excel("Medals.xlsx")
    Top = Medals.head() 
    print("Top five most Medals won by countries in Tokyo Olympics 2021", "\n") 
    print(Top, "\n")
    
    # calculating the length and arranging the team names in teams that needs 
    # to be displayed on x-axis 
    Teams = np.arange(len(Top['Team']))
    plt.figure(figsize = (figwidth, figheight))

    # Location on x-ais to plot the Bar chart
    silverbar = [i+wid for i in Teams]
    bronzebar = [i+wid for i in silverbar]
    totalbar = [i+wid for i in bronzebar]
    
    # Plots Grouped Barchart with respect to Gold, Silver & Bronze medals along
    # with the total medals won.        
    Gold = plt.bar(Teams, Top['Gold'], width = wid, label = "Gold", 
                    color = "Gold")
    plt.bar_label(Gold, labels = Top['Gold'], label_type = 'edge', padding = 3)
    
    Silver = plt.bar(silverbar, Top['Silver'], width = wid, label = "Silver", 
                    color = "Silver")
    plt.bar_label(Silver, labels = Top['Silver'], label_type = 'edge',
                  padding = 3)
    
    Bronze = plt.bar(bronzebar, Top['Bronze'], width = wid, label = "Bronze", 
                    color = "Brown")
    plt.bar_label(Bronze, labels = Top['Bronze'], label_type = 'edge',
                  padding = 3)
    Totals = plt.bar(totalbar, Top['Total'], width = wid, label ="TotalMedals")
    plt.bar_label(Totals, labels = Top['Total'], label_type = 'edge',
                  padding = 3)
    
    # Labelling x and y axis
    plt.xlabel("Top Five Countries")
    plt.ylabel("Medals won")
    plt.xticks(Teams+wid*1.5, ["USA", "China", "Japan", "Great Britain", 
                               "Russia"])
    plt.ylim(0, 120)
    plt.grid(axis ='y', lw = 0.3, ls = "dashdot")
    plt.title("Most Medals won by countries in Tokyo Olympics(2021)")
    plt.legend(title = "Medals", loc = "upper right", edgecolor = "black")
    plt.savefig("Groupedbarchart.png")
    plt.show()
    return


def piechart(figwidth, figheight, startangle):
    """
    To plot pie chart showing the inflation percentage hit on India from 2012 -
    2021. 
    """
    #To import Medals excel file
    data = pd.read_excel("C:/Users/Lenovo/.spyder-py3/Ind_inflation.xlsx") 
    India_data = pd.DataFrame(data)
    print("Data of India's Inflation % & other entities from 2012-2021", "\n")
    print(India_data, "\n")
    Explode_2021 = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    plt.figure(figsize = (figwidth, figheight))
    
    #Plotting pie chart and providing the title using matplotlib 
    plt.pie(India_data["InflationPercentage"], labels = India_data["Years"], 
            startangle = 90, autopct = "%2.1f%%", explode = Explode_2021)
    plt.title("India's Inflation rate, GDP deflator(Annual %) from 2012-2021")
    plt.legend(title = "Years", loc = "upper right", edgecolor = "black")
    plt.savefig("Piechart.png")
    plt.show()
    return


lineplot(10, 8, "United Kingdom", "India", "Syrian Arab Republic", "Haiti", 
         "Zimbabwe" )
barplot(0.2, 10, 6)
piechart(10, 12, 90)
