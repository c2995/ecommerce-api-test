import logging

import allure
import jsonpath

from utils.send_request import send_jdbc_request

@allure.step("3.http断言")
def http_assert(case,res):
    if case["check"]:
        result = jsonpath.jsonpath(res.json(), case["check"])[0]
        logging.info(f"4.http响应断言内容: 实际结果【{result}】 == 预期结果【{case["expected"]}】")
        assert str(result) == str(case["expected"])



def jdbc_assert(case):
    if case["sql_check"] and case["sql_expected"]:
        allure.dynamic.feature("3.jdbc断言")
        result = send_jdbc_request(case["sql_check"])[0]
        logging.info(f"4.jdbc响应断言内容: 实际结果【{result}】 == 预期结果【{case["sql_expected"]}】")
        assert str(result) == str(case["sql_expected"])
