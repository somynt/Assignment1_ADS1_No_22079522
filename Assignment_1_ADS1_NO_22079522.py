# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:46:21 2023

@author: LENOVO
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:20:46 2023

@author: LENOVO
"""
"""
Necessary packages are imported below. wbgapi from 
worldbank data set is used for downloading data in world bank format.
"""
import wbgapi as wb
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def ReadWorldBankData (seriescode, *args): #Function definition
    
    '''
    Takes country as first parameter and multiple parameters for climate change indicators. 
    Provide the id code from World bank data as second set of arguments
    '''
    Read_series_country = wb.data.DataFrame (*args,seriescode ) # Getting data from Worldbank data set
    Read_series_country_Transpose = Read_series_country.transpose()#Transpose of the downloaded data set
    dfRead_series_country_Transpose = pd.DataFrame(Read_series_country_Transpose)#Converts to a dataframe
    return Read_series_country, dfRead_series_country_Transpose #returns two values one is original data set and the other is transposed data set
     
"""
Calling the required data from world bank climate change data set with country = GBR and 7 other indicators 
calling using its code in the data set
"""
WBDataPop, WBDataPop_Transpose = ReadWorldBankData('GBR', ['ER.H2O.FWTL.K3','SP.POP.GROW', 'EN.ATM.CO2E.KT', 'EN.ATM.NOXE.KT.CE', 'EN.ATM.NOXE.AG.ZS','AG.YLD.CREL.KG','EG.USE.ELEC.KH.PC'])
WBDataPop_Transpose_clean = WBDataPop_Transpose.dropna(how='all')#removes null values
WBDataPop_Transpose_clean_1980 = WBDataPop_Transpose_clean.loc["YR1980":"YR2020",:]#set dataset values to year =1980 To year =2020

#Renaming columns
columnsrename =['Annual Fresh Water  Withdrawals','Population Growth', 'CO2 Emissions (kt)', 'NO2 Emissions(1000 Metric tons of CO2 Equivalent)','Agricultural NO2 Emissions(Total)','Cereal Yield (Kg/Hectare)','Electric Power Consumption(Kwh per capita)' ]
WBDataPop_Transpose_clean_1980.columns = columnsrename

"""
Plotting the heat map of the given data set to understand the relation among the indicators                          
"""
plt.figure (figsize=(15,8))#Setting figure size
sns.heatmap(WBDataPop_Transpose_clean_1980, annot=True, cmap='coolwarm',fmt='.2f',linewidth=.5)#Heat map function is called
plt.title('Heat Map') #Plotting heat map
plt.show() #Show the plot                        

"""
This section provides the pairwise plot of the given indicators. 
It can provides clues on clusters, relationships or no relationships, trends outliers
"""

sns.set_style('whitegrid') #Whitegrid as the style for the plot       
sns.set(style ='ticks', color_codes= True)#providing colour to the plotted points
sns.set_context(context='paper',rc={'axes.labelsize': 20.0})#Context function provides option for setting label size, title size etc

"""
Plotting the pairwise function with 'pairplot'
"""
Pairplot= sns.pairplot(WBDataPop_Transpose_clean_1980, hue ='Annual Fresh Water  Withdrawals', height=3,diag_kind ='hist', grid_kws={"despine": False})
plt.suptitle("Pairplot of Climate indictors Vs UK", y=1.02,fontsize = 20,fontweight = 'bold', color = 'blue')
plt.tight_layout()#To fit the subplots automatically in to the plot
plt.savefig('Pairplot.png', dpi=300)#Saves the plot with dots per inch (dpi)=300
plt.show()
     
"""
Here the index is reset to make use of the year column.
New column names are provided which includes year as new column
""" 
WBDataPop_Transpose_clean_1980 = WBDataPop_Transpose_clean_1980.reset_index()#index reset
columnsrename1 =['Year','Annual Fresh Water  Withdrawals','Population Growth', 'CO2 Emissions (kt)', 'NO2 Emissions(1000 Metric tons of CO2 Equivalent)','Agricultural NO2 Emissions(Total)','Cereal Yield (Kg/Hectare)','Electric Power Consumption(Kwh per capita)' ]
WBDataPop_Transpose_clean_1980.columns = columnsrename1#rename the columns of data set
WBDataPop_Transpose_clean_1980['Year'] = WBDataPop_Transpose_clean_1980['Year'].str.extract(r'YR(\d{4})')#Strips the date value which will return 1980 insread of YR1980
                                                                  
"""
Plotting dataframe using relplot which is used to provide scatter plot view of the selected indicators
Here we chose Annual fresh water withdrawals, population growth and cereal production
This is chosen since we observed two clusters from pair plot
"""
sns.set_style('darkgrid')#grid colour
sns.set_palette('Set2')#colour palette for the scatter point
sns.set_context(context='paper',rc={'axes.labelsize': 20.0})#Context function provides option for setting label size, title size etc
sns.relplot(data=WBDataPop_Transpose_clean_1980, x='Annual Fresh Water  Withdrawals', y='Cereal Yield (Kg/Hectare)',hue='Population Growth', size = 'Agricultural NO2 Emissions(Total)', sizes=(10,300))                                                          
plt.title('Annual fresh water withdrawal and cereal production aganist Population growth', fontsize=8,fontweight = 'bold', color = 'green', loc='center')   
plt.tight_layout()
plt.savefig('Scatter plot cereal versus Population and water withdrawal.png', dpi=300)#Saves the plot with dots per inch (dpi)=300
plt.show()                            

                
"""
Here all the indicators are plotted as line graphs to provide a simple view of the behaviour of each indicator
It is distinguished with different colours. The main indicator is highlighted in blue with thick line plot
"""
fig,ax=plt.subplots()
"""
In the following section all the left, right, bottom and top labels are removed. 
This is because of the congestion in the label area. New labels are added.
"""
plt.tick_params (left = False, right = False ,bottom = False, top =False, labelleft = False , labelright = False, labelbottom = True)
ax2 = ax.twinx()
plt.tick_params (left = False, right = False ,bottom = False, top =False, labelleft = False , labelright = False, labelbottom = False)

ax3=ax.twinx()
plt.tick_params (left = False, right = False ,bottom = False, top =False, labelleft = False , labelright = False, labelbottom = False )

ax4=ax.twinx()
plt.tick_params (left = False, right = False ,bottom = False, top =False, labelleft = False , labelright = False, labelbottom = False )

ax5=ax.twinx()
plt.tick_params (left = False, right = False ,bottom = False, top =False, labelleft = False , labelright = False, labelbottom = False )

ax6=ax.twinx()
plt.tick_params (left = False, right = False ,bottom = False, top =False, labelleft = False , labelright = False, labelbottom = False)

ax7=ax.twinx()
plt.tick_params (left = False, right = False ,bottom = False, top =False, labelleft = False , labelright = False, labelbottom = False)

"""
In the following section each indicator is plotted aganist the year
"""

L1 = ax.plot(WBDataPop_Transpose_clean_1980 ['Year'],WBDataPop_Transpose_clean_1980 ['Annual Fresh Water  Withdrawals'], color='blue', marker = 'x', label = 'Annual Fresh Water  Withdrawals', linewidth = 5)
L2 = ax2.plot (WBDataPop_Transpose_clean_1980 ['Year'],WBDataPop_Transpose_clean_1980 ['Population Growth'], color='red', marker = 'x', label = 'Population Growth', linewidth = 2.5 )
L3 = ax3.plot(WBDataPop_Transpose_clean_1980 ['Year'],WBDataPop_Transpose_clean_1980 ['CO2 Emissions (kt)'], color= 'orange', marker = 'x', label ='CO2 Emissions (kt)', linewidth = 2.5 )
L4 = ax4.plot(WBDataPop_Transpose_clean_1980 ['Year'],WBDataPop_Transpose_clean_1980 ['NO2 Emissions(1000 Metric tons of CO2 Equivalent)'], color='green', marker = 'x', label = 'NO2 Emissions', linewidth = 2.5)
L5 = ax5.plot (WBDataPop_Transpose_clean_1980 ['Year'],WBDataPop_Transpose_clean_1980 ['Cereal Yield (Kg/Hectare)'], color='maroon', marker = 'x', label = 'Cereal Yield (Kg/Hectare)', linewidth = 2.5 )
L6=  ax6.plot (WBDataPop_Transpose_clean_1980 ['Year'],WBDataPop_Transpose_clean_1980 ['Electric Power Consumption(Kwh per capita)'], color='purple', marker = 'x' , label = 'Electric Power Consumption(Kwh per capita)', linewidth = 4)
L7=  ax7.plot (WBDataPop_Transpose_clean_1980 ['Year'],WBDataPop_Transpose_clean_1980 ['Agricultural NO2 Emissions(Total)'], color='magenta', marker = 'x' , label = 'Agricultural NO2 Emissions(Total)', linewidth = 2.5)


"""
Since the legends will not come independently, all of it are captured and added together
to plot as a single legend
"""
L = L1+L2+L3+L4+L5+L6+L7
Alllabel = [l.get_label()for l in L]
ax.legend (L,Alllabel, fontsize =20,loc='upper right', bbox_to_anchor=(0.35, 1.02),
           fancybox=True, shadow=True)

ax.grid()
ax.set_ylabel('Climate change parameters', fontsize = 45,fontweight = 'bold')#New Ylabel
ax.set_xlabel ('Years', fontsize = 45,fontweight = 'bold')#New X label

ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40])#Adding x ticks will get the year values totslling 40			
ax.tick_params(axis='x', rotation=45, labelsize = 25)#Year lable is rotaded 45 degrees

"""
Title, figure size, and save function is added here with tight layout.
"""
plt.title("Plot of Climate change indicators Vs United Kingdom", fontsize = 30,fontweight = 'bold', color = 'Purple', loc ='center' )
fig.set_size_inches(30, 15)
plt.tight_layout()
plt.savefig('linechart.png', dpi=300)
plt.show()

"""
End of the program

"""