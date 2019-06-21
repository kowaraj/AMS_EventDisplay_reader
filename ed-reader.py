#!/bin/python3

import subprocess as subp
import shlex
import time 

DEST_PATH="/home/amslocal/src/ams-website__mount/files/EventDisplay/buffer/"
SCROT_CMD = "scrot ./ss_current.png -q10"

# read the screen and save to a file
while True:
    ts = time.gmtime()
    
    #buffer_name = time.strftime("buffer_%Y_%m_%d_%H_%M", ts)
    #file_name = time.strftime("ss_%S.png", ts)
    #buffer_path = DEST_PATH+'/'+buffer_name
    subp.Popen(['mkdir', '-p', DEST_PATH])
    file_path = DEST_PATH+'/ss_{0}.png'.format(ts)
    cmd = "{0} -e 'mv $f {1}'".format(SCROT_CMD, file_path)
    print(cmd)
    cmd_seq = shlex.split(cmd)
    print(cmd_seq)
    
    p = subp.Popen(cmd_seq)
    pout, perr = p.communicate()
    print(pout)
    print(perr)
    time.sleep(1)
    

# parse the file

# copy to the destination



