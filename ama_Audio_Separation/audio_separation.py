import os
import torch
import torchaudio 
from openunmix.predict import separate 

def VDBO(
        Song_Name: str,
        
    ):
    # Naming the Audio File which needs separation
    name_AudioFile = Song_Name

    # Define input and output paths
    input_path = '/Users/aditya/Desktop/open-unmix/input/' + name_AudioFile + '.mp3' 
    output_path = '/Users/aditya/Desktop/open-unmix/output/' + name_AudioFile  

    # Function to separate audio into its components
    def separate_audio(input_path, output_path):
        # Ensure the output directory exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Load the audio file
        src = torchaudio.load(uri = input_path)

        # Perform the separation
        estimates = separate(
                            audio = src[0],
                            rate = 44100 )
        
        # Testing the output of audio_tensor
        ## audio_tensor = torch.tensor(estimates.get('vocals'))
        ## print(audio_tensor[0])

        tracks = ["vocals",'drums','bass','other']
        # Save the separated track
        for track in tracks:
            torchaudio.save( 
                uri = output_path + '/'+ name_AudioFile + '_'+ track + '.wav',
                src = torch.tensor(estimates.get(track))[0],
                sample_rate = 44100,
                channels_first = True,
                format = "wav",
                buffer_size = 1024
            )
            
        # output_path, track_waveform, sample_rate)
        print(f"Saved to {output_path}")

    # Call the function to separate the audio
    separate_audio(input_path, output_path)

    # Final Print Statement
    print(f"Separation of {Song_Name} into VDBO is completd and saved at {output_path}")