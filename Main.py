
from ama_Audio_Post_Processing import audio_post_processing
from ama_Audio_Separation import audio_separation

# List of songs in '/Users/aditya/Desktop/open-unmix/input/'

List_of_the_Song = [
    'ALittleLate_Sören', 
    'Bankroll_Tytillidie x Xollllinnnn', 
    'Blue_Ghostly-Beard', 
    'DeadRoses_Andrew Cole', 
    'DragMeDown_Adam Buckely', 
    'ItsSoEasyToLoveYou_David Tyo', 
    'Naturally_Allen Stone', 
    'Nostalgic_Strobe', 
    'SlowDown_Jessica Childress', 
    'SpiritCold_Tall Heights']

Song_Name = (List_of_the_Song[7])

# Speed of the song, 
## Values greater than 1.0 compress
## whereas values less than 1.0 stretch
Speed_factor = 1.5

## SEPARATION
audio_separation.VDBO(Song_Name)

## POST-PROCESSING

audio_post_processing.torchAU_LUFS(Song_Name)
audio_post_processing.torchAU_Speed(Speed_factor, Song_Name)