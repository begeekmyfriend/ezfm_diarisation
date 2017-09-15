# ezfm_diarisation
Fork from [ezfm_process](https://github.com/zhichenghou/ezfm_process)

根据MFCC提取音频特征，训练“飞鱼秀”音频节目语音和音乐的分类。

# Material
[应用机器学习分类声音文件中的音乐和人声](https://houzhicheng.com/blog/ml/2015/04/03/machine-learning-audio-process.html)

# Preinstallation
- [FFmpeg](https://ffmpeg.org)
- [python_speech_features](https://github.com/jameslyons/python_speech_features)
- [scikit-learn](https://scikit-learn.org)
- [scipy](https://www.scipy.org)

# Prediction
> python run.py -p input_audio -m model/20160203c.pkl

# Traing
> python run.py -t input_audio

Note: 本程序不对“飞鱼秀”以外的音频节目预测正确率负责，如有需要请自行训练。
