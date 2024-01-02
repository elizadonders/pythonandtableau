# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:10:05 2023

@author: eliza
"""
import pandas as pd

#file_name = pd.read_csv('file.csv') <----- Correspode o formato para ler.

#data = pd.read_csv('transaction.csv') #Esse comando so seleciona apenas comandos se nao houver separation por'

data = pd.read_csv('transaction.csv', sep=';')

#Summary of the data (Esse comando abaixo vc obetera toda informacao da tabela)

data.info()

#working with calculations
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operation (Nessa operacao sera calculado o lucro, que sera a subtracao do preco de venda com preco de custo)
# ProfitPerItem = 21.11 - 11.73

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem 
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#Creat a Columm Calculation CostPerTransaction 
#CostPerTransaction = NumberOfItemsPurchased * CostPerItem 
# Variable = dataframe['column_name'] ----> Sintaxe

CostPerItem = data ['CostPerItem']

NumberOfItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = NumberOfItemsPurchased * CostPerItem 

#adding a new colunm to dataFrame

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per transaction

data ['SalesPerTransaction'] = data ['NumberOfItemsPurchased'] * data['SellingPricePerItem']

# Profit Calculation = Sales - Cost (Essa e a formula para o calculo do Lucro)

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/Cost

data['Markup'] =(data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

data['Markup'] = (data['ProfitPerTransaction'])/data['CostPerTransaction']

#Rouding Marking

roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)

#Combining data fields Exemplos, usar essa ideia para separar datas
#My_name= 'Elizabeth' + ' Donders'
#print(My_name)
#Esse comando abaixo coloca o separador.

#my_date = 'Day" + '-' + 'Month' + '-' + 'Year'

#Esse comando a baixo, vc pd colocar o serador de data na coluna.

# my_date = data['Day'] + '-'

#Checking columns data type.
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

print (day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year
data['date']= my_date

#Using iloc to view specific columns/rows

data.iloc[0] #views the row with index =0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column

data.iloc[4,2] #brings in 4th row, 2sd column

#Using split to split the client_keywords field
#New_var = columns.str.split('sep' , expand = True)

split_col = data ['ClientKeywords'].str.split(',', expand=True)

#Creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#Using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','0')

#Using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#How to merge files
#Bringing in new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#Mweging files: merge_df = pd.merge(df_old, df_new, on ='key')

data = pd.merge(data,seasons, on ='Month')

#Dropping columns
# df = df.drop('columnname' , axis=1)

data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data = data.drop(['Year', 'Month'], axis=1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)










