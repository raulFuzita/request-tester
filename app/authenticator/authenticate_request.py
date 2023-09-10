from flask import request
from dotenv import load_dotenv
from ..util.datetime import datetime_utils
from ..cipherkit.cipher import CipherPy
from ..exception.httprequest.http_error import HTTPError
import os

load_dotenv()

def authenticate_request():
    API_KEY = os.getenv("API_KEY")
    API_KEY_EXPIRATION = os.getenv("API_KEY_EXPIRATION")
    SECRET_WORD = os.getenv("SECRET_WORD")
    SALT = os.getenv("SALT")

    if API_KEY:
        if not SECRET_WORD:
            raise SystemError("SECRET_WORD must be provided if API_KEY is set")
        
        if SALT:
            cipher = CipherPy(secret_key=SECRET_WORD, salt=SALT)
        else:
            cipher = CipherPy(secret_key=SECRET_WORD)

        request_api_key = request.headers.get('Authorization')
        if not request_api_key:
            raise HTTPError("Authorization header is missing in the request", 401)
        try:
            if not cipher.validate(request_api_key, API_KEY):
                raise HTTPError("Invalid API_KEY provided in Authorization header", 401)
        except:
            raise HTTPError("Invalid API_KEY provided in Authorization header", 401)

    if API_KEY_EXPIRATION:
        try:
            expiration_date = datetime_utils.iso_to_datetime(API_KEY_EXPIRATION)
            current_date = datetime_utils.current_datetime()
            if datetime_utils.compare_datetime(current_date, expiration_date) > 0:
                raise HTTPError("API_KEY has expired", 401)
        except:
            raise SystemError("API_KEY_EXPIRATION must be a valid ISO 8601 date")
        
    return "Request authenticated"