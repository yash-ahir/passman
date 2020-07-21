# PassMan

PassMan is a simple, cross platform password manager written in Python.

  - AES(CBC Mode) for password encryption.
  - Passwords are stored in MongoDB.
  - In-built random password generator.

---
### Install dependecies

Requires Python 3, only tested with v3.8.3 as of now.

MongoDB 4.2.8 or higher to run (untested with prior versions).
https://docs.mongodb.com/manual/administration/install-community/

Install the required libraries, change directory to /src and run it.

```
pip install pyqt5 padding pycryptodome pymongo
```

---
### Run it
```
python main.py
```

---
### License
**GPLv3**
