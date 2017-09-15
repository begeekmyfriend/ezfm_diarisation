# coding=utf-8

__author__ = 'hou'

import os
import sh

def split(filepath):
        splits = filepath.split('/')
        name = splits[len(splits) - 1]
        splits = name.split('.')
        return splits[0], splits[1]

def convert(input_file):
        name, suffix = split(input_file)
        wav_file = name + ".wav"
        cmd = "ffmpeg -i " + input_file + " -ar 16000 -ac 1 -f wav " + wav_file
        sh.run(cmd)
        return wav_file

def cut(input_file, delimit_points):
	if len(delimit_points) <= 2: return
        name, suffix = split(input_file)
	for i in range(0, len(delimit_points) - 1):
		cmd = "ffmpeg -i " + input_file + " -acodec copy -ss " + str(delimit_points[i]) + " -to " + str(delimit_points[i + 1]) + " " + name + "_" + str(i) + "." + suffix
		sh.run(cmd)
