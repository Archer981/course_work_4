import hashlib
import base64
from constants import HASH_ALGO, PWD_HASH_SALT, PWD_HASH_ITERATIONS


def get_hash(password):
    return base64.b64encode(
        hashlib.pbkdf2_hmac(
            HASH_ALGO,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
    )
