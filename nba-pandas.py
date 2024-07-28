import pandas as pd

df = pd.read_csv("nba.csv")

#İlk 10 kaydı getiriniz.

result = df.head(10)

#Toplam kaç kayıt vardır.

result = len(df.index)

#Tüm oyuncuların toplam maaş ortalaması

result = df["Salary"].sum()

# 4- En yüksek maaşı ne kadardır ?

result = df["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?

result = df[df["Salary"] == df["Salary"].max() ]["Name"].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.

result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age",ascending=False)


# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?

result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?

result = df.groupby("Team").mean()["Salary"]

# 9- Kaç farklı takım mevcut ?

result = len(df.groupby("Team"))

result = df["Team"].unique()

# 10- Her takımda kaç oyuncu oynamaktadır ?

result = df["Team"].value_counts()



print(result)