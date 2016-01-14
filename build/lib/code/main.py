from uplist import PlayList

def Main():
    while(True):
        url = input('Enter the Youtube playlist URL: ')
        if len(url) == 0 or url =='quit':
            break
        pl = PlayList(url)
        print('-' * 45)
        for i, x in enumerate(pl.videos):
            print('URL: %s - %s.%s'%(x.url, i+1, x.title))
        print('-' * 45)


if __name__ == '__main__':
    Main()
