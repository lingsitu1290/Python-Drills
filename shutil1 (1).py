# Script to move files from File A to File B that has been modified within the last 24 hours 

import shutil
import os
import time
import datetime


for name in os.listdir('C:\Users\Student\Desktop\A'):
    src = 'C:\Users\Student\Desktop\A\{}'.format(name)
    dst = 'C:\Users\Student\Desktop\B\{}'.format(name)

    #now = time.time()
    #print now
    time_diff = time.time() - (os.path.getmtime(src))

    _24hoursago = time.time() - (24 *60 *60)
    last_24_hrs = time.time() - _24hoursago 


    if time_diff < last_24_hrs:
        print 'File moved: {} '.format(src)
        print "last modified: {}".format(time.ctime(os.path.getmtime(src)))
        shutil.move(src, dst)
        
    
