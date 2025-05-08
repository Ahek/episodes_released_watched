#run in spyder_env
import urllib
from bs4 import BeautifulSoup as BSoup
import requests
import re

class ListedAnime:
    def __init__(self, bot, node, list_status):
        self._id = node.get('id')
        self._title = node.get('title')
        self._main_picture = node.get('main_picture')
        self._large = node.get('large')
        self._status = list_status.get('status')
        self._score = list_status.get('score')
        self._num_episodes_watched = list_status.get('num_episodes_watched')
        self._is_rewatching = list_status.get('is_rewatching')
        self._updated_at = list_status.get('updated_at')
        self._bot = bot
    def details(self):
        r = self._bot.public_request(f'https://api.myanimelist.net/v2/anime/{self._id}?fields=id,title')
        return r.json()
    def nyaa_anime_query(self):
        url_parsed_title = urllib.parse.quote_plus(self._title)
        r = requests.get('https://nyaa.si/?page=rss', params = {'q':url_parsed_title})
        soup = BSoup(r.content, 'html.parser')
        
        title_tags = soup.find_all('title')
        
        torrenttitles = [tag.text for tag in title_tags]
        nrs = []
        for trt in torrenttitles:
            episode_nr = re.findall(r'(S|E)(\d+)', trt)
            try:
                if episode_nr:
                    if len(episode_nr) > 1:
                        nrs.append(episode_nr[1][1])
            except IndexError:
                pass
        if nrs:
            return max(int(x) for x in nrs)
        else:
            return -1