import serial
import json
import logging

RS_CONFIG_FILE = './rs_config.json'

#read global config file
def read_rs_config_file():
    #read config json
    with open(RS_CONFIG_FILE) as file:
        rs_config = json.load(file)
    return rs_config


#read config file and send back a configured serial object
def get_serial():
    
    #RIG_SERIAL_CONFIG_FILE = './rig_serialconfig.json'
    config = read_rs_config_file()
    RIG_SERIAL_CONFIG_FILE = config["rig_serial_config_file"]

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


#Format a simple string and convert command to binary eg add ; at the end for sending to rig
def cmdstr_to_cmdbin(cmd):
    #check if it's a string
    if type(cmd) == str:
        #check that the last character is a ;, if not add one
        if cmd[-1] != ';':
            cmd = cmd + ';'
        #convert to binary ascii
        cmd = bytes(cmd, encoding="ascii")
        return cmd

    else:
        return "Not a string"


#convert a binary command to string for output or saving
def cmdbin_to_cmdstr(cmd):
    #check if it's binary
    if type(cmd) == bytes:
        cmd = cmd.decode('ascii')
        return cmd
    else:
        return "Not binary"


#send a command to the rig return the raw response
def send_rig_cmd(cmd):
    ser = get_serial()
    if type(cmd) == str:
        cmd = cmdstr_to_cmdbin()
        send_rig_cmd(cmd)
    elif type(cmd) == bytes:
        ser.write(cmd)
    else:
        return "cmd wasn't a a string or bytes."
    out = ser.readline()
    ser.close()
    return out


