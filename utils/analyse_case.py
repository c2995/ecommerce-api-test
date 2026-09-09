import ast
import logging

import allure
import requests

from config.config import BASEURL

def safe_parse(value):
    if isinstance(value,str) and value.strip():
        return ast.literal_eval(value)
    return None

def open_upload_files(files):
    if not files:
        return None
    result = {}
    for key,value in files.items():
        if isinstance(value,str):
            result[key] = open(value,"rb")
        elif isinstance(value,(tuple,list)):
            f_name = value[0]
            f_path = value[1]
            f_type = value[2] if len(value) > 2 else None
            f_obj = open(f_path,"rb")
            result[key] = (f_name,f_obj,f_type) if f_type else (f_name,f_obj)
        else:
            result[key] = value

    return result

def close_upload_files(files):
    if not files:
        return
    for f in files.values():
        if isinstance(f,tuple):
            f = f[1]
        if hasattr(f,"close"):
            f.close()

@allure.step("1.解析数据")
def http_case(case):
    method = case["method"]
    url = BASEURL + case["path"]
    headers = safe_parse(case["headers"])
    params = safe_parse(case["params"])
    data = safe_parse(case["data"])
    json = safe_parse(case["json"])
    files = open_upload_files(safe_parse(case["files"]))

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
