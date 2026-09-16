\## 快速开始



\### 1. 初始化数据库



\- 安装 MySQL 5.7+

\- 执行以下命令初始化（先建表，后导数据）：



mysql -u root -p < sql/schema.sql

mysql -u root -p < sql/data.sql



\- 内置测试账号：admin / 123456（在 data.sql 中创建，可自行修改）



\### 2. 配置环境



复制 config/config.local.example.yaml 为 config.local.yaml，

填入本机 MySQL 地址、账号、密码及被测系统地址（该文件已被 .gitignore 忽略，不会提交）。



\### 3. 安装依赖并运行



python -m venv venv

\# Windows: venv\\Scripts\\activate

pip install -r requirements.txt



\# 执行全部用例

pytest -v



\# 生成 Allure 报告

pytest --alluredir=reports/allure-results

allure generate reports/allure-results -o docs/allure-report --clean



> 注：用例依赖本地部署的被测系统与数据库，属于接口自动化测试的正常前置条件。

