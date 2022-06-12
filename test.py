#tested by Sudayon
import mysql.connector as mysql
conn = mysql.connect(host="localhost", user="root", password="", database="stud_dbase")

cur=conn.cursor()
sql="SELECT user FROM tbl_logs ORDER BY id DESC LIMIT 1"
cur.execute(sql)
last_id = cur.fetchone()

for lastID in last_id:
    print(lastID)
