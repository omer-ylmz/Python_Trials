import pandas as pd

df = pd.read_csv("youtube-ing.csv")

result = df.head(10)

result = df[5:20].head(5)

result = df.columns
result = len(df.columns)

df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)

result = df["likes"].mean()
result = df["dislikes"].mean()

result = df[:50][["title","likes","dislikes"]]

result = df[df["views"].max() == df["views"]]["title"].iloc[0]

result = df[df["views"].min() == df["views"]]["title"].iloc[0]

result = df.sort_values("views",ascending=False).head(10)[["title","views"]]

result = df.groupby("category_id").mean().sort_values("likes",ascending=False)

result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

result = df["category_id"].value_counts()

df["title_len"] = pd.Series





print(result)