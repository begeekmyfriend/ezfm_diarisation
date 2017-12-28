# coding=utf-8

__author__ = 'hou'

from sklearn.externals import joblib
import numpy as np
import wave
import mfcc

# smooth tiny interval
# 1100000111000 --> 000000000000 (111 < interval)
# 0011111000111 --> 111111111111 (000 < interval)
def interval_size(Yp, interval):
	last = Yp[0]
	start = 0
	for i in range(0, len(Yp)):
		if Yp[i] != last:
			delta = i - start
			if delta < interval:
				Yp[start:i] = Yp[i]
			else:
				start = i
		last = Yp[i]

# smooth error labels which occupy littlse in a window size
def window(Y, duration):
	time_window = duration / 60
        if time_window < 5:
                time_window = 5
	threshold = time_window
	Yp = np.ones(len(Y), dtype=np.int)

	for i in range(0, len(Y)):
		d = Y[np.max([0, i - time_window]) : np.min([i + time_window, len(Y)])]
		if (np.sum(d) < threshold):
			Yp[i] = 0

        # The interval of songs and speech should not be shorter than the window
        interval_size(Yp, time_window)
	return Yp

def run(input_wav, model):
        f = wave.open(input_wav, "r")
        duration = f.getnframes() / f.getframerate()

	X = mfcc.extract(input_wav, duration)

	clf = joblib.load(model)

	Y = clf.predict(X[:,:])
	#np.savetxt("Y.txt", Y)
	Yp = window(Y, duration)
	#np.savetxt("Yp.txt", Yp)

	last = Yp[0]
	delimit_point = [0]
	for i in range(0, len(Yp)):
		if Yp[i] != last:
			delimit_point.append(i)
		        last = Yp[i]

	return Yp, delimit_point
