related = []


base_link = 'http://gdata.youtube.com/feeds/api/videos?q='

def get_page(song):
    song = song.replace(' ', '+')
    url = base_link + song + '+karaoke'
    html = urllib2.urlopen(url).read()
def get_links(page):
    vid_id = 