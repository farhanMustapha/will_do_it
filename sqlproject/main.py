import sqlite3

conn=sqlite3.connect('madb.db')
cur=conn.cursor()
#idselected=input('id')
#name=input('ton nom :')
#email=input('ton email :')
#req="CREATE TABLE student (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT NOT NULL,email TEXT NOT NULL)"
#cur.execute("INSERT INTO student (name,email) values (?,?)",(name,email))


#cur.execute("UPDATE student set name=? , email=?  WHERE id=?",(name,email,idselected))
req="SELECT * FROM student"
result=cur.execute(req)
rows=result.fetchall()
#print(rows)
print(rows[1])
"""
for row in result:
    print('-----------------')
    print("id :",row[0])
    print("name :",row[1])
    print("email :",row[2])

"""
conn.commit()
conn.close()