from bs4 import BeautifulSoup
import urllib2

#gets list of urls from dropbox url
def get_imagelinks_from_dropbox(url):
    links = []
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response)
    section = soup.find('ol', id='gallery-view-media')
    lis = section.find_all('a')
    for li in lis:
        links.append(li['href'][:-5])
    return links
