<h1 align="center">Seed Database</h1>

Seed Database is lightweight, fast, and simple database based on the json module.

## Instructions of usage

Install important tools using command :
  * `sudo apt-get install git`
  * `sudo apt install python3-pip`

Clone this app using the command:
  * `git clone https://github.com/vishalgaddam873/Seed-Database.git`


### Step 3:
create a database using command:
  * `python3 test.py`


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
