#!/usr/bin/python

import sqlite3

class _db():
    def __init__(self):
        self.conn = sqlite3.connect('100.db')
        print ("数据库打开成功")
    def close(self):
        print ("数据库断开成功")
        self.conn.close()
    def new(self):
        c = self.conn.cursor()    
        
        c.execute('''CREATE TABLE "USER" (
            "id" INT NOT NULL,
            "name" TEXT NOT NULL,
            "age" INT NOT NULL,
            "height" DOUBLE(50),
            "weight" DOUBLE(50),
            "createTime" DATETIME,
            "updateTime" DATETIME,
            "deleteTime" DATETIME,
            "flag" BOOLEAN,
            "trainer" TEXT,
            PRIMARY KEY ("id")
            );''')
        print ("数据表创建成功")
        self.conn.commit()
        self.conn.close()
db = _db().conn