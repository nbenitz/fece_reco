# This Python file uses the following encoding: utf-8
import mysql.connector

class conndb:
    def __init__(self):
        pass

    def queryResult(self, strsql):
        cnx = mysql.connector.connect(user='root', password='12345', host='127.0.0.1', database='faceReco')
        conn =  cnx.cursor()
        conn.execute(strsql)
        result = conn.fetchall()
        return result

    def queryExecute(self, strsql):
        cnx = mysql.connector.connect(user='root', password='12345', host='127.0.0.1', database='faceReco')
        conn =  cnx.cursor()
        conn.execute(strsql)
        cnx.commit()
        pass
