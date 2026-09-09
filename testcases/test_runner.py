import ast
import logging

import jsonpath
import pytest
import requests
from jinja2 import Template

from utils.allure_utils import allure_init
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import read_excel

from utils.analyse_case import http_case
from utils.extractor import *
from utils.send_request import send_http_request


class TestRunner:
    #读取测试用例数据
    data = read_excel()
    #定义全局变量
    all = {}

    @pytest.mark.parametrize("case",data)
    def test_case(self,case):
        all = self.all
        logging.info(f"全局变量值{all}")
        case = ast.literal_eval(Template(str(case)).render(all))

        allure_init(case)

        logging.info(f"1.编号：{case["id"]}  模块：{case["feature"]}  场景：{case["story"]}  标题：{case["title"]}")

        #1解析请求数据
        request_data = http_case(case)

        #2.发送请求
        res = send_http_request(**request_data)



        #3.处理断言
        #http断言
        http_assert(case, res)

        #数据库断言
        jdbc_assert(case)

        #4.提取
        #json提取
        json_extractor(case,all,res)

        #数据库提取
        sql_extractor(case,all)
