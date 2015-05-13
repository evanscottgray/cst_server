from flask import Flask
from flask import abort, request, jsonify
from flask.ext.cors import CORS
import subprocess
import utils
import os.path

app = Flask(__name__)
cors = CORS(app)


def get_token():
    cmd = app.config.get('token_command')
    p = subprocess.Popen([cmd], stdout=subprocess.PIPE)
    s = p.communicate()[0]
    return s.strip('\n')


def get_user():
    u = app.config.get('user')
    return u


@app.route('/token')
def token():
    k = request.args.get('key')
    if k != app.config.get('api_key'):
        abort(403)
    return jsonify({'token': get_token(), 'user': get_user()}), 200


if __name__ == '__main__':
    crt = os.path.join(os.path.dirname(__file__), 'ssl/server.crt')
    key = os.path.join(os.path.dirname(__file__), 'ssl/server.key')
    app.config.update(utils.parse_config())
    app.run(host='127.0.0.1', port=15000, ssl_context=(crt, key))
