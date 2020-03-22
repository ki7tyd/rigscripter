import serial
import argparse
from datetime import datetime
import os
import memorymanager ## project import

#strftime: https://strftime.org/

MEM_MAX = 117
MEM_SAVE_FOLDER = './rigmemdumps'

#API
#add memory
#rs.py mem 
#   -m, --memslot 2         eg. 2
#   -f, --freq 146960000    eg. 146960000 
#   -c, --clar_offset       eg. +500 
#   -rc, --rxclar           On/Off
#   -tc, --txclar           On/Off 
#   -m, --mode              eg. FM
#   -t, --tone              eg. ctcss-codec
#   -s, --shift             eg. minus
#   -tag, --tag             eg. FaveRepeater


#dump all memory to file
def radio_memdump():
    #connect to serial port
    print('Connecting to port')
    ser = serial.Serial(
	port='COM3',
	baudrate=4800,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.EIGHTBITS,
    timeout=0.1
    )

    #open a file for appending
    if not os.path.exists(MEM_SAVE_FOLDER):
        os.makedirs(MEM_SAVE_FOLDER)
    filename = str(datetime.now().strftime("%m-%d-%Y_%H-%M-%S-%f"))
    f = open(f'{MEM_SAVE_FOLDER}/{filename}', 'ab')
    print(f'Writing to {filename}')

    MDM_CMD = 'MT'
    print('Fetching memories...')
    i = 0
    while i < MEM_MAX:
        i += 1
        memnum = ('{0:03d}'.format(i))
        cmd = MDM_CMD + memnum + ";"
        cmd = bytes(cmd, encoding="ascii")
        #print(str(cmd))
        ser.write(cmd)
        out = ser.readline()
        if out != b'?;':
            #write to file
            f.write(out)
            print(out)

    print('All done. Closing port and file')
    f.close()
    ser.close()

#first thing dump all current memories to a save file
radio_memdump()