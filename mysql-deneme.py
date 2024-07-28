import pymysql

# mydb = pymysql.connect (
#     host = "localhost",
#     user = "root",
#     password = "mysql1234",
#     database = "scholldb"
# )



# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase") //database oluşturma
# mycursor.execute("SHOW DATABASES") #database görme
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")

# print(mydb)


#insert etme

def insertProducts(list):
    mydb = pymysql.connect(
        host= "localhost",
        user= "root",
        password="mysql1234",
        database= "node_app"
    )

    cursor =mydb.cursor()
    
    sql = "INSERT INTO products (name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)
    
    try:
        mydb.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")

    except pymysql.connect.Error as err:
        print("hata;",err)
    finally:
        mydb.close()
        print("database bağlantısı kapandı")

list = []
while True:
    name = input("ürün adı: ")
    price = float(input("ürün fiyatı: "))
    image = input("ürün resmi: ")
    description = input("ürün yorumu: ")
    
    list.append((name,price,image,description))

    result = input("devam etmek istiyor musunuz")
    if (result == "h"):
        print("Kayıtlarınız veri tabanına aktarılıyor")
        print(list)
        insertProducts(list)



insertProduct(name,price,image,description)
    