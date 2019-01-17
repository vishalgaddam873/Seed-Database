import mydb
db = mydb.load('table.db')
db.set('sunil','vandu')
db.dump()
b = db.exists('sunil')
print(b)
c = db.total_keys()
print(c)
d = db.del_db()
print(d)

e = db.random_insert(10)
print(e)

