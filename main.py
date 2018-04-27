
import time

import matplotlib.pyplot as plt
import numpy as np
import pyautogui
from Xlib import display
from scipy import signal

# ------------------------------------------------
# sampling a mouse coordinate.
# ------------------------------------------------

all_org_data_x = []
all_org_data_y = []
all_cor_data_x = []
all_cor_data_y = []

count = 0
for i in range(2):
    count = 0
    t = []
    x = []
    y = []
    start_time = time.time()
    print("start sampling")
    while (time.time() - start_time <= 10):
        qp = display.Display().screen().root.query_pointer()
        x_coordinate = qp.root_x
        y_coordinate = qp.root_y
        y.append(y_coordinate)
        x.append(x_coordinate)
        t.append(time.time())
        count += 1
    nsamples = count
    sample_rate = count / 4.0
    all_org_data_x.append(x)
    all_org_data_y.append(y)
    y = np.array(y)
    x = np.array(x)
    t = np.array(t)

    # ------------------------------------------------
    # Create a FIR filter and apply it to x.
    # ------------------------------------------------

    # The Nyquist rate of the signal.
    nyq_rate = sample_rate / 2.0

    # The desired width of the transition from pass to stop,
    # relative to the Nyquist rate.  We'll design the filter
    # with a 5 Hz transition width.
    width = 5.0 / nyq_rate

    # The desired attenuation in the stop band, in dB.
    ripple_db = 60.0

    # Compute the order and Kaiser parameter for the FIR filter.
    N, beta = signal.kaiserord(ripple_db, width)

    # The cutoff frequency of the filter.
    cutoff_hz = 5.0

    # Use firwin with a Kaiser window to create a lowpass FIR filter.
    taps = signal.firwin(N, cutoff_hz / nyq_rate, window=('kaiser', beta))
    print("start fixing")
    # Use lfilter to filter x with the FIR filter.
    backfilter_x = signal.filtfilt(taps, 1.0, x)
    backfilter_y = signal.filtfilt(taps, 1.0, y)
    all_cor_data_x.append(backfilter_x)
    all_cor_data_y.append(backfilter_y)
    # ------------------------------------------------
    # correction mouse a movement.
    # ------------------------------------------------
    # os.system('setterm -cursor on')
    print("start walking")
    for v in range(0,len(backfilter_x),5):
        # m.move(backfilter_x[v],backfilter_y[v])
        pyautogui.moveTo(backfilter_x[v], backfilter_y[v], duration=0)

all_cor_data_x = [item for sublist in all_cor_data_x for item in sublist]
all_cor_data_y = [item for sublist in all_cor_data_y for item in sublist]
all_org_data_x = [item for sublist in all_org_data_x for item in sublist]
all_org_data_y = [item for sublist in all_org_data_y for item in sublist]

plt.plot(all_cor_data_x, all_cor_data_y, 'ro-')
plt.plot(all_org_data_x, all_org_data_y, 'bo-')
plt.show()