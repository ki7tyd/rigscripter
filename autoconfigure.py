def autoconfigure():
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