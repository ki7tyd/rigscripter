#FT991a is on COM3
# https://pyserial.readthedocs.io/en/latest/shortintro.html
# https://pythonhosted.org/pyserial/index.html
# http://www.varesano.net/blog/fabio/serial%20rs232%20connections%20python
# https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=102&encProdID=D24F60F33816ED8BE5568D7E2B5E2131
# https://www.yaesu.com/downloadFile.cfm?FileID=10604&FileCatID=158&FileName=FT%2D991%5FCAT%5FOM%5FENG%5F1612%2DD0.pdf&FileContentType=application%2Fpdf

import serial
import responseparser

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='COM3',
	baudrate=4800,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.EIGHTBITS,
    timeout=0.1
)

#commandarray = 	['FB147960000', 'FA146960000', 'FB']
commandarray = ['MT001']

i = 0
for cmd in commandarray:
	i += 1
	cmd = f'{cmd};'
	cmd = bytes(cmd, encoding="ascii")
	print("Sending " + str(i) + ": " + str(cmd))
	
	#write cmd to serial
	ser.write(cmd)
		
	#read response
	#out = ser.read(100) #this works doesn't depend on EOL characters
	out = ser.readline()
	out = out.decode('ascii')

	#test response parser
	print('Response parser returned: ' + str(responseparser.parse(out)))

	print("Response: " + str(out) + ": " + str(len(out)) + "chars")


#close the connection
ser.close()

