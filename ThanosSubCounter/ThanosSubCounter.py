import praw
import threading
import os
from requests import Session

clientid = "sr3m0IVZunKl0Q"
clientsecret = "hl2PC6GTe_kEMIobo8etOSuhIZg"

reddit = praw.Reddit(client_id=clientid,
                     client_secret=clientsecret,
                     redirect_uri='http://www.reddit.com',
                     user_agent='testscript by GSxHidden')

def printit():
    threading.Timer(5, printit).start()
    sub = reddit.subreddit('thanosdidnothingwrong').subscribers
    total = int(sub) / 2
    os.system('cls')
    print('Subscribers: ',sub)
    print('       Half: ',round(total))
printit()
