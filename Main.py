
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

## SEPARATION
audio_separation.VDBO(Song_Name)