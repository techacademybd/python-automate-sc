import datetime
import os
import time

'''Triggers the 8.py script in the given time
'''

# input time in hours, minutes and seconds...

checker = "15:14:30"
x = 0
while 1:
    date_time = datetime.datetime.now()
    d = date_time.strftime("%m-%d-%Y")
    t = date_time.strftime("%H:%M:%S")
    
    if x < 1000:
        x+=1    
        print(t)

    if t >= checker:
        print("Starting new script....")
        os.system("8.py 1")
        break

