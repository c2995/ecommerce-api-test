import os
from dotenv import load_dotenv



load_dotenv()
BASEURL = os.getenv("BASEURL","http://localhost:3000")
EXCEL_FILE = os.getenv("EXCEL_FILE", "./data/测试用例_200条_fix.xlsx")
SHEET_NAME = os.getenv("SHEET_NAME", "Sheet1")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_DATABASE = os.getenv("DB_DATABASE", "wisdom_shop_api")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD","123456")


