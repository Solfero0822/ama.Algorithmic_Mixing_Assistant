import os
import torchaudio
import torchaudio.transforms as T

# Importing from Main.py
# from Main import Song_Name
# from Main import Speed_factor



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
        Song_Name: str,
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

    audio_waveform, audio_sample_rate = torchaudio.load(input_path, normalize=True)

    loudness_sampleRate = T.Loudness(sample_rate=audio_sample_rate)

    LUFS = loudness_sampleRate(audio_waveform)

    print(f"LUFS: {LUFS}")