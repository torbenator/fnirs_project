
import serial
import csv
import sys

#from time import gmtime, strftime
#resultFile=open('MyData.csv','wb')
my_serial_port = '/dev/cu.usbmodem1411'

output_fname = '/Users/Torben/Code/fnirs_project/output.csv'

if __name__=='__main__':
    f = open('output.csv', 'w+')
    while True:
        ser = serial.Serial(my_serial_port,9600, timeout=1)
        # Read a line and convert it from b'xxx\r\n' to xxx
        line = ser.readline().decode('utf-8')
        if line:  # If it isn't a blank line
            f.write(line)
    f.close()