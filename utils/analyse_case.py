import ast
import logging
from wsgiref import headers

import allure
import requests

from config.config import BASEURL

def safe_parse(value):
    if isinstance(value,str) and value.strip():
        return ast.literal_eval(value)
    return None


@allure.step("1.解析数据")
def http_case(case):
    method = case["method"]
    url = BASEURL + case["path"]
    headers = safe_parse(case["headers"])
    params = safe_parse(case["params"])
    data = safe_parse(case["data"])
    json = safe_parse(case["json"])
    files = safe_parse(case["files"])

    request_data  = {
        "method":method,
        "url": url,
        "headers": headers,
        "params": params,
        "data": data,
        "json": json,
        "files": files,
    }
    logging.info(f"2.解析数据：{request_data}")
    return request_data
