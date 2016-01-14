from bs4 import BeautifulSoup
from collections import namedtuple
import requests

"""This class extracts the urls and titles of a given youtube playlist"""

class PlayList:
	# name tuple to store outputs
    Video = namedtuple('Video', ['url', 'title'])
    
    def __init__(self, listurl):
        # get the html text
        self.__listurl = self.__makeUrl(listurl)
        htmldoc = requests.get(self.__listurl).text
        # parse the html
        soup = BeautifulSoup(htmldoc, 'html.parser')
        # get all the pl(aylist)-video-title-link(s):
        rawList = soup('a', {'class' : 'pl-video-title-link'})
        # there has to be at least 1 item in a playlist
        if len(rawList) < 1:
            raise ValueError('This might be either a private ' \
                              'or an empty playlist.')
        else:
            # list of the raw hrefs and their anchor texts
            self.__rawList = [(x.get('href'), x.contents[0].strip())
                              for x in rawList]


    @property
    def playlist(self):
		# return the playlist as a list of named tuples
        return [PlayList.Video._make([self.__getVideoURL(x[0])] + [x[1]])
                for x in self.__rawList]
        
    def __getVideoURL(self, text):
		# helper function split extract url and add prefix
        url = text.split('&')[0]   
        url = 'https://www.youtube.com' + url
        return url
    
    def __makeUrl(self, text):
		# url validation and clean up
        if text.find('playlist?list') != -1:
            return text
        elif text.find('watch?v=') * text.find('list=') > 1:
            return self.__getListUrlfromVideoLink(text)
        else:
            raise ValueError('Playlist ID not found in URL.')


    def __getListUrlfromVideoLink(self, text):
		# helper function as its name implies
        return r'''https://www.youtube.com/playlist?''' + \
               [x for x in text.split('&')
                if x.startswith('list=')][0]








