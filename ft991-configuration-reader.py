#yaesu ft991 configuration reader

#FT991a is on COM3
# https://pyserial.readthedocs.io/en/latest/shortintro.html
# https://pythonhosted.org/pyserial/index.html
# http://www.varesano.net/blog/fabio/serial%20rs232%20connections%20python
# https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=102&encProdID=D24F60F33816ED8BE5568D7E2B5E2131
# https://www.yaesu.com/downloadFile.cfm?FileID=10604&FileCatID=158&FileName=FT%2D991%5FCAT%5FOM%5FENG%5F1612%2DD0.pdf&FileContentType=application%2Fpdf

import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='COM3',
	baudrate=4800,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.EIGHTBITS,
    timeout=0.1
)

#read menu configurations
#range 001 - 153

NUM_CMDS = 153
MENU_CMD = 'EX'

i = 0
while i < NUM_CMDS:
    i += 1
    cmdnum = ('{0:03d}'.format(i))
    cmd = MENU_CMD + cmdnum + ";"
    cmd = bytes(cmd, encoding="ascii")
    #print(cmd)
    ser.write(cmd)
    out = ser.read(28)
    print(str(out))

ser.close()