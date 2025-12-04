import mysql.connector
from faker import Faker
import random
import dotenv
import os


dotenv.load_dotenv()
DB_PWD = os.getenv("DB_PWD")

# MySQL 연결 설정
db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = DB_PWD,
    database = "testdatabase"
)

# MySQL 연결
cursor = db_connection.cursor()
fake = Faker()

# users 데이터 생성
for _ in range(100):
    username = fake.user_name()
    email = fake.email()
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    cursor.execute(sql, (username, email))

sql = "SELECT user_id FROM users"
cursor.execute(sql)
valid_user_id = [row[0] for row in cursor.fetchall()]

for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = fake.word()
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders (user_id, product_name, quantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user_id, product_name, quantity))
    except: #mysql.connector.IntegrityError:
        #유효하지않은 user_id로 인한 오류
        pass



db_connection.commit()
cursor.close()
db_connection.close()
