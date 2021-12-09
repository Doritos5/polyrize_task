from datetime import datetime, timedelta
import string
import random

from sanic import Sanic, response
import jwt

app = Sanic(__name__)
app.config['SECRET'] = "".join(random.choice(string.ascii_lowercase) for i in range(32))

users = {"dor": "123"}

_JWT_ALG = "HS256"
_ACCESS = "access"
_REFRESH = "refresh"
_DEFAULT_TOKEN_DURATION_UNIT = "minutes"
_DEFAULT_TOKEN_DURATION_VAL = 360
_DEFAULT_TOKEN_DURATION = {
    _ACCESS: {_DEFAULT_TOKEN_DURATION_UNIT: _DEFAULT_TOKEN_DURATION_VAL},
    _REFRESH: {_DEFAULT_TOKEN_DURATION_UNIT: _DEFAULT_TOKEN_DURATION_VAL * 100},
}


def generate_token(payload: dict):
    token = jwt.encode({
        "exp": datetime.utcnow() + timedelta(minutes=30),
        "content": payload
    }, app.config['SECRET'], algorithm="HS256")

    return token


@app.route("/login", methods=['POST'])
def run(request):
    payload = request.json
    payload_username = payload["username"]

    user_ok = users.get(payload_username) and users[payload_username] == payload["password"]
    if not user_ok:
        return response.HTTPResponse(status=401,
                                     body="Incorrect user/credentials")

    return response.text(generate_token(payload=payload))


@app.route("/check_json", methods=['POST'])
def check_json(request):

    auth_header = request.headers.get('Authorization')

    try:
        jwt.decode(auth_header, app.config['SECRET'], algorithms="HS256")
    except jwt.exceptions.InvalidSignatureError as e1:
        return response.HTTPResponse(status=401,
                                     body="Incorrect JWT TOKEN!")

    res_dict = {cell["name"]: cell[key] for cell in request.json for key in cell if key.lower().endswith("val")}

    return response.json(res_dict)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1234, debug=True)
