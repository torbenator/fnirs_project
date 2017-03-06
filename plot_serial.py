#import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib.pyplot as plt

serial_file = '/Users/Torben/Code/fnirs_project/output.csv'
out_path = '/Users/Torben/Code/fnirs_project/output_figure.png'


def make_plot(data, out_path=None):
    fig = plt.figure(figsize=(5,5))
    ax1 = plt.subplot(111)
    #ax1.plot(data[:,0],'r',label='red')
    #ax1.plot(data[:,1],'k',label='infared')
    ax1.plot(data[:,2],'b',label='ratio')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.set_ylabel('A0 Output')
    ax1.set_xlabel('Sample Number')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    #fig.legend()

    if out_path:
        fig.savefig(out_path)
    return fig

def load_data(serial_file):
    my_data = []
    with open(serial_file,'rb') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            temp_line = [i for i in line]
            my_data.append([int(temp_line[0]),int(temp_line[1]),float(temp_line[0])])
    return my_data


if __name__=='__main__':
    my_data = load_data(serial_file);
    array_data = np.array(my_data)
    fig = make_plot(array_data,out_path)
