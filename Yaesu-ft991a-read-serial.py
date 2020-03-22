#FT991a is on COM3
# https://pyserial.readthedocs.io/en/latest/shortintro.html
# https://pythonhosted.org/pyserial/index.html
# http://www.varesano.net/blog/fabio/serial%20rs232%20connections%20python
# https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=102&encProdID=D24F60F33816ED8BE5568D7E2B5E2131
# https://www.yaesu.com/downloadFile.cfm?FileID=10604&FileCatID=158&FileName=FT%2D991%5FCAT%5FOM%5FENG%5F1612%2DD0.pdf&FileContentType=application%2Fpdf
import json
import serial
import memorymanager
import logging
import rsutils #project import

#get logifle name from global config and start logging
logging.basicConfig(filename=rsutils.read_rs_config_file()["logfile"], level=logging.DEBUG)

#commandarray = 	['FB147960000', 'FA146960000', 'FB']
commandarray = ['MT001']

i = 0
for cmd in commandarray:
	i += 1
	cmd = rsutils.cmdstr_to_cmdbin(cmd)
	
	logging.debug("Sending " + str(i) + ": " + str(cmd))
	out = rsutils.send_rig_cmd(cmd)
	
	logging.debug("variable out is type: " + str(type(out)))
	strout = rsutils.cmdbin_to_cmdstr(out)

	#test response parser
	logging.debug("Response: " + strout + " " + str(len(out)) + "chars")
	print('Response parser returned: ' + str(memorymanager.parse(cmd, strout)))


#close the connection
#ser.close()

