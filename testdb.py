from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("system", "CCbound3", "jdbc:oracle:thin:@156.140.7.173:1521:xe")

cursor = connection.cursor()
cursor.execute("""
    SELECT customer_id, product_id
    FROM sales"""
    )
for cid, pid in cursor:
    print("Values:", cid, pid)
