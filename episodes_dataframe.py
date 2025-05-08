import episodes_from_mal
from Bot import MyBot
import pandas as pd

bot = MyBot()
watchlist = bot.get_my_list('watching')

anime_tracking_list = []

for anime in watchlist['data']:
    LtA = episodes_from_mal.ListedAnime(bot, anime['node'], anime['list_status'])
    episodes_watched = LtA._num_episodes_watched
    episodes_released = LtA.nyaa_anime_query()
    anime_tracking_list.append([LtA._title, episodes_watched, episodes_released])

anime_tracker_df = pd.DataFrame(anime_tracking_list, 
    columns = ['anime_name', 'episodes_watched', 'episodes_unwatched'])