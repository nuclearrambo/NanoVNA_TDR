import skrf as rf
import matplotlib.pyplot as plt
from scipy import constants
import numpy as np

raw_points = 101
NFFT = 16384
PROPAGATION_SPEED = 83

_prop_speed = PROPAGATION_SPEED/100
cable = rf.Network('cable_open_3.s1p')

s11 = cable.s[:, 0, 0]
window = np.blackman(raw_points)
s11 = window * s11
td = np.abs(np.fft.ifft(s11, NFFT))

#Calculate maximum time axis
t_axis = np.linspace(0, 1/cable.frequency.step, NFFT)
d_axis = constants.speed_of_light * _prop_speed * t_axis

#find the peak and distance
pk = np.max(td)
idx_pk = np.where(td == pk)[0]
print(d_axis[idx_pk[0]]/2)

# Plot time response
plt.plot(d_axis, td)
plt.xlabel("Distance (m)")
plt.ylabel("Magnitude")
plt.title("Return loss Time domain")
plt.show()
