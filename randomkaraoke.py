from bs4 import BeautifulSoup
import urllib, urllib2
related = []




def get_song(song):
    base_link = 'http://gdata.youtube.com/feeds/api/videos?q='
    song = song.replace(' ', '+')
    url = base_link + song + '+karaoke'
    html = urllib2.urlopen(url).read()
    html = html[html.find('entry'):]
    html = html[html.find('link rel='):]
    page = html.split("'")[5].split('&')[0][31:]
    
    return page
    
def get_related_song(page):
    html = urllib2.urlopen(page).read()
    soup = BeautifulSoup(html)
    link = str(soup.select(".video-list-item")[5])
    link = link[link.find('href'):].split('"')[1]
    return link
    
    