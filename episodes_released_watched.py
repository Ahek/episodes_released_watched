import requests
from bs4 import BeautifulSoup as bs

ggbaseurl = 'https://gogoanimehd.io/'

def find_mainbody(url):
    '''
    Uses beautifulsoup to find the main body. This main body stores the contents we want, namely the number of the last episode
    '''
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

def episodes_from_mainbody(main_body, tagname, my_classname):
    '''
    Find the right class that contains the episode number. Filtering by the tagname lessens the amount of classes it needed to search through
    '''
    soup_with_tagname = main_body.find_all(tagname)
    for tag in soup_with_tagname:
         if tag.get('ep_end'):
             last_episode =  tag.get('ep_end')
    return last_episode
