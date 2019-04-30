# Seed Database
Small Db is lightweight, fast, and simple database based on the json module.
# Fun with Seed Database

```
>>> import seed

>>> db = seed.load('test.db', True)

>>> db.set('key', 'value')

>>> db.get('key')
'value'

>>> db.dump()
True
```
