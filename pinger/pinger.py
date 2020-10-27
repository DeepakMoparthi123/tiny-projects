import os
import time
hostname = "google.com" #example



import http.server
import socketserver
import datetime
from urllib.parse import urlparse
from urllib.parse import parse_qs
from scipy.stats import pearsonr

import time 
import random
import csv
from timeloop import Timeloop
from datetime import timedelta
import speedtest


def getNetSpeed():
    try:
        speedTestHelper = speedtest.Speedtest()
        speedTestHelper.get_best_server()

        #Check download speed 
        speedTestHelper.download()
        
        return speedTestHelper.results.dict()['download']/1000000, speedTestHelper.results.dict()['ping']
    except:
        #fetch result
        return 100000, 1000000


#seconds between each reading of sensor
tl = Timeloop()

@tl.job(interval=timedelta(seconds=60))
def pingg():
    speed, ping = getNetSpeed()
    file = open('pingerdata.csv','a')
    curr = datetime.datetime.now()
    file.write('\n'+str(curr.hour)+':'+str(curr.minute)+','+str(speed)+','+str(ping))
    file.close()
    

if __name__ == "__main__":
    tl.start(block=True)




