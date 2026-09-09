import ast
import logging

import allure
import jsonpath

from utils.send_request import send_jdbc_request

@allure.step("4.json提取")
def json_extractor(case,all,res):
    if case["jsonExData"]:
        for key, value in ast.literal_eval(case["jsonExData"]).items():
            value = jsonpath.jsonpath(res.json(), value)[0]
            all[key] = value
        logging.info(f"json提取，根据{case['jsonExData']}提取数据,此时全局变量：{all}")

def sql_extractor(case,all):
    if case["sqlExData"]:
        allure.dynamic.feature("4.sql提取")
        for key, value in ast.literal_eval(case["sqlExData"]).items():
            value = send_jdbc_request(value)
            all[key] = value
        logging.info(f"sql提取，根据{case['sqlExData']}提取数据,此时全局变量：{all}")