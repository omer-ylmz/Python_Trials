from multiprocessing import connection
from unittest import result
import pandas as pd
import sqlite3

result = pd.read_csv("sample.csv")

result = pd.read_json("sample.json")

connection = sqlite3.connect("sample.db")
result = pd.read_sql_query("SELECT * FROM STUDENTS",connection)



print(result)