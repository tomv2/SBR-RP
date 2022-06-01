import can
import os

print('Initialising can bus...')

def initialiseCan():
    try:
        os.system("sudo /sbin/ip link set can0 up type can bitrate 500000") #check ECU bitrate is 500000
        print('Connected')
    except OSError:
        print('Cannot find PiCAN board')
        print('\nAttempting again...')
        os.system("sudo /sbin/ip link set can0 down")
        print('Will attempt again in 30 seconds')
        print('Have ran link down command')
        time.sleep(30)
        initialiseCan()

initialiseCan()
print('System ready')
bus = can.interface.Bus(channel='can0', bustype='socketcan')
notifier = can.Notifier(bus, [can.Printer()])
