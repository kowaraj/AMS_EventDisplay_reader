#!/bin/python3

import subprocess as subp
import shlex
import time 

ROOT_PATH="/home/amslocal/src/ams-website__mount/files/EventDisplay"
DEST_PATH=ROOT_PATH + '/buffer'
SCROT_CMD = "scrot ./ss_current.png"

# read the configuration
import configparser as cfgp
config = cfgp.ConfigParser()
config.read(ROOT_PATH+'/config.ini')
if 'DEFAULT' in config:
    scrot_key_q = int(config['DEFAULT']['ScreenshotQuality'])
else:
    scrot_key_q = 10
print("CONFIG: q = " + str(scrot_key_q))



# read the screen and save to a file
while True:
    ts = int(time.time()) #round(time.time(),0) #time.gmtime()
    print("ts = ", ts)
    
    subp.Popen(['mkdir', '-p', DEST_PATH])
    file_path = DEST_PATH+'/ss_{0}.png'.format(ts)
    cmd = "{0} -q{2} -e 'mv $f {1}'".format(SCROT_CMD, file_path, scrot_key_q)
    cmd_seq = shlex.split(cmd)
    # print(cmd_seq)

    p = subp.Popen(cmd_seq)
    pout, perr = p.communicate()
    # print(pout)
    # print(perr)
    time.sleep(1)
    

# parse the file

# copy to the destination



