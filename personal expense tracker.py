import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/ACER/Downloads/Manya Shorey python project/personal_expense_dataset.csv")
df.head()
# this will help me to undertand the data .

#checking the data now

df.info()
df.describe()
df.isnull().sum()

#Data Cleaning(a.)

df = df.drop_duplicates()
df = df[df['Amount'] < df['Amount'].quantile(0.99)]

#Standardize the values of the Category column using map() (b.)

df['Category'] = df['Category'].str.strip().str.lower().str.capitalize()
df = df.dropna()

# Convert the Amount column into an ndarray and then find out the total expenses made . (c.)
amount_array = np.array(df['Amount'])
total_expense = np.sum(amount_array)
print(total_expense)

#Add a new column "Month" to the dataset by extracting the month component from the values of the Date column . (d.)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

#Find out category -wise total expenses , average expense and maximum expense.(e.)
print(df['Category'].unique())
result=df.groupby('Category')['Amount'].agg(['sum','mean','max'])
print(result)

#Add a new column "Spending Level" to the dataset and compute its values by binning the "amount" column using labels such as - ["low"," medium","high"].(f.)

df['Spending Level'] = pd.cut(
    df['Amount'],
    bins=[0,1000,5000,10000],
    labels=['low','medium','high']
)
#Create a pivot table that shall display the total expenses made for each category in each month. (g.)

pivot = pd.pivot_table(
    df,
    values='Amount',
    index='Category',
    columns='Month',
    aggfunc='sum'
)
print(pivot)
#Compute a contingency table between the payment mode and category of expense. (h.)

ct=pd.crosstab(df['Payment_Mode'], df['Category'])
print(ct)
#Checking the final dataset
print(df.head())
