import pandas as pd
import Bot
from episodes_released_watched import episodes_from_mainbody, find_mainbody

#You might need to change this url if they switched their domain
ggbaseurl = 'https://gogoanimehd.io/'

def mal_df():
    bot = Bot.MyBot()
    df_watching_raw = pd.DataFrame(bot.get_my_list()['data'])
    
    node = pd.json_normalize(df_watching_raw['node'])
    list_status = pd.json_normalize(df_watching_raw['list_status'])
    df_watching = pd.concat([node, list_status], axis = 1)
    return df_watching

def eps_released(df_watching, title_url):
    df_watching['url'] = df_watching['title'].apply(lambda x: title_url[x] if x in title_url else pd.NA)
    df_watching['num_released_episodes'] = df_watching['url'].apply(lambda x: int(episodes_from_mainbody(find_mainbody(x), 'a', 'active')) if pd.notna(x) else 0)
    df_watching['not_watched_episodes'] =  df_watching['num_released_episodes'] - df_watching['num_episodes_watched']
    df_watching = df_watching.sort_values(['not_watched_episodes', 'num_released_episodes'], ascending = False).reset_index(drop = True)
    return df_watching

#Change this into the shows you watch. The key is the title on MyAnimeList, the value is the link to the show on gogoanime
title_url = {
    'Kage no Jitsuryokusha ni Naritakute! 2nd Season':'https://gogoanimehd.io/category/kage-no-jitsuryokusha-ni-naritakute-2nd-season',
    'One Piece':'https://gogoanimehd.io/category/one-piece',
    'Sousou no Frieren':'https://gogoanimehd.io/category/sousou-no-frieren'
    }

df_watching = eps_released(mal_df(), title_url)
