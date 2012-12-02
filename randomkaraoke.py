from bs4 import BeautifulSoup
import urllib, urllib2
related = []



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
    
def get_related_song(page):
    html = urllib2.urlopen(page).read()
    soup = BeautifulSoup(html)
    return soup.select(".video-list-item")
    link = str(soup.select(".video-list-item")[5])
    print link
    link = link[link.find('title'):].split('"')[1]
    return link
    
def get_related_song2(page):
    html = urllib2.urlopen(page).read()
    soup = BeautifulSoup(html)
    link = str(soup.select(".video-list-item")[5])
    link = link[link.find('class="title"'):]

    link = link[link.find('title'):].split("=")[2].split(" -")[0].strip('"')
    return link
    
    