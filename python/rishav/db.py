import sqlite3 as sql
connection = sql.connect("localdb")
cursor = connection.cursor()
q = open("./queries.sql").read()
q = q.split(';')
out = []
for i in q:
    out.append(i.replace('\n', ''))
try:
    for line in out:
        cursor.execute(line)
    print("Executed successfully")
except:
    pass
res = cursor.execute("select * from Player")
print(res.fetchall())