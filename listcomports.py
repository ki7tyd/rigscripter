import serial
from serial.tools import list_ports

x = list(list_ports.comports())
for port in x:
    print("Checking port: " + str(port))
    print("Description: " + port.description)
    print("Device name: " + port.device)
    print("Hardware ID: " + port.hwid)
    print("Interface: " + str(port.interface))
    print("Location: " + str(port.location))
    print("Manufacturer: " + port.manufacturer) 
    print("Name: " + str(port.name))
    print("PID: " + str(port.pid))
    print("Product: " + str(port.product))
    print("Serial number: " + port.serial_number)
    print("VID: " + str(port.vid))

    print("Trying " + port.device)

    ser = serial.Serial(
        port=f'{port.device}',
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.EIGHTBITS,
        timeout=0.1
    )

    commandarray = ['ID']

    i = 0
    for cmd in commandarray:
        i += 1
        cmd = f'{cmd};'
        cmd = bytes(cmd, encoding="ascii")
        print(str(i) + ": " + str(cmd))
        
        #write cmd to serial
        ser.write(cmd)
            
        #read response
        out = ser.read(28)

        if(out == b'?;'):
            print("Didn't understand that one...")

        elif(out == b''):
            print("Command worked. No response")

        else:
            print("Response: " + str(out) + ": " + str(len(out)))


    #close the connection
    ser.close()