# Small Db
Small Db is lightweight, fast, and simple database based on the json module.
# Fun with Small Db

```
>>> import mydb

>>> db = mydb.load('test.db', True)

>>> db.set('key', 'value')

>>> db.get('key')
'value'

>>> db.dump()
True
```
