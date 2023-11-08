import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

ggbaseurl = 'https://gogoanimehd.io/'

r_gogoanime = requests.get(f"{ggbaseurl}/category/one-piece")
r_myanimelist = pd.read_html("https://myanimelist.net/animelist/Wwwwat?status=1")[0]

def find_mainbody(url):
    r = requests.get(url, timeout = 5)
    if r.status_code != 200:
        raise Exception(f'{r.status_code}:{r.reason}\n{r.url}')
    soup = bs(r.text, features = 'lxml')
    content_left = soup.find('body').find_all('div')[1].find('div').find('div').find_all('section')[1].find('section')
    main_body = content_left.find('div')
    if not main_body:
        print("Main body not found")
    else:
        print("Main body found")
    return main_body

def episodes_from_mainbody(main_body, tagname, my_classname):#main_body, 'a', 'active
    soup_with_tagname = main_body.find_all(tagname)
    for tag in soup_with_tagname:
         if tag.get('ep_end'):
             laatste_episode =  tag.get('ep_end')
    return laatste_episode
    raise KeyError("No episode end found")
    
main_body = find_mainbody(f"{ggbaseurl}/category/one-piece")
last_episode = episodes_from_mainbody(main_body, 'a', 'active')

def get_table(url):
    r = requests.get(url)
    soup = bs(r.text, features = 'lxml')
    str_table = soup.find('table')['data-items']
    df_table = pd.DataFrame(json.loads(str_table))
    return df_table

df_watching = get_table("https://myanimelist.net/animelist/Wwwwat?status=1")[['anime_title', 'anime_num_episodes', 'num_watched_episodes']]
df_plan_to_watch = get_table("https://myanimelist.net/animelist/Wwwwat?status=6")[['anime_title', 'anime_num_episodes', 'num_watched_episodes']]
df = pd.concat([df_watching, df_plan_to_watch], axis = 0)
df['anime_num_episodes'] = df['anime_num_episodes'].apply(lambda x: x if x > 0 else pd.NA)
    
title_url = {'One Piece':f'{ggbaseurl}/category/one-piece',
             'Mushoku Tensei II: Isekai Ittara Honki Dasu':f'{ggbaseurl}/category/mushoku-tensei-ii-isekai-ittara-honki-dasu',
             'Shingeki no Kyojin: The Final Season - Kanketsu-hen':f'{ggbaseurl}/category/shingeki-no-kyojin-the-final-season-kanketsu-hen',
             'Kage no Jitsuryokusha ni Naritakute! 2nd Season':f'{ggbaseurl}/category/kage-no-jitsuryokusha-ni-naritakute-2nd-season',
             'Kanojo, Okarishimasu 3rd Season':f'{ggbaseurl}/category/kanojo-okarishimasu-3rd-season',
             'Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou':f'{ggbaseurl}/category/jidou-hanbaiki-ni-umarekawatta-ore-wa-meikyuu-wo-samayou',
             'Zom 100: Zombie ni Naru made ni Shitai 100 no Koto':f'{ggbaseurl}/category/zom-100-zombie-ni-naru-made-ni-shitai-100-no-koto',
             'Shiguang Dailiren II':f'{ggbaseurl}/category/shiguang-dailiren-ii'
             }
df['url'] = df['anime_title'].apply(lambda x: title_url[x] if x in title_url else pd.NA)
df['num_released_episodes'] = df['url'].apply(lambda x: int(episodes_from_mainbody(find_mainbody(x), 'a', 'active')) if pd.notna(x) else 0)
df['not_watched_episodes'] =  df['num_released_episodes'] - df['num_watched_episodes']
df['not_watched_episodes'] = df.apply(lambda x: x['not_watched_episodes']//3 if x['anime_title'] == 'One Piece' else x['not_watched_episodes'], axis = 1)

df = df.sort_values(['not_watched_episodes', 'num_released_episodes', 'anime_num_episodes'], ascending = False).reset_index(drop = True)
# def peek(soup, length = 100):
#     soup_parts = str(soup).split('\n')
#     i = 0
#     soup_string = soup_parts[i]
#     while len(soup_string) < length:
#         i += 1
#         soup_string = soup_string + '\n' + soup_parts[i]
#     print(str(soup)[:length])