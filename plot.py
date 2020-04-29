import matplotlib.pyplot as plt
import numpy as np
import serial
import time


t = np.arange(0,10, 0.1)
x = np.zeros(100)
y = np.zeros(100)
z = np.zeros(100)
over_5 = np.zeros(100)


serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200, timeout = 1)

print("Start!")
for i in range(99):
    linex=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    x[i] = float(linex)
    liney=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    y[i] = float(liney)
    linez=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    z[i] = float(linez)
    linet=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    over_5[i] = float(linet)
    

fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x, 'b', label = 'X')
ax[0].plot(t ,y , 'r', label = 'Y')
ax[0].plot(t, z, 'g', label = 'Z')
ax[0].legend()
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].stem(t, over_5) 
ax[1].set_xlabel('Time')
ax[1].set_ylabel('> 5cm')
plt.show()
s.close()