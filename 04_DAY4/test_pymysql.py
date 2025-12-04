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
    database = 'testdatabase',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connection.cursor()

sql = "SELECT * FROM pets"
cursor.execute(sql)

customers = cursor.fetchall()



cursor.close()
connection.close()




