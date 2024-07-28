import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="node_app"
)

cursor = connection.cursor()

# sql = "SELECT * FROM products"
# sql = "SELECT * FROM categories"
sql = "SELECT * FROM products join categories on products.categoryid = categories.id"

cursor.execute(sql)

try:
    result=cursor.fetchall()

    for i in result:
        print(i)
except pymysql.Connect.Error as err:
    print("hata",err)
finally:
    connection.close()
    print("database kapandı")
    
