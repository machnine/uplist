from bs4 import BeautifulSoup
import requests
"""this class extracts the url and index of a given youtube playlist"""

class PlayList:
    
    def __init__(self, listurl):
        # get the html text
        htmldoc = requests.get(listurl).text
        # parse the html
        soup = BeautifulSoup(htmldoc, 'html.parser')
        # put all links begins with '/watch?' into a list
        rawList = set(x.get('href') for x in soup('a')
                      if x.get('href').startswith('/watch?'))
        """
            check if this is likely to be a playlist page all
            videos urls and the url of the list itself appears
            twice in the html, 4 = a list with at least 1 video
        """
        if len(rawList) > 4:
            self.__rawList = rawList
        else:
            raise ValueError

        
    def __urlSplit(self, text):
        """
           youtube playlist url has 3 parts:
             main url: /watch?v=xxxxxxxxxxx
             index: index=xx
             listid: list=xxxxxxxxxxxxxxxxxxxxx
             the positions of index and listid swap randomly
           int(x[6:])   ->   6 = len('index=')
        """
        if 'index=' in text:
            splitText = text.split('&')
            return ['https://www.youtube.com' + splitText[0]]  + \
                   [int(x[6:]) for x in splitText
                                  if x.find('index=') != -1]
        else:
            return None

    @property
    def urls(self):
        # fill a list same length as __rawList with None
        temp = [None for x in self.__rawList]
        for x in self.__rawList:
            split = self.__urlSplit(x)
            if split:
                # update the list according to playlist order
                index = split[1] - 1
                temp[index]  = split
        # remove any None in the list and return
        return [x[0] for x in temp if x]
























