# coding=utf-8

__author__ = 'hou'

from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import numpy as np

def extract(input_wav, duration):
	(rate, sig) = wav.read(input_wav)
	feature = mfcc(sig, rate)

	size_per_sec = len(feature) / duration
	time_window = 1
	std_tmp = []
	for j in range(0, len(feature[0])):
		xx = []
		for i in range(0, duration, time_window):
			xx.append(np.std(feature[i*size_per_sec: (i+time_window)*size_per_sec, j]))
		std_tmp.append(xx)

	std = np.transpose(std_tmp)
        return std
