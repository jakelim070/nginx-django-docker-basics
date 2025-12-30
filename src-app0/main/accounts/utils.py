import jwt
import datetime
from django.conf import settings
from django.contrib.auth.models import User

def generate_tokens(user: User):
    now = datetime.datetime.utcnow()

    access_payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': now + datetime.timedelta(seconds=settings.JWT_SETTINGS['ACCESS_TOKEN_LIFETIME']),
        'type': 'access'
    }

    refresh_payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': now + datetime.timedelta(seconds=settings.JWT_SETTINGS['REFRESH_TOKEN_LIFETIME']),
        'type': 'refresh'
    }

    access_token = jwt.encode(access_payload, settings.SECRET_KEY, algorithm=settings.JWT_SETTINGS['ALGORITHM'])
    refresh_token = jwt.encode(refresh_payload, settings.SECRET_KEY, algorithm=settings.JWT_SETTINGS['ALGORITHM'])

    return {
        'access': access_token,
        'refresh': refresh_token
    }

def decode_token(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_SETTINGS['ALGORITHM']])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
