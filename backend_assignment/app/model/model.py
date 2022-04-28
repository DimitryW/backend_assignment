
import mysql.connector
import mysql.connector.pooling
from config import dbconfig

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool", pool_size = 5, pool_reset_session=True, **dbconfig)


class BoardMsg:
    @staticmethod
    def SaveMsg(msg, pic_file=None):
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        sql = "INSERT INTO message (message, picture) VALUES (%s, %s)"
        val = (msg, pic_file)
        cursor.execute(sql, val)
        cnx.commit()
        cursor.close()
        cnx.close()
        return