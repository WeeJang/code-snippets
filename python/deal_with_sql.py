#! /usr/bin/python 
#encoding:utf-8

import MySQLdb
import urllib2
import sys

if __name__ == '__main__':
    # ��������
    conn = MySQLdb.connect(
            host="120.131.68.189",
            user="work",
            passwd="work123456",
            db="dingfu_data",
            charset="utf8") 
    cursor = conn.cursor()  
    if not cursor:
        print("open cursor error!")
        sys.exit(-1)

    # ִ�� sql
    cursor.execute("select * from tb_related_schema")

    # ÿ���е���ͨ�� row[i] ���õ�
    rows = cursor.fetchall()
    for row in rows:
        if len(row) < 2:
            continue
        ori = row[0]
        rel = row[1]

        cursor.close()

    # ����
    conn.commit()
    conn.close()

