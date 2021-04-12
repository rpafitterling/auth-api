from passlib.hash import pbkdf2_sha256

def hash_password(clear_password):
    return pbkdf2_sha256.hash(clear_password)

def verify_password(clear_password, hashed_password):
    return pbkdf2_sha256.verify(clear_password, hashed_password)

