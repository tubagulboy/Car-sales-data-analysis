import pandas as pd
import matplotlib.pyplot as plt

#read data
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv("mercedes_benz_sales_2020_2025.csv")
print(data.head())
print(data.info())

#Best selling models
print(data["Model"].value_counts().head(15))

data["Model"].value_counts().head(15).plot(kind="bar")
plt.title("TOP ON MERCEDES MODELS SALES")
plt.xlabel("Model")
plt.ylabel("Sales")
plt.show()

#Fuel type analysis

print(data["Fuel Type"].value_counts().plot(kind="bar"))
plt.title("FUEL TYPE DISTRIBITION")
plt.xlabel("Fuel Type")
plt.ylabel("Number of cars")
plt.show()

#Sales year analysis
year_sales = data["Year"].value_counts().sort_index()
print(year_sales)
year_sales.plot(kind="line")
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

#######################################

print(data.isnull().sum())


#If there is missing data

data = data.dropna()

#####

print(data.dtypes)

#Basic data summary

print(data.describe())