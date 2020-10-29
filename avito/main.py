from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from hashlib import md5

import time

from cryptools import encrypt, decrypt
from database_tools import insert_into_db, select_from_db, delete_from_db



class EncryptData(BaseModel):
    secret: str
    passphrase: Optional[str] = None


app = FastAPI()


@app.post('/generate/')
async def generate(data: EncryptData) -> dict:
    """ Puts secret into database and return secret_key. """
    secret_key = md5(str(time.time()).encode()).hexdigest()
    password = data.passphrase
    
    if data.passphrase is None:
        password = ''
    
    encrypted = encrypt(password, data.secret.encode())
    password_encrypted = md5(password.encode()).hexdigest()
    insert_into_db((secret_key, password_encrypted, encrypted))
    return {'secret_key': secret_key}


@app.post("/secrets/{secret_key}")
async def secrets(secret_key: str, passphrase: Optional[str] = None) -> dict:
    """ Return secret if password is correct. """
    row = select_from_db(secret_key)

    if passphrase is None:
        passphrase = ''
    
    if row is None or row[1] != md5(passphrase.encode()).hexdigest():
        raise HTTPException(status_code=404, detail="Item not found") 
    
    try:
        secret = decrypt(passphrase, row[2])
    except:
        raise HTTPException(status_code=404, detail="Item not found") 

    delete_from_db(secret_key)

    return {'secret': secret}
