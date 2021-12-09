# polyrize_task

Just install the needed pakcages using pip install -r requirements.txt

In the server task - the server runs in port 1234
You can use http://localhost:1234/login in order to get the JWT token.
Good username:
u: "dor" p: "123"

example payload: {"username": "dor", "password": "123"}

Wronf username or password will let to 401 error

For getting the second part of the exercise:
http://localhost:1234/check_json

body:
[
  {
    "name": "device",
    "strVal": "iPhone",
    "metadata": "not interesting"
  },
  {
    "name": "isAuthorized",
    "boolVal": "false",
    "lastSeen": "not interesting"
  }
] 

HEADERS:
Authorization: <JWT_TOKEN>
