#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:02:08 2017

@author: abhilashsk
"""
#importing pandas, numpy and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

#Function for Data ingestion stage using read_csv
def readData():
    try:
        return pd.read_csv('./Airplane_Crashes_and_Fatalities_Since_1908.csv') #storing the data in a DataFrame
    except FileNotFoundError:
        print("The file does not exist.")
    else:
        print("Dataset loaded successfully")
    
    #print(crashds.head(2))

#Function for Data cleaning stage
def cleanData(dataset):
    del dataset['Summary']  #Summary column is dropped
    
    #removing invalid values
    ds1=dataset.isnull().any()
#    print(ds1)
    if True in ds1.values:  #if there are invalid value drop them
        print("There are invalid values in the dataset. Deleting invalid values...")
        dataset=dataset.dropna()
        print("Invalid values have been dropped.\n")
#        ds1=dataset.isnull().any()
#        print(ds1)
    else:   #if there are no invalid values
        print("There are no invalid values in the dataset.\n")
        
    #changing the format and type of values in Date column
    shape=dataset.shape
    for x in range(shape[0]):
        dataset.iloc[x,0]=datetime.datetime.strptime(dataset.iloc[x,0], "%m/%d/%Y").date()
        
    #returning dataset
    return dataset

#Function for displaying data regarding the data set
def defDataset(dataset):
    #print(dataset.head())
    #print(dataset.tail())
    shape=dataset.shape
    columns=dataset.columns
    print("The Indices of the dataset: ",columns,"\nThe shape of dataset: ",shape)
    #dataset.plot(x='Operator',y='Fatalities',figsize=(15,10),kind='bar')


#Function to return column and rows of the dataset
def retData(dataset,cols,rows=0):   #cols will be a list of columns selected
    columns=dataset.columns
    for x in columns:
        print(dataset[x])


ds=readData()
#ds=cleanData(ds)
#print(ds.head(10))
