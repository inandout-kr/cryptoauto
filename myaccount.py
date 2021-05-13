import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = 'bIQ17TlUSVILX0s5tOowdiAoxSWuJosT1DxYVQNd'
secret_key = 'x31ywPx6LtJueY2yP2ZIcG3ypB9a34erWnPAn7Ow'
server_url = 'https://api.upbit.com'

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)

print(res.json())