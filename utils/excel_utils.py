import allure
import openpyxl

from config.config import EXCEL_FILE, SHEET_NAME

@allure.step("1.读取测试用例")
def read_excel():
    #打开excel文件
    workbook = openpyxl.load_workbook(EXCEL_FILE)
    #选择表
    worksheet = workbook[SHEET_NAME]
    #读取数据
    data = []
    keys = [cell.value for cell in worksheet[2]]  #读取表第二行
    for row in worksheet.iter_rows(min_row=3,values_only=True):
        dict_data = dict(zip(keys,row))
        if dict_data["is true"]:
            data.append(dict_data)

    #关闭文件
    workbook.close()

    return data
