import serial
import json

RIG_SERIAL_CONFIG_FILE = './rig_serialconfig.json'

#read config file and send back a configured serial object
def get_serial():
    
    RIG_SERIAL_CONFIG_FILE = './rig_serialconfig.json'

    #read config json
    with open(RIG_SERIAL_CONFIG_FILE) as file:
        rig_conf_json = json.load(file)

    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port        =   rig_conf_json["port"],
        baudrate    =   int(rig_conf_json["baudrate"]),
        parity      =   rig_conf_json["parity"],
        stopbits    =   int(rig_conf_json["stopbits"]),
        bytesize    =   int(rig_conf_json["bytesize"]),
        timeout     =   float(rig_conf_json["timeout"])
    )

    #return the serial port
    return ser


#convert a string command to binary for sending to rig
def cmd_to_bin():
    return -1


#convert a binary command to string for output or saving
def bin_to_cmd():
    return -1


#send a command to the rig return the raw response
def send_rig_cmd():
    return -1

