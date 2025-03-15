import os
import librosa
import librosa.display
import numpy as np 
import matplotlib.pyplot as plt
import torchaudio.functional as T

def Spectrogram(
        Song_name: str
    ):
    # Naming the Audio File which needs separation
    name_AudioFile = Song_name

    # Define input and output paths
    input_path = '/Users/aditya/Desktop/open-unmix/input/' + name_AudioFile + '.mp3' 
    output_path = '/Users/aditya/Desktop/open-unmix/output/' + name_AudioFile + '/' + 'images'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    src = librosa.load(input_path)

    # define Frame size and Hop size
    Frame_size = 2048
    Hop_size = 2048

    # librosa.stft
    # torchaudio.functional.spectrogram
    S_scale = librosa.stft(src[0], n_fft=Frame_size, hop_length=Hop_size)

    Y_scale = np.abs(S_scale)**2
    Y_log_scale = librosa.power_to_db(Y_scale)

    def plot_spectrogram(Y, sr, hop_length, y_axis="log"):
        plt.figure(figsize=(25, 10))
        librosa.display.specshow(Y, sr=sr, hop_length=hop_length, x_axis="time", y_axis=y_axis)
        plt.colorbar(format="%+2.0f")

        plt.savefig(output_path + '/' + 'images' + name_AudioFile + '_Spectrogram.png', bbox_inches='tight', pad_inches=0.8)

    plot_spectrogram(Y_log_scale, sr=src[1], hop_length=Hop_size)