from bs4 import BeautifulSoup
import urllib2, urllib
import random

base_link = 'http://gdata.youtube.com/feeds/api/videos?q='

def get_song(song, original=False):
    song = song.replace(' ', '+')
    if original:
        url = base_link + song
    else:
        url = base_link + song + '+karaoke'
    html = urllib2.urlopen(url).read()
    html = html[html.find('entry'):]
    html = html[html.find('link rel='):]
    try:
        page = html.split("'")[5].split('&')[0][31:]
    except:
        page = 'sTE9s43rdT8'
    return page

def get_related_song(page):
    html = urllib2.urlopen(page).read()
    soup = BeautifulSoup(html)
    related_vids = soup.find(id="watch-related").find_all('a', 'related-video')
    try:
        link = related_vids[random.randint(1, 11)]
    except:
        return 'call me maybe'
    song = str(link.find('span', 'title')).split('title=')[1]
    if len(song) > 20:
        song = song[:21]
    if 'karaoke' in song.lower():
        index = song.lower().find('karaoke')
        song = song[:index] + song[index+7:]
    #song = 'to make you feel my love'
    return song
    