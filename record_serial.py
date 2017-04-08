import argparse
import serial
import csv
import sys
import os
import datetime


def preprocess_args():

    parser = argparse.ArgumentParser(description='Stream serial input to a csv file')
    parser.add_argument('-fname', type=str,
        help='insert a file to save output to that ends in .csv')
    parser.add_argument('-timelim', type=int,
        help='time in seconds to record data. default is 2 minutes')
    parser.add_argument('-serial_port', type=str,
        help='path to serial port. Default is Torben\'s')
    parser.add_argument('-paradigm', type=str,
        help='string to csv file with paradigm for labeling and timeing recordings')
    parser.add_argument('-verbose', type=bool,
        help='talk through steps')

    return parser.parse_args()


class serial_processor:
    """
    Class that runs a recording paradigm
    """

    def __init__(self):
        self.fnames = {'default':os.path.join('.','output.csv')}
        self.end_times = {}
        self.serial_port=os.path.join('dev','cu.usbmodem1411')
        self.verbose=False


    def assign_args(self,start_time):

        args = preprocess_args()

        if args.verbose:
            self.verbose=True

        if args.fname:
            self.fnames = {'default':os.path.join('.',args.fname+'.csv')}
            if self.verbose:
                print 'saving output to ' + str(args.fname)
        else:
            if self.verbose:
                print 'no file name given. Saving as output.csv'

        if args.timelim:
            self.end_times = {'default':start_time + datetime.timedelta(seconds=args.timelim)}
            if self.verbose:
                print 'Recording for ' + str(args.timelim) + ' seconds.'
        else:
            self.end_times = {'default':start_time + datetime.timedelta(seconds=60)}
            if self.verbose:
                print 'No time limit given. Recording for 1 minute.'
        if args.serial_port:
            self.serial_port = args.serial_port
            if verbose:
                print 'using custom serial port: ' + str(self.serial_port)
        else:
            if self.verbose:
                print 'using default serial port: ' + self.serial_port


    def simple_record(end_time,serial_port):
        """
        records input and returns it as an array. no stream.
        """

        output_array = []
        time_array = []
        this_time=datetime.datetime.now()
        if self.verbose:
            print 'begining run at ' + str(this_time)

        while this_time<end_time:
            try:
                ser = serial.Serial(self.serial_port,9600, timeout=1)
                # Read a line and convert it from b'xxx\r\n' to xxx
                line = ser.readline().decode('utf-8')
                if line:  # If it isn't a blank line
                    output_array.append(line)
            except serial.serialutil.SerialException:
                print 'ERROR: could not access serial port: ' + str(self.serial_port)
                break

            this_time = datetime.datetime.now()
            time_array.append(this_time)

        return output_array,time_array


    def write_results(self, data_array, outfile=None, datetime_array=None, label_array=None):
        """
        writes data, recording times and labels (outputs from simple_record) to a csv file.

        """

        if not datetime_array:
            datetime_array = ['no time' for i in data_array]
        if not label_array:
            label_array = ['unlabeled' for i in data_array]

        if not outfile:
            outfile = self.fnames['default']
            if self.verbose:
                print 'saving to default file path: ' + self.fnames['default']
        f = open(outfile, 'w+')
        for e,line in enumerate(output_array):
            labeled_line = line.extend(datetime_array[e],label_array[e])
            f.write(line)
        f.close()


    def stream_input(self, start_time, endtime_key='default', outfile_key='default'):

        """
        stream input to a csv file.
        """

        this_time=start_time
        end_time = self.end_times[endtime_key]
        outfile = self.fnames[endtime_key]

        if self.verbose:
            print 'begining run at ' + str(start_time)
        f = open(outfile, 'w+')

        while this_time<end_time:

            ser = serial.Serial('/dev/cu.usbmodem1411',9600, timeout=1)
            # Read a line and convert it from b'xxx\r\n' to xxx
            line = ser.readline().decode('utf-8')
            if line:  # If it isn't a blank line
                f.write(line)
            # except serial.serialutil.SerialException:
            #     print 'ERROR: could not access serial port: ' + str(self.serial_port)
            #     break

            this_time = datetime.datetime.now()

        f.close()


def main():

    start_time = datetime.datetime.now()
    my_processor = serial_processor()
    my_processor.assign_args(start_time)

    raw_input("Press Enter to begin recording")

    my_processor.stream_input(start_time)


if __name__=='__main__':
    main()


# might need for some reason
    #

