"""
#1. Importing Required libraries
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, plot

"""#2. Loading Data Set"""

# Read data from CSV files
df_manufacturer = pd.read_csv('/content/drive/MyDrive/Naan Mudalvan/country_vaccinations_by_manufacturer.csv')
df_vaccinations = pd.read_csv('/content/drive/MyDrive/Naan Mudalvan/country_vaccinations.csv')

"""#Cloumns present in given data set"""

df_manufacturer.columns

df_vaccinations.columns

"""#Shape of DataFrames

"""

df_manufacturer.shape

df_vaccinations.shape

"""#Information about given data sets"""

df_manufacturer.info()

df_vaccinations.info()

"""#Vaccines Manufactured on a particular Date"""

df_manufacturer = df_manufacturer[df_manufacturer.date == '2022-02-04']
df_manufacturer.head()

"""#Country wise Vaccination status on a particular Date"""

df_vaccinations = df_vaccinations[df_vaccinations.date == '2022-02-04']
df_vaccinations.head()

"""#3. Preprocessing Data

#Checking for Missing Values

No missing values in manufacturers table
"""

df_manufacturer.isna().sum()

"""But, it is present in country wise vaccine utilization"""

df_vaccinations.isna().sum()

"""#Dropping Missing values present in total_vaccinations attribute"""

df_vaccinations = df_vaccinations.drop(df_vaccinations[df_vaccinations.total_vaccinations.isna()].index)

df_vaccinations.isna().sum()

"""#Dropping Missing values present in people_vaccinated & daily_vaccinations_raw attributes"""

df_vaccinations = df_vaccinations.drop(df_vaccinations[df_vaccinations.people_vaccinated.isna()].index)
df_vaccinations = df_vaccinations.drop(df_vaccinations[df_vaccinations.daily_vaccinations_raw.isna()].index)

df_vaccinations.isna().sum()

"""#Checking for Null Values"""

df_vaccinations.isnull().sum()

"""#Filling Mean values"""

df_vaccinations = df_vaccinations.fillna(df_vaccinations.mean())

df_vaccinations.isnull().sum()

"""#Checking for Duplicated records

No duplications present
"""

duplicate_rows = df_vaccinations[df_vaccinations.duplicated()]
print(len(duplicate_rows))
print(duplicate_rows)

"""#4. Visualization of Data

#Heatmap Visualization to check correlation between attributes
"""

plt.subplots(figsize = (10,10))
sns.heatmap(df_vaccinations.corr(), annot = True, square = True)
plt.show()

"""#Top countries in vaccinations Utilization"""

df_vaccinations["Total_vaccinations_count"]= df_vaccinations.groupby("country").total_vaccinations.tail(1)
df_vaccinations.groupby("country")["Total_vaccinations_count"].mean().sort_values(ascending= False).head(10)

x= df_vaccinations.groupby("country")["Total_vaccinations_count"].mean().sort_values(ascending= False).head(10)
sns.set_style("whitegrid")
plt.figure(figsize= (8,8))
ax= sns.barplot(x=x.values,y=x.index)
ax.set_xlabel("Total vaccinations count")
plt.show()

"""#Fully Vaccinated Count"""

df_vaccinations["Full_vaccinations_count"]= df_vaccinations.groupby("country").people_fully_vaccinated.tail(1)

df_vaccinations.groupby("country")["Full_vaccinations_count"].mean().sort_values(ascending= False).head(10)

#barplot visualization of top countries with most full vaccinations

sns.set_style("whitegrid")
plt.figure(figsize= (8,8))
ax= sns.barplot(x=x.values,y=x.index)
ax.set_xlabel("Fully vaccinated count")
plt.show()

"""#Most commonly used vaccines in the World"""

total  = df_manufacturer.groupby('vaccine').sum()

px.bar(x=total.index, y=total['total_vaccinations'],
                   title='Most Used Vaccine in the World')

df_vaccinations = df_vaccinations[ df_vaccinations['date'] == '2022-02-04']
df_vaccinations = df_vaccinations.sort_values(by='people_vaccinated_per_hundred',ascending=False)
fig=px.bar(df_vaccinations.head(10), x='country', y='people_vaccinated_per_hundred',
                   title='People Vaccinated per Hundred for the Date 2022-02-04')
fig.update_layout(xaxis_tickangle=-45)
fig.show()

"""#Type of vaccine utilized Vs Count"""

plt.figure(figsize=(15,15))
sns.countplot(y= "vaccines",data= df_vaccinations)
plt.show()

"""#Vaccination per hundred top countries"""

df_vaccinations["Total_vaccinations_per_hundred"]= df_vaccinations.groupby("country").total_vaccinations_per_hundred.tail(1)
x= df_vaccinations.groupby("country")["Total_vaccinations_per_hundred"].mean().sort_values(ascending= False).head(10)
plt.figure(figsize= (8,8))
ax= sns.barplot(x=x.values,y=x.index)
ax.set_xlabel("vaccinations per hundred")
plt.show()

"""#Statistical Analysis of given Data sets"""

df_manufacturer.describe()

df_vaccinations.describe()

df_manufacturer.vaccine.value_counts()

"""#Daily vaccinations per million top countries"""

df_vaccinations.groupby("country")["daily_vaccinations_per_million"].mean().sort_values(ascending= False).head(20)

"""#Preferred vaccine in India"""

x= df_vaccinations[df_vaccinations["country"]=="India"]
z= x.vaccines.value_counts()
c= list(z.index)
c

"""#Country wise daily vaccination per million"""

def trace_bar(data, feature, title, xlab, ylab,color):
    data = data.sort_values(feature, ascending=False)
    trace = go.Bar(
            x = data['country'],
            y = data[feature],
            marker=dict(color=color),
            text=data['country']
        )
    data = [trace]

    layout = dict(title = title,
            xaxis = dict(
                title = xlab,
                showticklabels=True,
                tickangle=45,
                zeroline=True,
                zerolinewidth=1,
                zerolinecolor='grey',
                showline=True,
                linewidth=2,
                linecolor='black',
                mirror=True,
                tickfont=dict(
                        size=10,
                        color='black'),),


            yaxis = dict(
                title = ylab,
                gridcolor='lightgrey',
                zeroline=True,
                zerolinewidth=1,
                zerolinecolor='grey',
                showline=True,
                linewidth=2,
                linecolor='black',
                mirror=True),

            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            hovermode = 'closest'
             )
    fig = dict(data = data, layout = layout)
    iplot(fig)


trace_bar(df_vaccinations, 'daily_vaccinations_per_million', 'Daily vaccinations per million per country', 'Country','Daily vaccinations per million', "magenta" )

number_of_days = (df_vaccinations["date"].max() -df_vaccinations["date"].min() ).days
data=pd.DataFrame(columns=['Country', 'Vaccine', 'Total_vaccine'])
dtfrm=data[data["Vaccine"]=="Pfizer/BioNTech"]
dtfrm = dtfrm.drop(dtfrm[dtfrm['Country'] == 'European Union'].index)
dtfrm.head(10)

