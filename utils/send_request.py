import logging

import allure
import pymysql
import requests
from email_validator import DEFAULT_TIMEOUT

from config.config import *

SESSION = requests.Session   

DEFAULT_TIMEOUT = (5,10)

RETRY_TIMES = 2

@allure.step("2.处理http请求")
def send_http_request(**request_data):
    request_data.setdefault("timeout", DEFAULT_TIMEOUT)  # 看data文件中有没有“timeout”，没有就加上
    last_error = None
    for attempt in range(RETRY_TIMES + 1):  # ③ 最多试 3 次
        try:
            res = requests.request(**request_data)
            logging.info(f"3.http请求响应：{res}")
            return res
        except(requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            last_error = e
            logging.warning(f"第{attempt + 1}次请求失败（{type(e).__name__}），正在重试...")
    raise last_error

def send_jdbc_request(sql):
    conn = pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result