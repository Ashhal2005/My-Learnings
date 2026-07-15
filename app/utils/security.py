import bcrypt

def hash_pswd(password:str):
    pswd = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=10)
    pswd = bcrypt.hashpw(pswd, salt)
    return pswd.decode('utf-8')