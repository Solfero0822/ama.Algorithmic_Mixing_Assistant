import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


from ama_Audio_Post_Processing import audio_post_processing
from ama_Audio_Separation import audio_separation

# Function to select the input folder
def select_input_folder():
    input_folder_path = filedialog.askdirectory(title="Select the Input Folder")
    input_label.config(text=f"Input Folder: {input_folder_path}")

    input_folder_var.set(input_folder_path)
    
# Function to select the output file
def select_output_file():
    output_file_path = filedialog.askdirectory(title="Select the Output File")
    output_label.config(text=f"Output File: {output_file_path}")

    output_folder_var.set(output_file_path)

def separation_window():
    separation_window = tk.Toplevel()
    separation_window.title("AMA : Separation")
    separation_window.geometry("500x700")

    separation_window.rowconfigure((0,1,2,3,4,5,6), weight=1)
    separation_window.columnconfigure(0, weight=1)
    

    def select_audio_file():
        input_Audio_File = filedialog.askopenfilename(title="Select the Audio File")
        input_label.config(text=f"Input Folder: {input_Audio_File}")

        audio_file_var.set(input_Audio_File)
    
    # Function to select the output file
    def output_file():
        output_file_path = filedialog.askdirectory(title="Select the Output File")
        output_label.config(text=f"Output File: {output_file_path}")

        output_folder_var.set(output_file_path)


    audio_file_var = tk.StringVar()
    output_folder_var = tk.StringVar()

    def separation():
        arg1 = audio_file_var.get()
        arg2 = output_folder_var.get()
        audio_separation.VDBO(arg1,arg2)
        separation_label.config(text = "Separation : Completed")

    # Add a label to display the selected input folder
    input_label = tk.Label(separation_window, text="Audio File: Not selected")
    input_label.grid(row=0 , column=0 )

    # Add a button to select the input folder
    input_button = tk.Button(separation_window, text="Select Audio File", command=select_audio_file)
    input_button.grid(row=1, column=0)

    # Add a label to display the selected output file
    output_label = tk.Label(separation_window, text="Output File: Not selected")
    output_label.grid(row=2, column=0)

    # Add a button to select the output file
    output_button = tk.Button(separation_window, text="Select Output File", command=output_file)
    output_button.grid(row=3, column=0)

    # Add a label to display the selected output file
    separation_label = tk.Label(separation_window, text="Separation: Not initiated")
    separation_label.grid(row=4, column=0)

    # Add a button to select the output file
    separation_button = tk.Button(separation_window, text="Separate", command=separation)
    separation_button.grid(row=5, column=0)


# Function to close the root window
def close_window():
    root.quit()
    root.destroy() 

# Create the root window
root = tk.Tk()
root.title("Algorithmic Mixing Assistant")
root.geometry("900x700")

# Configure Grid
root.columnconfigure((0,1,2), weight=1, uniform="a")
root.rowconfigure((0,2,3), weight=1, uniform="a")
root.rowconfigure(1, weight=5, uniform="a")

input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
audio_file_var = tk.StringVar()

# Labels
title_label = tk.Label(root, text = "Algorithmic Mixing Assistant", font = ("Arial", 24))
intro_label = tk.Label(root, 
                       text = " This project aims to develop an algorithmic music mixing assistant designed to support\nsound engineers in achieving a mix. The assistant will analyze user-provided reference\ntracks (2-3) and the current mix, offering suggestions on EQ curves, panning,\ncompression, tonal quality and peak RMS/LUFS measurements.This assistant will function\nsolely as a suggester, allowing users to make independent decisions and explore\ncreative solutions. While beginners will use the tool to achieve technical standards\nmore efficiently, professional engineers may find it valuable as it may provide\npossible solutions to a problem. Success will be measured by the assistant's ability\nto offer suggestions that positively influence the mix, bringing it closer to the reference tracks\nand empowering users to preserve the individuality and creative process in their mixes.", 
                       font = ("Arial", 18))
input_label = tk.Label(root, text = "Input Folder: Not selected")
output_label = tk.Label(root, text = "Output File: Not selected")

# Buttons
input_button = tk.Button(root, text = "Select Input Folder", command = select_input_folder)
output_button = tk.Button(root, text = "Select Output File", command = select_output_file)

separation_button = tk.Button(root, text = "Separation", command = separation_window)

close_button = tk.Button(root, text = "Next", command = close_window)

# Packing
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
intro_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
input_label.grid(row=2, column=0, padx=10, pady=10)
input_button.grid(row=3, column=0, padx=10, pady=10)
output_label.grid(row=2, column=1, padx=10, pady=10)
output_button.grid(row=3, column=1, padx=10, pady=10)
separation_button.grid(row=2, column=3, padx=10, pady=10)

close_button.grid(row=3, column=3, padx=10, pady=10)

root.mainloop()

input_folder_path = input_folder_var.get()
output_folder_path = output_folder_var.get()

print(f"{input_folder_path}")
print(f"{output_folder_path}")

# --------------------  2nd Window  -------------------------

# Function to load and process a track (dummy function for this example)
def load_track1(track_type):
    filepath = filedialog.askopenfilename(title=f"Select {track_type} Track", filetypes = [("Audio Files", "*.wav *.mp3")])
    if filepath:
        print(f"{track_type} track loaded from: {filepath}")
        
        # getting the file path and renaming the button
        name_AudioFile = os.path.basename(filepath)
        refSong1_lable.set(name_AudioFile)
        refSong1.set(filepath)
    else:
        messagebox.showerror("Error", f"Failed to load {track_type} track.")

def load_track2(track_type):
    filepath = filedialog.askopenfilename(title=f"Select {track_type} Track", filetypes = [("Audio Files", "*.wav *.mp3")])
    if filepath:
        print(f"{track_type} track loaded from: {filepath}")
        
        # getting the file path and renaming the button
        name_AudioFile = os.path.basename(filepath)
        refSong2_lable.set(name_AudioFile)
        refSong2.set(filepath)
    else:
        messagebox.showerror("Error", f"Failed to load {track_type} track.")

def load_track3(track_type):
    filepath = filedialog.askopenfilename(title=f"Select {track_type} Track", filetypes = [("Audio Files", "*.wav *.mp3")])
    if filepath:
        print(f"{track_type} track loaded from: {filepath}")
        
        # getting the file path and renaming the button
        name_AudioFile = os.path.basename(filepath)
        refSong3_lable.set(name_AudioFile)
        refSong3.set(filepath)
    else:
        messagebox.showerror("Error", f"Failed to load {track_type} track.")

def load_track4(track_type):
    filepath = filedialog.askopenfilename(title=f"Select {track_type} Track", filetypes = [("Audio Files", "*.wav *.mp3")])
    if filepath:
        print(f"{track_type} track loaded from: {filepath}")
        
        # getting the file path and renaming the button
        name_AudioFile = os.path.basename(filepath)
        refSong4_lable.set(name_AudioFile)
        refSong4.set(filepath)
    else:
        messagebox.showerror("Error", f"Failed to load {track_type} track.")

# Import buttons for tracks
reference_tracks = []
def import_reference_track1(track_number):
    track = load_track1(f"Reference Track {track_number}")
    if track:
        reference_tracks.append(track)

def import_reference_track2(track_number):
    track = load_track2(f"Reference Track {track_number}")
    if track:
        reference_tracks.append(track)

def import_reference_track3(track_number):
    track = load_track3(f"Reference Track {track_number}")
    if track:
        reference_tracks.append(track)

def import_reference_track4(track_number):
    track = load_track4(f"Reference Track {track_number}")
    if track:
        reference_tracks.append(track)

# Function for processing LUFS for the Reference Track
def calling_lufs1():  
    arg1 = refSong1.get()
    output = audio_post_processing.torchAU_LUFS(arg1)
    lufs_label1.config(text = "LUFS:"+ output + "dB")

def calling_lufs2():  
    arg1 = refSong2.get()
    output = audio_post_processing.torchAU_LUFS(arg1)
    lufs_label2.config(text = "LUFS:"+ output + "dB")

def calling_lufs3():  
    arg1 = refSong3.get()
    output = audio_post_processing.torchAU_LUFS(arg1)
    lufs_label3.config(text = "LUFS:"+ output + "dB")

def calling_lufs4():  
    arg1 = refSong4.get()
    output = audio_post_processing.torchAU_LUFS(arg1)
    lufs_label4.config(text = "LUFS:"+ output + "dB")


# Function for processing Dynamic Range for the Reference Track
def calling_DynRange1():
    arg1 = refSong1.get()
    output = audio_post_processing.torchAU_DynRange(arg1)
    dynamic_range_label1.config (text = "Dyn Range:" + output + "dB")

def calling_DynRange2():
    arg1 = refSong2.get()
    output = audio_post_processing.torchAU_DynRange(arg1)
    dynamic_range_label2.config (text = "Dyn Range:" + output + "dB")

def calling_DynRange3():
    arg1 = refSong3.get()
    output = audio_post_processing.torchAU_DynRange(arg1)
    dynamic_range_label3.config (text = "Dyn Range:" + output + "dB")

def calling_DynRange4():
    arg1 = refSong4.get()
    output = audio_post_processing.torchAU_DynRange(arg1)
    dynamic_range_label4.config (text = "Dyn Range:" + output + "dB")

# Creating the main window
root = tk.Tk()
root.title("Algorithmic Mixing Assistant")
root.geometry("900x700")

# Title Label
title_label = tk.Label(root, text = "Algorithmic Mixing Assistant", font = ("Arial", 24))
title_label.pack(padx=10, pady=10)

# Frame for Import Buttons and Track Display
frame = tk.Frame(root)
frame.pack(pady=20)

refSong1 = tk.StringVar()
refSong2 = tk.StringVar()
refSong3 = tk.StringVar()
refSong4 = tk.StringVar()

refSong1_lable = tk.StringVar(value = "Import Reference Track 1")
refSong2_lable = tk.StringVar(value = "Import Reference Track 2")
refSong3_lable = tk.StringVar(value = "Import Reference Track 3")
refSong4_lable = tk.StringVar(value = "Import Reference Track 4")

# Buttons
button1 = tk.Button(frame, textvariable = refSong1_lable, command=lambda: import_reference_track1(1))
button2 = tk.Button(frame, textvariable = refSong2_lable, command=lambda: import_reference_track2(2))
button3 = tk.Button(frame, textvariable = refSong3_lable, command=lambda: import_reference_track3(3))
button4 = tk.Button(frame, textvariable = refSong4_lable, command=lambda: import_reference_track4(4))

# Packing
button1.grid(row=0, column=0, padx=10)
button2.grid(row=0, column=1, padx=10)
button3.grid(row=0, column=2, padx=10)
button4.grid(row=0, column=3, padx=10)

# Frame for displaying visualizations
visualization_frame = tk.Frame(root)
visualization_frame.pack(pady=20)

refSong1_lufs = tk.IntVar(value = "LUFS")
refSong2_lufs = tk.IntVar(value = "LUFS")
refSong3_lufs = tk.IntVar(value = "LUFS")
refSong4_lufs = tk.IntVar(value = "LUFS")

refSong1_DR = tk.IntVar(value = "Dyn Range")
refSong2_DR = tk.IntVar(value = "Dyn Range")
refSong3_DR = tk.IntVar(value = "Dyn Range")
refSong4_DR = tk.IntVar(value = "Dyn Range")

# Labels
lufs_label1 = tk.Label(visualization_frame, text = "LUFS: 0.0 dB", font = ("Arial", 14))
lufs_label2 = tk.Label(visualization_frame, text = "LUFS: 0.0 dB", font = ("Arial", 14))
lufs_label3 = tk.Label(visualization_frame, text = "LUFS: 0.0 dB", font = ("Arial", 14))
lufs_label4 = tk.Label(visualization_frame, text = "LUFS: 0.0 dB", font = ("Arial", 14))

dynamic_range_label1 = tk.Label(visualization_frame, text = "Dynamic Range: 0.00 dB", font = ("Arial", 14))
dynamic_range_label2 = tk.Label(visualization_frame, text = "Dynamic Range: 0.00 dB", font = ("Arial", 14))
dynamic_range_label3 = tk.Label(visualization_frame, text = "Dynamic Range: 0.00 dB", font = ("Arial", 14))
dynamic_range_label4 = tk.Label(visualization_frame, text = "Dynamic Range: 0.00 dB", font = ("Arial", 14))

# Buttons
FE_LUFS1 = tk.Button(frame, textvariable = refSong1_lufs, command = calling_lufs1)
FE_LUFS2 = tk.Button(frame, textvariable = refSong2_lufs, command = calling_lufs2)
FE_LUFS3 = tk.Button(frame, textvariable = refSong1_lufs, command = calling_lufs3)
FE_LUFS4 = tk.Button(frame, textvariable = refSong2_lufs, command = calling_lufs4)

FE_DynRange1 = tk.Button(frame, textvariable = refSong1_DR, command = calling_DynRange1)
FE_DynRange2 = tk.Button(frame, textvariable = refSong2_DR, command = calling_DynRange2)
FE_DynRange3 = tk.Button(frame, textvariable = refSong3_DR, command = calling_DynRange3)
FE_DynRange4 = tk.Button(frame, textvariable = refSong4_DR, command = calling_DynRange4)

close_button = tk.Button(root, text = "Done", command = close_window)


# Packing
FE_LUFS1.grid(row=2, column=0, padx=10)
FE_LUFS2.grid(row=2, column=1, padx=10)
FE_LUFS3.grid(row=2, column=2, padx=10)
FE_LUFS4.grid(row=2, column=3, padx=10)

FE_DynRange1.grid(row=3, column=0, padx=10)
FE_DynRange2.grid(row=3, column=1, padx=10)
FE_DynRange3.grid(row=3, column=2, padx=10)
FE_DynRange4.grid(row=3, column=3, padx=10)

lufs_label1.grid(row=0, column=0, padx=20)
lufs_label2.grid(row=0, column=1, padx=20)
lufs_label3.grid(row=0, column=2, padx=20)
lufs_label4.grid(row=0, column=3, padx=20)

dynamic_range_label1.grid(row=1, column=0, padx=20)
dynamic_range_label2.grid(row=1, column=1, padx=20)
dynamic_range_label3.grid(row=1, column=2, padx=20)
dynamic_range_label4.grid(row=1, column=3, padx=20)

close_button.pack(pady=20)

# Panel to display the LUFS and Dynamic Range bar chart
lufs_dynamic_range_panel = tk.Label(visualization_frame)
lufs_dynamic_range_panel.grid(row=1, column=1, padx=20, pady=10)

# Run the Tkinter event loop
root.mainloop()