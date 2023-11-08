import requests
import secrets  
import pandas as pd

class RequestError(Exception):
    '''
    Error in case the request didn't return a 200
    '''
    def __init__(self, r):
        self._status_code = r.status_code
        self._reason = r.reason
        self._url = r.url
    def __str__(self):
        return(f"\n{self._status_code}: {self._reason} \nInput: {self._url}")
    
def get_my_password():
    with open("password.txt", "r") as f:
        password = f.read()
    return password
    
class MyBot:
    def __init__(self):
        self._username = 'PUT YOUR MAL USERNAME HERE'
        self._password = get_my_password()
        self._state = secrets.token_hex(16)
        self._code_verifier = secrets.token_urlsafe(64)
        self._code_challenge = self._code_verifier
        self._clientid = 'PUT YOUR CLIENT ID HERE
        self._headers = {'X-MAL-CLIENT-ID': self._clientid}
        self._authtoken = PUT YOUR AUTHTOKEN HERE
    def public_request(self, url):
        '''
        Ideally you'll be using this one to access your animelist, but this only works if you made your animelist public
        '''
        mal_access_token = 'PUT YOUR ACCESS TOKEN HERE'
        url = 'https://api.myanimelist.net/v2/users/@me/animelist'
        headers = {
          'Authorization': f'Bearer {mal_access_token}',
        }
        r = requests.get(url, headers = headers)
        if r.status_code != 200:
            raise RequestError(r)
        else:
            data = r.json()

        return r
    def get_my_list(self):
        #curl 'https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=4' \
        #-H 'Authorization: Bearer YOUR_TOKEN'
        my_headers = {'Authorization':f'Bearer {self._authtoken}'}
        r = requests.get('https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&status=watching', headers = my_headers)
        r.raise_for_status()
        return r.json()
    def authlink(self, port):
        print(self._code_challenge)
        return f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={self._clientid}&code_challenge={self._code_challenge}&state={self._state}&redirect_uri=127.0.0.1:{port}'
    def get_token(self, code):
        url = 'https://myanimelist.net/v1/oauth2/token'
        data = {
            'client_id': self._clientid,
            'code': code,
            'code_verifier':self._code_verifier,
            'grant_type': 'authorization_code'
        }

        response = requests.post(url, data)
        print(self._code_verifier)
        
        if response.status_code == 200:
            access_token = response.json()
            return access_token
            # Do something with the access token
        else:
            print(response.url)
            print(f"Error: {response.status_code} - {response.text}")
            return response
if __name__ == "__main__":
    bot = MyBot()
    authlink = bot.authlink(5000) #Use the port you used in flask_server.py
    print(f"Authlink:\n{authlink}")
