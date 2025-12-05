import pymysql
import dotenv
import os


dotenv.load_dotenv()
DB_PWD = os.getenv("DB_PWD")

#db 연결
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password = DB_PWD,
    database = 'classicmodels',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connection.cursor()

#데이터 조회 SELECT
sql = "SELECT * FROM customers"
cursor.execute(sql)

customers = cursor.fetchone()
print("pets:", customers['customerNumber'])
print("pets:", customers['customerName'])
print("pets:", customers['country'])

cursor.close()
connection.close()

#데이터 입력 INSERT

# sql = "INSERT INTO pets (name, species, breed) VALUES (%s, %s, %s)"
# values = ("Buddy", "Dog", "Golden Retriever")



