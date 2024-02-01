from flask import Flask, request, jsonify
from functools import wraps
import os
import json
from sys import argv
from ids import Ids
from serviceapi.api import create_service
from serviceapi.startapi import start_service
from serviceapi.stopapi import stop_service
from serviceapi.restartapi import restart_service

app = Flask(__name__)

def CheckToken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('TOKEN')
        if token == token_user:
            return func(*args, **kwargs)
        else:
            return jsonify({'error': "403"}), 403
    return wrapper

def get_token(file):
    file = file + ".json"
    with open('token/' + file, 'r') as f:
        return (json.load(f)['token'])


@app.route('/check', methods=['GET'])
def check():
    jsoninfo = machine.check()
    return jsonify(jsoninfo), 200

@app.route('/build', methods=['GET'])
@CheckToken
def build():
    jsoninfo = machine.build()
    machine.update_db_data()
    return jsonify({"message" : jsoninfo}), 200

@app.route('/db', methods=['GET'])
@CheckToken
def see_db():
    machine.update_db_data()
    jsoninfo = machine.db
    return jsonify(jsoninfo), 200

@app.route('/raport', methods=['GET'])
@CheckToken
def see_raports():
    list_raport = os.listdir('raport/')
    return jsonify({'list raport' : list_raport}), 200

@app.route('/raport/<raport>', methods=['GET'])
@CheckToken
def see_raport(raport):
    try:
        with open('raport/' + raport, 'r') as f:
            return jsonify(json.load(f)), 200
    except FileNotFoundError:
        return jsonify({'error': "404"}), 404


@app.errorhandler(404)
def error404(e):
    return jsonify({'error': "404"}), 404

def help():
    print("Usage: python ids-api.py [command]")
    print("commands:")
    print("    run, r: run api server in terminal")
    print("    token, t: get your api token")
    print("    create_service, cs: create api service")
    print("    start_service, start: start api service")
    print("    stop_service, stop: stop api service")


if __name__ == "__main__":
    app.secret_key = get_token('tokenapi').encode('utf-8')
    token_user = get_token('tokenuser')
    machine = Ids()
    if len(argv) > 1:
        cmd = argv[1]
        if cmd == 'run' or cmd == 'r': app.run(host='0.0.0.0', port=8080, debug=True)
        elif cmd == 'help' or cmd == 'h': help()
        elif cmd == 'token' or cmd == 't': print(f'Your Token  : {token_user}')
        elif cmd == 'create_service' or cmd == 'cs': create_service()
        elif cmd == 'start_service' or cmd == 'start' : start_service()
        elif cmd == 'stop_service' or cmd == 'stop' : stop_service()
        elif cmd == 'restart_service' or cmd == 'restart' : restart_service()
        else: print("Invalid command. Type 'help' or 'h' for more information")
    else: print("Invalid command. Type 'help' or 'h' for more information")