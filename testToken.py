from functools import wraps
from flask import request, jsonify
import json

def get_token_user():
    with open("token/tokenuser.json", "r") as fichier: return json.load(fichier)['token']

token_user = get_token_user()

class TestToken:
    def CheckToken(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('TOKEN')
            if token == token_user:
                return func(*args, **kwargs)
            else:
                return jsonify({'error': "403"}), 403
        return wrapper