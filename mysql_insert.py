import pymysql
from datetime import datetime
from connection import mydb

class Student:
    connection = mydb
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender



    def saveStudent(self):
        sql = "INSERT INTO student (StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)

        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
            print(f"Son eklenen kaydın id: {Student.mycursor.lastrowid}")
        except pymysql.connect.Error as err:
            print("Hata ",err)
        finally:
            Student.connection.close()
    
    @staticmethod
    def saveStudents(students):


        sql = "INSERT INTO student (StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
            print(f"Son eklenen kaydın id: {Student.mycursor.lastrowid}")
        except pymysql.connect.Error as err:
            print("Hata ",err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id = %s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchone()
        except pymysql.connect.Error as err:
            print("error:",err)
       

    def updateStudent(self):
        sql = "update student set StudentNumber = %s,Name = %s, Surname = %s, Birthdate = %s, Gender = %s where id =%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)   

        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi")
        except pymysql.connect.Error as err:
            print("Error",err)

    @staticmethod
    def updateStudents(liste):
        sql = "update student set StudentNumber = %s,Name = %s, Surname = %s, Birthdate = %s, Gender = %s where id =%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi")
        except pymysql.connect.Error as err:
            print("Error",err)
            

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from student where Gender = %s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except pymysql.connect.Error as err:
            print("error:",err)

# deneme = Student.getStudentById(20)        
# print(deneme)

# student = Student(deneme[0],deneme[1],deneme[2],deneme[3],deneme[4],deneme[5])
# student.name ="Çınar"
# student.surname = "Turan"

# student.updateStudent()

students = Student.getStudentsGender("E")
print(students)

liste = []
for s in students:
    s = list(s)
    s[2] = "Mr "+ s[2]
    liste.append(s)

Student.updateStudents(liste)

# omer = Student("105","ömer","yilmaz",datetime(2002,2,18),"E")
# omer.saveStudent()



# sql = "INSERT INTO student (StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
# ogrenciler = [
# ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
# ("302","Ali","Can",datetime(2005, 6, 17),"E"),
# ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
# ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
# ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
# ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
# ]
# cursor.executemany(sql,ogrenciler)

# Student.saveStudents(ogrenciler)

# try:
#     mydb.commit()
#     print(f"{cursor.rowcount} tane kayıt eklendi")
#     print(f"Son eklenen kaydın id: {cursor.lastrowid}")
# except pymysql.connect.Error as err:
#     print("Hata ",err)
# finally:
#     mydb.close

#######################################################

# def getProducts():
#     connection = pymysql.connect(
#         host="localhost",
#         user="root",
#         password="mysql1234",
#         database="node_app"
#     )

#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM products")

#     result = cursor.fetchall()

#     for i in result:
#         print(i)