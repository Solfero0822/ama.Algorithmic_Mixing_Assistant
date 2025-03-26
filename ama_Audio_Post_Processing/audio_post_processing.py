import os
import torch
import torchaudio
import torchaudio.transforms as T

import numpy as np


def torchAU_Speed(
        Speed_factor: float,
        Song_Name: str
        ):

    # Naming the Audio File which needs separation
    name_AudioFile = Song_Name

    # Define input and output paths
    input_path = '/Users/aditya/Desktop/open-unmix/input/' + name_AudioFile + '.mp3' 
    output_path = '/Users/aditya/Desktop/open-unmix/output/' + name_AudioFile  
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    src = torchaudio.load(input_path)
    src_waveform = src[0]
    src_sample_rate = src[1]

    Speed_factor_str = str(Speed_factor)    

    New_Speed = T.Speed(
        orig_freq = src_sample_rate,
        factor = Speed_factor,
    )

    New_src_waveform = New_Speed(src_waveform)

    torchaudio.save( 
        uri = output_path + '/' + name_AudioFile + '_ x' + Speed_factor_str +'.wav',
        src = New_src_waveform[0],
        sample_rate = src_sample_rate,
        channels_first = True,
        format = "wav",
        buffer_size = 1024
    )
    print('Audio File has been successfully saved at ' + output_path + '/' + name_AudioFile + '.wav')

def torchAU_LUFS(
        input_path: str,
        # output_path: str,
        # Song_Name: str,
        ):

    # Naming the Audio File which needs separation
    # name_AudioFile = Song_Name
    name_AudioFile = os.path.basename(input_path)

    # Define input and output paths
    # input_path = Song_path  
    ip =  input_path 
    # op = output_path + name_AudioFile  
    # if not os.path.exists(op):
    #     os.makedirs(op)

    src = torchaudio.load(ip)
    src_waveform = src[0]
    src_sample_rate = src[1]

    audio_waveform, audio_sample_rate = torchaudio.load(input_path, normalize=True)

    loudness_sampleRate = T.Loudness(sample_rate=audio_sample_rate)

    LUFS = loudness_sampleRate(audio_waveform)

    print(f"LUFS of {name_AudioFile} is {LUFS} dB")

    LUFS_int = (f"{LUFS:.2f}")

    return LUFS_int

def torchAU_DynRange(
        input_path: str,
        # output_path: str,
        # Song_Name: str,
    ):

    # Naming the Audio File which needs separation
    # name_AudioFile = Song_Name
    name_AudioFile = os.path.basename(input_path)


    # # Define input and output paths
    ip =  input_path # + name_AudioFile + '.mp3'  
    # op = output_path + name_AudioFile  
    # if not os.path.exists(op):
    #     os.makedirs(op)    

    src = torchaudio.load(ip)
    src_waveform = src[0]
    src_sample_rate = src[1]

    # Compute the maximum and minimum amplitudes of the waveform
    A_max = src[0].abs().max()
    A_min = src[0].pow(2).mean().sqrt()

    # Add a small epsilon to A_min to avoid division by zero
    # epsilon = 1e-10
    # A_mine = A_min + epsilon

    # Calculate the dynamic range in dB
    A_max_dB = 20 * np.log10(A_max)
    A_min_dB = 20 * np.log10(A_min)

    dynamic_range_dB = 20 * np.log10(A_max / A_min)

    # print (f"Loudest part of {name_AudioFile} is {A_max_dB} dB")
    # print (f"Softest part of {name_AudioFile} is {A_min_dB} dB")

    print(f"Dynamic Range of {name_AudioFile} is {dynamic_range_dB} dB")

    dynamic_range_dB_int = (f"{dynamic_range_dB:.2f}")

    return dynamic_range_dB_int

def torchAU_Panning(
        input_path: str,
        # output_path: str,
        # Song_Name: str,
    ):

     # Naming the Audio File which needs separation
    # name_AudioFile = Song_name
    name_AudioFile = os.path.basename(input_path)

    # Define input and output paths
    # input_path = '/Users/aditya/Desktop/open-unmix/input/' + name_AudioFile + '.mp3' 
    # output_path = '/Users/aditya/Desktop/open-unmix/output/' + name_AudioFile + '/' + 'images'
    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)

    ip = input_path

    # Load the stereo audio file
    waveform, sample_rate = torchaudio.load(ip) 

    # Ensure the audio is stereo
    if waveform.shape[0] != 2:
        raise ValueError("The input audio must be a stereo signal with 2 channels.")

    # Separate the channels: Left and Right
    left_channel = waveform[0, :]
    right_channel = waveform[1, :]

    # Function to calculate the energy of each channel (RMS value)
    def calculate_rms(signal):
        return torch.sqrt(torch.mean(signal ** 2))

    # Calculate RMS for each channel
    left_rms = calculate_rms(left_channel)
    right_rms = calculate_rms(right_channel)

    # Function to estimate panning
    def estimate_panning(left_rms, right_rms):
        # Normalize the RMS values
        total_rms = left_rms + right_rms
        if total_rms == 0:
            return 0.0  # No signal (centered or silent)
        
        # Calculate the panning ratio
        pan_ratio = (left_rms - right_rms) / total_rms
        return pan_ratio

    # Estimate panning
    pan_value = estimate_panning(left_rms, right_rms)

    # Print the pan value
    print(f"Estimated pan value of {name_AudioFile} is {pan_value:.2f}")
    print("Interpretation:")
    if pan_value < -0.5:
        print("Instrument is mostly panned to the left.")
    elif pan_value > 0.5:
        print("Instrument is mostly panned to the right.")
    else:
        print("Instrument is panned close to the center.")

    pan_value_int = (f"{pan_value:.2f}")  

    return pan_value_int