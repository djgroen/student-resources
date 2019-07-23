import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

"""
Reads a simple CSV file and plots the first two colums (column #0 and #1). The first line of the CSV file is ignored.
"""

def read_datafile(file_name):
    data = np.loadtxt(file_name, delimiter=',', skiprows=1)
    return data


if __name__ == "__main__":

  data = read_datafile('example.csv')

  x = data[:,0] # time
  y = data[:,1] # camp 22 (Mahama)

  fig = plt.figure()

  ax1 = fig.add_subplot(111)

  ax1.set_title("Example Plot")    
  ax1.set_xlabel('Data type shown in dataset x')
  ax1.set_ylabel('Data type shown in dataset y')

  ax1.plot(x,y, label='some data')
  ax1.plot(x,y*1.5, label='same data times 1.5')

  leg = ax1.legend()

  plt.show()
