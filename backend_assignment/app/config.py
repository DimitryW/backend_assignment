from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")

dbconfig = {
  "host": host,
  "user": user,
  "password": password,
  "database": "dimalife"
}