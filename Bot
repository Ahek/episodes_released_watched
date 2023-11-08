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
        self._clientid = '4564e2600d613d7c881489fd99d0cfaa'
        self._headers = {'X-MAL-CLIENT-ID': self._clientid}
        self._authtoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBkODdmMWZiZDNjYTUzZDY2OGY3NmYxNGRjN2Y4ODkzNWRlNTI4N2Q5MTQ0Y2ZmMmYzNGRjMzNiYmQ4NDg1OTdjNWYxNzc0M2E3NDRlMGI2In0.eyJhdWQiOiI0NTY0ZTI2MDBkNjEzZDdjODgxNDg5ZmQ5OWQwY2ZhYSIsImp0aSI6IjBkODdmMWZiZDNjYTUzZDY2OGY3NmYxNGRjN2Y4ODkzNWRlNTI4N2Q5MTQ0Y2ZmMmYzNGRjMzNiYmQ4NDg1OTdjNWYxNzc0M2E3NDRlMGI2IiwiaWF0IjoxNjk5Mjg0MDg5LCJuYmYiOjE2OTkyODQwODksImV4cCI6MTcwMTg3NjA4OSwic3ViIjoiODkzNDc4MSIsInNjb3BlcyI6W119.puK8jTnsoo_E_lYhBPNi3qL8HdCR5XfsRSu3Pnwm1FH91TYoEfoc0KZt6bFzVI7BTr5iKGJKZoYbSoP_iW3QcSZeAR6kI1NlO42jclGhocnG8lvZifpFZf1Yfugyj08QJu6zyb9XkGKS_Tp-64up24aNQn3082AQfuwX91r6Kr_xS9NhNTeDxhVfxUVs5_vbInJgpDUQoS1hOvcCS6aIivviFxo5lMEAjAuzSrAO6RjyMDqihYN0GNeJmZqIUanwtyPLPgeRzNZooDdH_XUbN98cyvqb-VvsgIADMadY-QhwAoSnGo_g9p8t-dBQ3kozkmWUvLciPRastHf4v2Xw0Q'
        self._access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBkODdmMWZiZDNjYTUzZDY2OGY3NmYxNGRjN2Y4ODkzNWRlNTI4N2Q5MTQ0Y2ZmMmYzNGRjMzNiYmQ4NDg1OTdjNWYxNzc0M2E3NDRlMGI2In0.eyJhdWQiOiI0NTY0ZTI2MDBkNjEzZDdjODgxNDg5ZmQ5OWQwY2ZhYSIsImp0aSI6IjBkODdmMWZiZDNjYTUzZDY2OGY3NmYxNGRjN2Y4ODkzNWRlNTI4N2Q5MTQ0Y2ZmMmYzNGRjMzNiYmQ4NDg1OTdjNWYxNzc0M2E3NDRlMGI2IiwiaWF0IjoxNjk5Mjg0MDg5LCJuYmYiOjE2OTkyODQwODksImV4cCI6MTcwMTg3NjA4OSwic3ViIjoiODkzNDc4MSIsInNjb3BlcyI6W119.puK8jTnsoo_E_lYhBPNi3qL8HdCR5XfsRSu3Pnwm1FH91TYoEfoc0KZt6bFzVI7BTr5iKGJKZoYbSoP_iW3QcSZeAR6kI1NlO42jclGhocnG8lvZifpFZf1Yfugyj08QJu6zyb9XkGKS_Tp-64up24aNQn3082AQfuwX91r6Kr_xS9NhNTeDxhVfxUVs5_vbInJgpDUQoS1hOvcCS6aIivviFxo5lMEAjAuzSrAO6RjyMDqihYN0GNeJmZqIUanwtyPLPgeRzNZooDdH_XUbN98cyvqb-VvsgIADMadY-QhwAoSnGo_g9p8t-dBQ3kozkmWUvLciPRastHf4v2Xw0Q'
        self._refresh_token = 'def502004ebd4266e51d5a32b77174ab897566733298fa2d47e6b5253f8b9b30520b0186290ab7f773ef3eb52dbd72644c2ddb02cabade46fa06eb4d08614eadf73e1de0878b6f362bec43856d12e44ed8d9bb6109febfe17753464d0f6911e723d398168d919ee3fa2f4a08fac394efb2a4838160541bec897547ac924b22d7f3c89caa2cd7249042d2d2627b9bc5e27fe52b0de53966958e596135401c80b55b85804192bca6d2451e9dbd97d22d3af2f07adee5b1ccf878e55848633ccaca1b1585e17b88f29c0bf5c68f73580db7e46d39af143ef30734b3f2aaffee48b5bd5e65572777f62b058d83b18a587ab027a57313ac05bf512199d90c92d1a4c455ee2a59cde9b3c8602147cb7a4eccea5267aa85d9aa123b8060d4c62f32244928779aef5c2904e06cd235397f7d124c26132c295797ecfe6aea303aa2c5bed0f99c0a81a79c531eb35c112c5991b08a4fedb1ee44f7205a6904d723683d252228ce281b9bbeed9fb61f602ea0219d3494f8140d37358a4f9a768a7492667fc086eae83fd69e25c5'
    def public_request(self, url):
        mal_access_token = 'def50200b18a4294067ecfad73bd8f86a6f2e0d3e183f5a8429e040a7f4f0d4a2e9950e46147e7e18527b6d0427b00873fd587c74b671c40b6af89c0981d5cda2d99793b3c3f2cb0b620277231ec43e179b530945b3ff3103cd113c3dc33dede4b09f7bc15e5214ec64438772f402b44b6fc36450e713f37bb2ea3ebbb2502fe0eea8aa6455af4f185c4e2d5afd34c8ed13ec685ecd688ef9082f9231ba5940add9a9f32e12206e24bcddc6bbea2b3812aee14e30cdbbb60d348ee95e9f6e7fed6b9ef690875bb34fc149999b46faf13df7c1f76a6940490bdc04abd47346be484e0874f252aeb5398e73a0d3253fca1c9ced89ab5c3bd3b783ae6c733ef5bbc179ded74fb4a733f18b5136c4a5fe13c0af8db4aaefbf9bff91202ef70198435fd6f66dac1d29540f9eceba2da4b245179bb23569e9c07f150054190125bff59b3126dd3ddb5457d61b5b60c876fa7c9eb0c3386e570369139d64ded459d0a1053da8e10b3bcb40218e64cffe71f01fb404b11e56cb97c1a06ba43a0bc4b8de369c523c5d3ac3bc3f2e4d3c808860fc7bae17717710b5d152a6544fac92dcbc842e81051d3d7f616ae502a2038bd18eaaaff59eea8fb6feb055451d2810f30 HTTP/1.1" 200'
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
