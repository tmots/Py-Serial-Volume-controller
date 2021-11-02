##serial import
import serial
import serial.tools.list_ports
import time
##volume import
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


ports = list(serial.tools.list_ports.comports())
for p in ports:
    ##print (str(p)[:4])
    if str(p)[7:14] == "Arduino" :
        conport = str(p)[:4]

###

def vol_fnc(volnum):
    numv = float(1/255*float(volnum))
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(numv, None)

###
ser = serial.Serial(conport, 9600)
##time.sleep(0.5)

def read_ser():
    if ser.readable():
        res = ser.readline()
        volnum=res.decode()[:len(res)-1]
        if int(volnum) < 20 :
            volnum = 0
        if int(volnum) > 235 :
            volnum = 255
        vol_fnc(volnum)
        ##print(volnum)

while True:
    read_ser()


