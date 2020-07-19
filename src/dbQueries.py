from pymongo import MongoClient
from crypt import *
from os import urandom

client = MongoClient()
db = client["passman"]
collection = db["entries"]

def setMasterkey(key):
    salt = urandom(16)
    collection.insert_one({"_id": 1, "key": hashKey(key, salt).hex(), "salt": salt.hex()})

def checkMasterkey():
    if collection.find_one({"_id": 1}) == None:
        return False
    else:
        return True

def getMasterkey():
    entries = collection.find_one({"_id": 1}, {"_id": 0})
    hashedKey = entries["key"]
    salt = entries["salt"]
    return hashedKey, salt

def addEntry(key, title, account, password, note = ""):
    iv = urandom(16)
    password = encrypt(password, key, iv)
    collection.insert_one({"title": title, "account": account, "password": password.hex(), "note": note, "iv": iv.hex()})

def editEntry(entryId, key, title, account, password, note = ""):
    iv = urandom(16)
    password = encrypt(password, key, iv)
    collection.find_one_and_update({"_id": entryId}, {"$set": {"title": title, "account": account, "password": password.hex(), "note": note, "iv": iv.hex()}})

def removeEntry(entryId):
    collection.delete_one({"_id": entryId})

def getTitle(entryId):
    entry = collection.find_one({"_id": entryId})
    return entry["title"]

def getAccount(entryId):
    entry = collection.find_one({"_id": entryId})
    return entry["account"]

def getPassword(entryId, key):
    entries = collection.find_one({"_id": entryId})
    iv = bytes.fromhex(entries["iv"])
    ciphertext = bytes.fromhex(entries["password"])
    password = decrypt(ciphertext, key, iv)
    return password

def getNote(entryId):
    entry = collection.find_one({"_id": entryId})
    return entry["note"]

def getAll():
    entries = collection.find({}, {"key": 0, "salt": 0})
    data = list()
    for entry in entries:
        if entry == {'_id': 1}:
            continue
        else:
            data.append(entry)
    return data