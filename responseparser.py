#parse responses from the radio
#Yaesu FT991A set for now
#CAT commands manual: https://www.yaesu.com/downloadFile.cfm?FileID=10604&FileCatID=158&FileName=FT%2D991%5FCAT%5FOM%5FENG%5F1612%2DD0.pdf&FileContentType=application%2Fpdf

returnstr = ''

def parse(resp):
    cmdstring = resp[0:2]
    #return(f'Parsed this: {resp}, command is this: {cmdstring}')

    if cmdstring == '':
        return('Command was empty')
    
    elif cmdstring == 'MR':
        return(memory_channel_read(cmdstring, resp))
    
    elif cmdstring =='MT':
        return(memory_channel_read(cmdstring, resp))

    else:
        return('Something else happened. No other conditions met in parse()')



def memory_channel_read(c, r):
    #Parse the memory read response from MR and MT commands
    
    d = dict()
    d['cmdletters'] =                   r[0:2]      #2 letter cmd
    d['channel'] =                      r[2:5]      #P1 Memory channel
    d['vfoafreq'] =                     r[5:14]     #P2 VFO a frequency
    d['clarifier_directon_offset'] =    r[14:19]    #P3 Clarifier direction + shift/- shift, clarifier offset 0000 - 9999Hz
    d['rx_clar_on_off'] =               r[19:20]    #P4 RX clarifier on/off 0 = OFF/1 = ON
    d['tx_clar_on_off'] =               r[20:21]    #P5 TX clarifier on/off 0 = OFF/1 = ON
    d['mode'] =                         r[21:22]    #P6 Mode 1=LSB, 2=USB, 3=CW, 4=FM, 5=AM, 6=RTTY-LSB, 7=CW-R, 8=DATA-LSB, 9=RTTY-USB, A=DATA-FM, B=FM-N, C=DATA-USB, D=AM-N, E=C4FM
    d['vfo_mem'] =                      r[22:23]    #P7 0=VFO/1=Memory
    d['coding'] =                       r[23:24]    #P8 0=CTCSS_OFF, 1=CTCSS ENC/DEC, 2=CTCSS ENC, 3=DCS ENC/DEC, 4=DCS ENC, 
    d['fixed_1'] =                      r[24:26]    #P9 00 (Fixed)
    d['shift'] =                        r[26:27]    #P10 0=simplex, 1=plus_shift, 2=minus shift
    
    if c == 'MT':
        d['fixed_2'] =                  r[27:28]    #P11 0 (Fixed)
        d['tag'] =                      r[28:40]    #P12 Tag

    #return to the main parser function
    return(d)
