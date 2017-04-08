#import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib.pyplot as plt

serial_file = './hold_breath.csv'
out_path = './output_figure.png'


def make_plot(data, out_path=None):
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(311)
    ax1.plot(data[:,0],'r',label='red')

    ax2 = fig.add_subplot(312)
    ax2.plot(data[:,1],'k',label='infared')

    ax3 = fig.add_subplot(313)
    ax3.plot(data[:,2],'b',label='ratio')

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
            my_data.append([int(temp_line[0]),int(temp_line[1]),float(temp_line[2])])
    return my_data


if __name__=='__main__':
    my_data = load_data(serial_file);
    array_data = np.array(my_data)
    fig = make_plot(array_data,out_path)
