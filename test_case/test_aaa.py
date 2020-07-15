import random

import allure
import requests

from config.conf import API_URL

@allure.feature("用户管理")
@allure.story("扣款接口")
@allure.title("充值金额成功")
def test_recharge_1(db):
    with allure.step("第一步,执行sql语句"):
        res = db.select_execute("SELECT account_name FROM t_cst_account WHERE  STATUS=0 AND account_name IS NOT NULL")
    with allure.step("第二步,从查询结果随机获取一条,去第一个数据"):
        account_name = random.choice(res)[0]
    with allure.step("第三步,准备请求数据"):
        data={
        "accountName": account_name,
        "changeMoney": 50000
        }
    r = requests.post(API_URL+"/acc/recharge",json=data)
    print(r.text)

@allure.feature("用户管理")
@allure.story("扣款接口")
@allure.title("账户余额不足")
def test_recharge_2(db):
    with allure.step("第一步,执行sql语句"):
        res = db.select_execute("SELECT account_name FROM t_cst_account WHERE  STATUS=0 AND account_name IS NOT NULL")
    with allure.step("第二步,从查询结果随机获取一条,去第一个数据"):
        account_name = random.choice(res)[0]
    with allure.step("第三步,准备请求数据"):
        data={
            "accountName": account_name,
            "changeMoney": 50000
        }
    r = requests.post(API_URL+"/acc/recharge",json=data)
    print(r.text)





