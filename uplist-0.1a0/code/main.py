from UPList import PlayList

def Main():
    while(True):
        url = input('Enter the Youtube playlist URL: ')
        if len(url) == 0 or url =='quit':
            break
        p = PlayList(url)
        print('-' * 45)
        for i, x in enumerate(p.urls):
            print(i+1, x)
        print('-' * 45)


if __name__ == '__main__':
    Main()
