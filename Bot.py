import requests
import secrets  
import pandas as pd

class RequestError(Exception):
    '''
    Error in het geval de request geen 200 terug gaf
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
        self._username = "Wwwwat"
        self._password = get_my_password()
        self._state = secrets.token_hex(16)
        self._code_verifier = secrets.token_urlsafe(64)
        self._code_challenge = self._code_verifier
        self._clientid = 'PUT YOUR CLIENT ID HERE
        self._headers = {'X-MAL-CLIENT-ID': self._clientid}
        self._authtoken = PUT YOUR AUTHTOKEN HERE
    def public_request(self, url):
        mal_access_token = 'PUT YOUR ACCESS TOKEN HERE'
        url = 'https://api.myanimelist.net/v2/users/@me/animelist'
        headers = {
          'Authorization': f'Bearer {mal_access_token}',
        }
        r = requests.get(url, headers = headers)
        return r
        # if r.status_code != 200:
        #     raise RequestError(r)
        # else:
        #     data = r.json()
        return r
    def get_my_list(self):
        #curl 'https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=4' \
        #-H 'Authorization: Bearer YOUR_TOKEN'
        my_headers = {'Authorization':f'Bearer {self._authtoken}'}
        r = requests.get('https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&status=watching', headers = my_headers)
        r.raise_for_status()
        return r.json()
    def authlink(self):
    #Stappen voor OAuth:
        #1. Maak een server met de python flask library en run de server
        #2. Ga naar de 0auth link
        #3. Klik op allow, je gaat nu naar een link die start met 127.0.0.1/...
        #4. Zet achter de link de poort die je gebruikt. Dus stel je gebruikt port 8000 in het flask script, ga dan naar 127.0.0.1:8000/...
        #5. Ga terug naar de runnende server. Er is nu iets geprint met de code en de state die jij hebt meegegeven. Kopieëer de code (alleen de code, niet de state)
        #6. Maak nu een post request waarin je de code submit die je net hebt gekregen
        #7. Hoop dat er geen errors in het process zaten en je nu de token terug hebt gekregen
        print(self._code_challenge)
        return f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={self._clientid}&code_challenge={self._code_challenge}&state={self._state}&redirect_uri=127.0.0.1:5000'
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
        # base_url = 'https://myanimelist.net/v1/oauth2/token'
        # data = {
        #     'client_id': self._clientid,
        #     'code': code,
        #     'grant_type': 'authorization_code',
        #     'code_verifier': self._code_verifier,
        #     'redirect_uri':'127.0.0.1:5000'
        # }
        
        
        # response = requests.post(base_url, data=data, auth = client_auth)
        if response.status_code == 200:
            access_token = response.json()
            return access_token
            # Do something with the access token
        else:
            print(response.url)
            print(f"Error: {response.status_code} - {response.text}")
            return response
    
    # def authorize(self):
    #     authorization_params = {
    #         "response_type": "code",
    #         "client_id": self._clientid,
    #         "state": self._state,
    #         "redirect_uri": "http://127.0.0.1",
    #         "code_challenge": self._code_challenge,
    #         "code_challenge_method": "plain",
    #         "grant_type":"authorization_code"
    #     }
    #     authorization_url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={self._clientid}&state={self._state}&redirect_uri=http://127.0.0.1:8080&code_challenge={self._code_challenge}&code_challenge_method=plain'
    #     #response = requests.post(authorization_url), data = authorization_params)
    #     auth = requests.auth.HTTPBasicAuth(self._clientid, "")
    #     response = requests.get(authorization_url, auth = auth)
    #     return response
    #     # if response.status_code == 200:
    #     #     return response
    #     # else:
    #     #     raise RequestError(response)
    # def authorize2(self):
    #     client_auth = requests.auth.HTTPBasicAuth(self._clientid, "")
    #     post_data = {"grant_type": "authorization_code", "username": self._username, "password": self._password}
    #     headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    #     response = requests.get("https://myanimelist.net/v1/oauth2/authorize", auth=client_auth, data=post_data, headers=headers)
    #     return response
    #     # if response.status_code == 200:
    #     #     return response
    #     # else:
    #     #     raise RequestError(response)
    # def authorize3(self):
    #     client_auth = requests.auth.HTTPBasicAuth(self._clientid, "")
    #     post_data = {"grant_type": "authorization_code", "username": self._username, "password": self._password}
    #     headers = {
    #         "response_type": "code",
    #         "client_id": self._clientid,
    #         "state": self._state,
    #         "redirect_uri": "http://127.0.0.1",
    #         "code_challenge": self._code_challenge,
    #         "code_challenge_method": "plain",
    #         "grant_type":"authorization_code"
    #     }
    #     response = requests.get("https://myanimelist.net/v1/oauth2/authorize", auth=client_auth, data=post_data, headers=headers)
    #     return response
    #     # if response.status_code == 200:
    #     #     return response
    #     # else:
    #     #     raise RequestError(response)
        
    
if __name__ == "__main__":
    bot = MyBot()
    # r = bot.public_request('https://api.myanimelist.net/v2/users/wwwwat/animelist?status=1')
    # data = r.json()
    authlink = bot.authlink()
    print(f"Authlink:\n{authlink}")
    #my_list = pd.DataFrame(bot.get_my_list()['data'])
