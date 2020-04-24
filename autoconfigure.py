import json
import serial

#config file TODO read this out of a master config file
RIG_SERIAL_CONFIG_FILE = './rig_serialconfig.json'
    
#adding a comment

def autoconfigure():
    
    #detect proper configuration TODO
    baudrates = [2400, 4800, 7200, 9600, 14400, 19200, 31250, 38400, 56000, 115200, 128000]
    parities = ['PARITY_NONE', 'PARITY_ODD', 'PARITY_EVEN']
    stopbits = ['STOPBITS_ONE', 'STOPBITS_ONE_POINT_FIVE', 'STOPBITS_TWO']
    bytesizes = ['FIVEBITS', 'SIXBITS', 'SEVENBITS', 'EIGHTBITS']

    i = 0
    for baudrate in baudrates:
        for parity in parities:
            for stopbit in stopbits:
                for bytesize in bytesizes:
                    i += 1
                    print(str(i))
                    print(f'Baudrate: {str(baudrate)}')
                    print(f'Parity: {parity}')
                    print(f'Stopbits: {stopbit}')
                    print(f'Bytesize: {bytesize}')
                    print('\n')
    
#build serial config dictionary
serial_config_dict = dict()
serial_config_dict["port"] = "COM3"
serial_config_dict["baudrate"] = "4800"
serial_config_dict["parity"] = "N"
serial_config_dict["stopbits"] = "2"
serial_config_dict["bytesize"] = "8"
serial_config_dict["timeout"] = "0.1"


#write config to serial config file
print("Writing to config file: {}".format(RIG_SERIAL_CONFIG_FILE))
with open(RIG_SERIAL_CONFIG_FILE, 'w') as f:
    json.dump(serial_config_dict, f)