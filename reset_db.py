# -*- coding: utf-8 -*-
"""测试环境数据重置脚本：每次执行 pytest 前运行，恢复订单/商品/购物车/评价/售后/优惠券的 fixture 状态。
用法: D:/python/python.exe reset_db.py
"""
import pymysql

from config.config import DB_HOST, DB_PORT, DB_DATABASE, DB_USER, DB_PASSWORD

def reset():

    c = pymysql.connect(host=DB_HOST, port=DB_PORT, database=DB_DATABASE,
                            user=DB_USER, password=DB_PASSWORD, charset='utf8')
    cur = c.cursor()
    # 1. 商品8 恢复上架（121 删除用例可能将其软删）
    cur.execute('UPDATE goods SET is_delete=0 WHERE goods_id=8')
    # 2. 内置订单恢复初始状态（901/906 待付款、903 待收货可确认、905 已完成可评价售后）
    cur.execute('UPDATE order_info SET order_status=10, pay_status=0 WHERE order_id IN (901,906)')
    cur.execute('UPDATE order_info SET order_status=30, pay_status=1, delivery_status=1 WHERE order_id=903')
    cur.execute("UPDATE order_info SET order_status=40, pay_status=1, delivery_status=2, express_id=1, express_no='SF100003' WHERE order_id=905")
    # 3. 清空状态型数据（评价/售后/领券记录）
    cur.execute('DELETE FROM user_coupon WHERE user_id=2')
    cur.execute('DELETE FROM comment WHERE order_id=905')
    cur.execute('DELETE FROM order_refund')
    # 4. 重置 user2 购物车（26/27/28 对应商品8的3个SKU）
    cur.execute('DELETE FROM cart WHERE user_id=2')
    cur.execute("INSERT INTO cart (cart_id,user_id,goods_id,sku_id,goods_num,create_time,update_time) "
                "VALUES (26,2,8,26,1,NOW(),NOW()),(27,2,8,27,1,NOW(),NOW()),(28,2,8,28,1,NOW(),NOW())")
    c.commit()
    cur.execute('SELECT (SELECT order_status FROM order_info WHERE order_id=901),(SELECT order_status FROM order_info WHERE order_id=903),'
                '(SELECT is_delete FROM goods WHERE goods_id=8),(SELECT COUNT(*) FROM cart WHERE user_id=2),'
                '(SELECT COUNT(*) FROM user_coupon WHERE user_id=2),(SELECT COUNT(*) FROM order_refund)')
    result = cur.fetchall()
    c.close()
    return result

if __name__ == '__main__':
    print('reset ok:',reset())