import os
import torch
import torchaudio 
from openunmix.predict import separate 

def VDBO(
        input_path: str,
        output_path: str,
        # Song_Name: str,
        
    ):
    # Naming the Audio File which needs separation

    Song_Name = os.path.basename(input_path)

    name_AudioFile = Song_Name.replace('.mp3','')

    # Define input and output paths
    ip = input_path 
    op = output_path + '/' + name_AudioFile

    # Function to separate audio into its components
    def separate_audio(ip, op):
        # Ensure the output directory exists
        if not os.path.exists(op):
            os.makedirs(op)

        # Load the audio file
        src = torchaudio.load(uri = ip)

        # Perform the separation
        estimates = separate(
                            audio = src[0],
                            rate = src[1] )
        
        # Testing the output of audio_tensor
        ## audio_tensor = torch.tensor(estimates.get('vocals'))
        ## print(audio_tensor[0])

        tracks = ["vocals",'drums','bass','other']
        # Save the separated track
        for track in tracks:
            torchaudio.save( 
                uri = op + '/'+ name_AudioFile + '_'+ track + '.wav',
                src = torch.tensor(estimates.get(track))[0],
                sample_rate = 44100,
                channels_first = True,
                format = "wav",
                buffer_size = 1024
            )
            
        # output_path, track_waveform, sample_rate)
        print(f"Saved to {op}")

    # Call the function to separate the audio
    separate_audio(ip, op)

    # Final Print Statement
    print(f"Separation of {Song_Name} into VDBO is completd and saved at {op}")

