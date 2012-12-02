from bs4 import BeautifulSoup
import urllib, urllib2
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
    page = html.split("'")[5].split('&')[0][31:]
    return page
    
"""def get_related_song(page):
    html = urllib2.urlopen(page).read()
    soup = BeautifulSoup(html)
    link = str(soup.select(".video-list-item")[4])
    link = link[link.find('href='):].split('>')[0][15:-1]
    return link"""
    
def get_related_song(page):
    html = urllib2.urlopen(page).read()
    soup = BeautifulSoup(html)
    try:
        link = str(soup.select(".video-list-item")[random.randint(0, 11)])
    except:
        return 'Call me maybe'
    link = link[link.find('class="title"'):]
    try:
        link = link[link.find('title'):].split("=")[2].split(" -")[1].strip('"').replace("'", "")[:25]
    except:
        return 'Call me maybe'
    return link
    
    