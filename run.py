import ffmpeg
import mfcc
import predict
import train
import sh
import sys, getopt
import numpy as np
import matplotlib.pyplot as plt

def song_dump(songs):
        for p in songs:
                print str(p[0] / 3600) + ":" + str(p[0] % 3600 / 60) + ":" + str(p[0] % 60)
                print str(p[1] / 3600) + ":" + str(p[1] % 3600 / 60) + ":" + str(p[1] % 60)

def usage():
        print "python run.py -t input.wav | -p input.wav -m model.pkl"
        print "-t Extract MFCC feature from the input autio in standard deviation mode, train in SVM and generate the model"
        print "-p Predict the diarisation of the input audio"
        print "-m Specify the model when predition"

def main():
        model = ""
        opts, args = getopt.getopt(sys.argv[1:], "ht:p:m:")
        for op, value in opts:
                if op == "-h":
                        usage()
                        sys.exit();
                elif op == "-t":
                        input_file = value
                elif op == "-p":
                        input_file = value
                elif op == "-m":
                        model = value

        input_wav = ffmpeg.convert(input_file)
        if model == "":
                input_wav = "20160203c.wav"
	        songs_20160203c = [[0, 265], [1028,1245], [1440, 1696], [2177, 2693]]
                song_dump(songs_20160203c)
                model = train.run(input_wav, songs_20160203c)
	Y, delimit_points = predict.run(input_wav, model)
        for i in delimit_points:
                print str(i / 3600) + ":" + str(i % 3600 / 60) + ":" + str(i % 60)

        ffmpeg.cut(input_file, delimit_points)

	plt.figure()
	plt.plot(-0.2)
	plt.plot(1.2)
        if model == "":
                plt.plot(songs_20160203c, 'b')
	plt.plot(Y,'r')
	plt.show()

if __name__ == '__main__':
	main()
