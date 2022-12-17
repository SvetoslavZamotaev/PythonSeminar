from datetime import datetime as dt
from time import time


def ShowMeTime():
    date = dt.now().strftime('%H:%M:%S')
    return date
