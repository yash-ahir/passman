# PassMan
---
PassMan is a simple, cross platform password manager written in Python.

  - AES(CBC Mode) for password encryption.
  - Passwords are stored in MongoDB.
  - In-built random password generator.

---
### Install dependecies

Requires Python 3, only tested with 3.8.3 as of now.

MongoDB 4.2.8 or higher to run (untested with prior versions).
https://docs.mongodb.com/manual/administration/install-community/

Install the required libraries, change directory to src/ and run it.

```
pip install pyqt5 padding pycryptodome pymongo
```

---
### Run it
```
python main.py
```
Feel free to open an issue in case of any difficulties.

---
### Goals
- [x] Complete base UI functionality.
- [x] Replace pycrypto with pycryptodome.
- [ ] Add icons with QResources.
- [ ] Add master password migration and reset options.
- [ ] Add clear entries option.
- [ ] Package into binary executable.

---
### License
**GPLv3**
