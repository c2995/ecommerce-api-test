# ecommerce-api-test

基于 Python + Pytest 的电商系统接口自动化测试项目，采用**数据驱动**设计：Excel 管理用例、HTTP + 数据库双重断言、全局变量提取与传递，Allure 生成可视化测试报告并部署到 GitHub Pages 在线查看。

- 测试用例：**201 条，全部通过**
- 在线测试报告：https://c2995.github.io/ecommerce-api-test/allure-report/

## 功能特性

- **数据驱动**：用例全部写在 Excel 中，新增用例无需修改代码
- **双重断言**：接口响应断言 + MySQL 数据库断言，验证数据是否正确落库
- **全局变量提取**：接口返回值 / 查询结果可提取为全局变量，供后续用例引用（token、订单号等）
- **模板渲染**：用例支持 Jinja2 模板语法引用变量，实现参数联动
- **报告可视化**：Allure 报告通过 GitHub Pages 在线部署，随时可查看
- **日志记录**：Pytest 日志按用例输出到 log/

## 技术栈

Python 3.12 · Pytest · Requests · PyMySQL · Allure · OpenPyXL · python-dotenv · Jinja2

## 目录结构

```
.
├── config/              # 配置读取（config.py 从 .env 加载）
├── data/                # 测试用例 Excel 与初始化数据
├── sql/                 # 数据库脚本（schema.sql 建表 / data.sql 造数）
├── testcases/           # 用例执行入口（数据驱动 runner）
├── utils/               # 公共封装：请求发送、断言、Excel 读取、变量提取、Allure
├── docs/allure-report/  # Allure 在线报告（GitHub Pages 部署目录）
├── conftest.py          # Pytest 夹具
├── reset_db.py          # 数据库重置
├── run.py               # 一键运行入口
└── requirements.txt     # 依赖清单
```

## 快速开始

### 1. 初始化数据库

- 安装 MySQL 5.7+
- 执行以下命令初始化（先建表，后导数据）：

```bash
mysql -u root -p < sql/schema.sql
mysql -u root -p < sql/data.sql
```

- 内置测试账号：admin / 123456（在 data.sql 中创建，可自行修改）

### 2. 配置环境

- 复制 `.env.example` 为 `.env`，填入本机 MySQL 地址、账号、密码及被测系统地址（`.env` 已被 .gitignore 忽略，不会提交）。

### 3. 安装依赖并运行

```bash
python -m venv venv
# Windows: venv\Scripts\activate
pip install -r requirements.txt
```

执行全部用例：

```bash
pytest -v
```

生成 Allure 报告：

```bash
pytest --alluredir=reports/allure-results
allure generate reports/allure-results -o docs/allure-report --clean
```

## 测试报告

- Allure 报告（在线查看）：https://c2995.github.io/ecommerce-api-test/allure-report/

> 注：用例依赖本地部署的被测系统与数据库，属于接口自动化测试的正常前置条件。
