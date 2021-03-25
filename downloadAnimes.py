import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import wget
import requests   



def download(url, file_name): 
    headers = {'User-Agent': 'Mozilla', 'Referer': 'https://animesvision.biz'}

    r = requests.get(url, allow_redirects=True, headers=headers)
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    return file_name


def getEpisodeList(url):
    site = url # Removes the /n
    print(site)

    req = Request(site, headers={'User-Agent': 'Mozilla'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    episode_list = soup.findAll("div", {"class": "sli-btn"})
    return episode_list

def getEpisodeLink(episode):
    on_click_value = episode.find_all('a')[1]['onclick']
    url_download = on_click_value.split('\'')[1]

    req = Request(url_download, headers={'User-Agent': 'Mozilla'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')

    item_to_download = soup.find_all('a', attrs={'style':'margin: 5px;'})[0]['href']
    return item_to_download        

# def downloadAll(url):
#     site = url # Removes the /n
#     print(site)

#     req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
#     webpage = urlopen(req).read()

#     soup = BeautifulSoup(webpage, 'html.parser')
#     episode_list = soup.findAll("div", {"class": "sli-btn"})

#     for episode in episode_list:
#         on_click_value = episode.find_all('a')[1]['onclick']
#         url_download = on_click_value.split('\'')[1]

#         req = Request(url_download, headers={'User-Agent': 'Mozilla/5.0'})
#         webpage = urlopen(req).read()

#         soup = BeautifulSoup(webpage, 'html.parser')

#         item_to_download = soup.find_all('a', attrs={'style':'margin: 5px;'})[0]['href']

#         print(item_to_download.split('/')[-1])

#         finished_download_item = download(item_to_download, url('/')[-1] + '_' + item_to_download.split('/')[-1])
        
#         print(item_to_download)