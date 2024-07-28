from tkinter.tix import COLUMN
import pandas as pd

df = pd.read_csv("imdb.csv")

#df = df.head()

#df = df.head(10)

#df = df.tail()

#df = df.tail(10)

#df = df.loc[:,"Movie_Title"]

#df = df.loc[:,["Movie_Title","Rating"]].head()

#df = df.loc[:,["Movie_Title","Rating"]].tail()



#df = df[df["Rating"]>8.0][["Movie_Title","Rating"]].head(50)

#df = df[(df["YR_Released"] >= 2014 )  & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]]

df = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title","Num_Reviews","Rating"]]
     
print(df)