import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import customtkinter as ctk

from ama_Audio_Post_Processing import audio_post_processing
from ama_Audio_Post_Processing import audio_comparision
from ama_Audio_Separation import audio_separation

# theme_info = {"Black and White": "/Users/aditya/Desktop/open-unmix/z_Custom_Tkinter_theme/BandW.json",
#               "Purple": "/Users/aditya/Desktop/open-unmix/z_Custom_Tkinter_theme/purple.json",
#               "Dark Blue": "/Users/aditya/Desktop/open-unmix/z_Custom_Tkinter_theme/dark-blue.json"
#               }

# def set_theme(theme_name):
#     if theme_name in theme_info:
#         print(f"Setting theme to {theme_name}")
#         ctk.set_default_color_theme(theme_info[theme_name])
#         root.update()
#         print (theme_info[theme_name])
#     else:
#         print(f"Theme '{theme_name}' not found. Using default theme.")
#         ctk.set_default_color_theme("blue") 
#         root.update()

# ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("/Users/aditya/Desktop/open-unmix/z_Custom_Tkinter_theme/BandW.json")

class ComparisionWindow():
    def __init__(self,root):

        # Window Properties
        self.window = ctk.CTkToplevel()
        self.window.title("AMA: Comparision")
        self.window.geometry("1000x700")

        self.create_window()

        # Configure Grid
        self.window.rowconfigure((0,1), weight=2)
        self.window.rowconfigure((2,3,4,5,6,7,8), weight=1)

        self.window.columnconfigure((0), weight=2)
        self.window.columnconfigure((1,2,3,4,5), weight=1)
        self.window.columnconfigure((6), weight=1)


    def create_window(self):

        # Function to Select Stems
        def optionmenu_callback(choice):
            print(f"Optionmenu dropdown clicked: {choice}")

        # Add a label to display the Title
        title_label = ctk.CTkLabel(self.window, text="Algorithmic Mixing Assistant: Comparision", font=("Arial", 24))
        title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Creating a textbox for description
        intro_label = ctk.CTkLabel(self.window, text="Comparing Audio ", font=("Arial", 20) )
        intro_label.grid(row=1, column=0, columnspan=6, rowspan=2, padx=10, pady=10)

        # # Creating Option Menu for Vocal, Drums, Bass, Other
        # option_button = ctk.CTkOptionMenu(self.window, values=["Vocals", "Drums", "Bass", "Others"], command=optionmenu_callback)
        # option_button.grid(row=2, column=0, padx=10, pady=10)

        # Creating Option Menu for Vocal, Drums, Bass, Other
        option1 = ctk.CTkOptionMenu(self.window, values=["1", "2", "3", "4"], command=optionmenu_callback)
        option1.grid(row=2, column=0, padx=10, pady=10)

        # Creating Option Menu for Vocal, Drums, Bass, Other
        option2 = ctk.CTkOptionMenu(self.window, values=["1", "2", "3", "4"], command=optionmenu_callback)
        option2.grid(row=2, column=1, padx=10, pady=10)
        

class AnalysisWindow():
    def __init__(self,root):

        # Window Properties
        self.window = ctk.CTkToplevel()
        self.window.title("AMA: Analysis")
        self.window.geometry("1000x700")

        # Calling create_window
        self.create_window()

        # Configure Grid
        self.window.rowconfigure((0,1), weight=2)
        self.window.rowconfigure((2,3,4,5,6,7,8), weight=1)

        self.window.columnconfigure((0), weight=2)
        self.window.columnconfigure((1,2,3,4,5), weight=1)
        self.window.columnconfigure((6), weight=1)

        # Dict for the song name and its file path
        self.file_info = {}

    def create_window(self):

        # defining variables
        refsong1 = tk.StringVar()
        refsong2 = tk.StringVar()
        refsong3 = tk.StringVar()
        refsong4 = tk.StringVar()

        refsong1_label = tk.StringVar(value = "Reference Track 1")
        refsong2_label = tk.StringVar(value = "Reference Track 2")
        refsong3_label = tk.StringVar(value = "Reference Track 3")
        refsong4_label = tk.StringVar(value = "Reference Track 4")

        refsong1_lufs = tk.IntVar(value = "LUFS")
        refsong2_lufs = tk.IntVar(value = "LUFS")
        refsong3_lufs = tk.IntVar(value = "LUFS")
        refsong4_lufs = tk.IntVar(value = "LUFS")

        refsong1_dr = tk.IntVar(value = "Dynamic Range")
        refsong2_dr = tk.IntVar(value = "Dynamic Range")
        refsong3_dr = tk.IntVar(value = "Dynamic Range")
        refsong4_dr = tk.IntVar(value = "Dynamic Range")

        refsong1_pan = tk.IntVar(value = "Panning")
        refsong2_pan = tk.IntVar(value = "Panning")
        refsong3_pan = tk.IntVar(value = "Panning")
        refsong4_pan = tk.IntVar(value = "Panning")

        reference_tracks = []
        track_index = 0

        # def optionmenu_callback(self, choice): 
        #     print(f"Optionmenu dropdown clicked: {choice}")

        # store song name and its file path in the dict
        def store_data(name_AudioFile, filepath):
            self.file_info[name_AudioFile] = filepath

            print (self.file_info)

        # fetching file path from the dict
        def check_dict(track_index):
            # Ensure that track_index is within the range of available keys
            if len(self.file_info) == 0:
                print("Error: file_info is empty.")
                return None

            # Convert the keys to a list and check if track_index is valid
            # info_key = list(self.file_info.keys())
            info_key = track_index
            if track_index:
                return self.file_info[info_key]
            else:
                print(f"Error: track_index {track_index} is out of range.")
            return None

        # Function for processing LUFS for the Reference Track
        def calling_lufs(track_index, lufs_track_label):  
            arg = check_dict(track_index)
            output = audio_post_processing.torchAU_LUFS(arg)
            lufs_track_label.configure(text = "LUFS:"+ output + "dB")

        # Function for processing Dynamic Range for the Reference Track
        def calling_DynRange(track_index, dynamic_range_track_label):
            arg = check_dict(track_index)
            output = audio_post_processing.torchAU_DynRange(arg)
            dynamic_range_track_label.configure(text = "Dyn Range:" + output + "dB")

        # Function for processing Dynamic Range for the Reference Track
        def calling_Panning(track_index, panning_track_label):
            arg = check_dict(track_index)
            output = audio_post_processing.torchAU_Panning(arg)
            panning_track_label.configure(text = "Panning:" + output )

        # Function to compare LUFS
        # def compare_lufs(lufs1, lufs2):
        #     result = audio_comparision.compare_lufs(lufs1, lufs2)
        #     print (result)
        #     # compare_lufs_label.configure(text = result)

        # Function to Select Stems
        def optionmenu_callback(choice):
            print(f"Optionmenu dropdown clicked: {choice}")

        def calling_comparision():
            ComparisionWindow(self.window)

        # Function to load and process a track (dummy function for this example)
        def load_track(track_number, label_track, store_name):
            filepath = filedialog.askopenfilename(title=f"Select Track", filetypes = [("Audio Files", "*.wav *.mp3")])

            # getting the file path and renaming the button
            name_AudioFile = os.path.basename(filepath)

            store_name.set(name_AudioFile)
            
            label_track.set(name_AudioFile)

            store_data(name_AudioFile,filepath)
            
            if filepath:
                print(f"Track {track_number} loaded from: {filepath}")
            else:
                messagebox.showerror("Error", f"Failed to load {track_number} track.")
    
        # Add a label to display the Title
        title_label = ctk.CTkLabel(self.window, text="Algorithmic Mixing Assistant: Analysis", font=("Arial", 24))
        title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Creating a textbox for description
        intro_label = ctk.CTkLabel(self.window, text="Description of Analysis", font=("Arial", 20) )
        intro_label.grid(row=1, column=0, columnspan=6, rowspan=2, padx=10, pady=10)

        # Creating Option Menu for Vocal, Drums, Bass, Other
        option = ctk.CTkOptionMenu(self.window, values=["Vocals", "Drums", "Bass", "Others"], command=optionmenu_callback)
        option.grid(row=2, column=0, padx=10, pady=10)

        # Creating Comaprision Button
        comparision_button = ctk.CTkButton(self.window, text = "Comparision" , command=calling_comparision)
        comparision_button.grid(row=3, column=0, padx=10, pady=10)


        # Creating Reference Song Buttons
        refSong1_button = ctk.CTkButton(self.window, textvariable = refsong1_label , command=lambda: load_track(1,refsong1_label,refsong1))
        refSong1_button.grid(row=2, column=1, padx=5)
    
        refSong2_button = ctk.CTkButton(self.window, textvariable = refsong2_label, command=lambda: load_track(2,refsong2_label,refsong2))
        refSong2_button.grid(row=2, column=2, padx=5)

        refSong3_button = ctk.CTkButton(self.window, textvariable = refsong3_label, command=lambda: load_track(3,refsong3_label,refsong3))
        refSong3_button.grid(row=2, column=3, padx=5)

        refSong4_button = ctk.CTkButton(self.window, textvariable = refsong4_label, command=lambda: load_track(4,refsong4_label,refsong4))
        refSong4_button.grid(row=2, column=4, padx=5)


        # Creating LUFS Buttons
        lufs1_button = ctk.CTkButton(self.window, textvariable = refsong1_lufs, command=lambda: calling_lufs(refsong1.get(),lufs1_label))
        lufs1_button.grid(row=3, column=1, padx=5)

        lufs2_button = ctk.CTkButton(self.window, textvariable = refsong2_lufs, command=lambda: calling_lufs(refsong2.get(),lufs2_label))
        lufs2_button.grid(row=3, column=2, padx=5)

        lufs3_button = ctk.CTkButton(self.window, textvariable = refsong3_lufs, command=lambda: calling_lufs(refsong3.get(),lufs3_label))
        lufs3_button.grid(row=3, column=3, padx=5)

        lufs4_button = ctk.CTkButton(self.window, textvariable = refsong4_lufs, command=lambda: calling_lufs(refsong4.get(),lufs4_label))
        lufs4_button.grid(row=3, column=4, padx=5)


        # Creating Dynamic Range Buttons
        dynRange1_button = ctk.CTkButton(self.window, textvariable = refsong1_dr, command=lambda: calling_DynRange(refsong1.get(),dynRange1_label))
        dynRange1_button.grid(row=4, column=1, padx=5)

        dynRange2_button = ctk.CTkButton(self.window, textvariable = refsong2_dr, command=lambda: calling_DynRange(refsong2.get(),dynRange2_label))
        dynRange2_button.grid(row=4, column=2, padx=5)

        dynRange3_button = ctk.CTkButton(self.window, textvariable = refsong3_dr, command=lambda: calling_DynRange(refsong3.get(),dynRange3_label))
        dynRange3_button.grid(row=4, column=3, padx=5)

        dynRange4_button = ctk.CTkButton(self.window, textvariable = refsong4_dr, command=lambda: calling_DynRange(refsong4.get(),dynRange4_label))
        dynRange4_button.grid(row=4, column=4, padx=5)


        # Creating Panning Buttons
        panning1_button = ctk.CTkButton(self.window, textvariable = refsong1_pan, command=lambda: calling_Panning(refsong1.get(),panning1_label))
        panning1_button.grid(row=5, column=1, padx=5)

        panning2_button = ctk.CTkButton(self.window, textvariable = refsong2_pan, command=lambda: calling_Panning(refsong2.get(),panning2_label))
        panning2_button.grid(row=5, column=2, padx=5)

        panning3_button = ctk.CTkButton(self.window, textvariable = refsong3_pan, command=lambda: calling_Panning(refsong3.get(),panning3_label))
        panning3_button.grid(row=5, column=3, padx=5)

        panning4_button = ctk.CTkButton(self.window, textvariable = refsong4_pan, command=lambda: calling_Panning(refsong4.get(),panning4_label))
        panning4_button.grid(row=5, column=4, padx=5)


        # Creating LUFS Labels
        lufs1_label = ctk.CTkLabel(self.window, text = "LUFS: not processed", font = ("Arial", 14))
        lufs1_label.grid(row=6, column=1, padx=5)

        lufs2_label = ctk.CTkLabel(self.window, text = "LUFS: not processed", font = ("Arial", 14))
        lufs2_label.grid(row=6, column=2, padx=5)

        lufs3_label = ctk.CTkLabel(self.window, text = "LUFS: not processed", font = ("Arial", 14))
        lufs3_label.grid(row=6, column=3, padx=5)

        lufs4_label = ctk.CTkLabel(self.window, text = "LUFS: not processed", font = ("Arial", 14))
        lufs4_label.grid(row=6, column=4, padx=5)


        # Creating Dynamic Range Label 
        dynRange1_label = ctk.CTkLabel(self.window, text = "Dynamic Range: not processed", font = ("Arial", 14))
        dynRange1_label.grid(row=7, column=1, padx=5)

        dynRange2_label = ctk.CTkLabel(self.window, text = "Dynamic Range: not processed", font = ("Arial", 14))
        dynRange2_label.grid(row=7, column=2, padx=5)

        dynRange3_label = ctk.CTkLabel(self.window, text = "Dynamic Range: not processed", font = ("Arial", 14))
        dynRange3_label.grid(row=7, column=3, padx=5)

        dynRange4_label = ctk.CTkLabel(self.window, text = "Dynamic Range: not processed", font = ("Arial", 14))
        dynRange4_label.grid(row=7, column=4, padx=5)


        # Creating Panning Label 
        panning1_label = ctk.CTkLabel(self.window, text = "Panning: not processed", font = ("Arial", 14))
        panning1_label.grid(row=8, column=1, padx=5)

        panning2_label = ctk.CTkLabel(self.window, text = "Panning: not processed", font = ("Arial", 14))
        panning2_label.grid(row=8, column=2, padx=5)

        panning3_label = ctk.CTkLabel(self.window, text = "Panning: not processed", font = ("Arial", 14))
        panning3_label.grid(row=8, column=3, padx=5)

        panning4_label = ctk.CTkLabel(self.window, text = "Panning: not processed", font = ("Arial", 14))
        panning4_label.grid(row=8, column=4, padx=5)



        

class AudioSeparationWindow():
    def __init__(self,root):
        self.window = ctk.CTkToplevel()
        self.window.title("AMA : Separation")
        self.window.geometry("1000x700")
        
        self.create_widgets()

        # Configure Grid
        self.window.rowconfigure((0,1), weight=2, uniform='a')
        self.window.rowconfigure((2,3,5,6), weight=1, uniform='a')
        self.window.rowconfigure((4), weight=2, uniform='a')
        

        self.window.columnconfigure((0,1,2), weight=1, uniform='a')
        
    def create_widgets(self):

        # defining variables
        audio_file_path = tk.StringVar()
        output_folder_path = tk.StringVar()

        input_file_lable = tk.StringVar(value = "Audio File: Not selected")
        output_folder_lable = tk.StringVar(value = "Output File: Not selected")

        separation_history = tk.StringVar(value = "Separation History: No Activity")

        

        # Function to select the audio file
        def select_audio_file():
            input_Audio_File = filedialog.askopenfilename(title="Select the Audio File")

            # getting the file path and renaming the button
            name_AudioFile = os.path.basename(input_Audio_File)

            input_file_lable.set(f"Input File: {name_AudioFile}")
            audio_file_path.set(input_Audio_File)

        # Function to select the output file
        def output_folder():
            output_file_path = filedialog.askdirectory(title="Select the Output File")
            output_folder_lable.set(f"Output File: {output_file_path}")
            output_folder_path.set(output_file_path)
            

        def separation():
            separation_history.set(separation_history.get() + "\n" "Separation History: In Progress")
            self.window.update_idletasks()

            arg1 = audio_file_path.get()
            arg2 = output_folder_path.get()
            audio_separation.VDBO(arg1,arg2)

            separation_lable.configure(text = "Separation : Completed")

            # getting the file path and renaming the button
            name_AudioFile = os.path.basename(arg1)
            separation_history.set(separation_history.get() + "\n" + f"Separation History: The stems of {name_AudioFile} are saved in {arg2}")



        # Add a label to display the Title
        title_label = ctk.CTkLabel(self.window, text="Algorithmic Mixing Assistant: Separation", font=("Arial", 24))
        title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Creating a textbox for description
        intro_label = ctk.CTkLabel(self.window, text="Description of Separation", font=("Arial", 20))
        intro_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        
        # Creating Input Label
        input_label = ctk.CTkLabel(self.window, textvariable = input_file_lable)
        input_label.grid(row=2 , column=0, padx=5)

        # Creating Input Button
        input_button = ctk.CTkButton(self.window, text="Select Audio File", command=select_audio_file)
        input_button.grid(row=3, column=0, padx=5)

        # Creating Output Label
        output_label = ctk.CTkLabel(self.window, textvariable = output_folder_lable)
        output_label.grid(row=2, column=1, padx=5)

        # Creating Output Button
        output_button = ctk.CTkButton(self.window, text="Select Output File", command=output_folder)
        output_button.grid(row=3, column=1, padx=5)

        # Creating Separation Label
        separation_lable = ctk.CTkLabel(self.window, text="Separation: Not initiated")
        separation_lable.grid(row=2, column=2, padx=5)

        # Creating Separation Button
        separation_button = ctk.CTkButton(self.window, text="Separate", command=separation)
        separation_button.grid(row=3, column=2, padx=5)

        # Creating History Label
        history_label = ctk.CTkLabel(self.window, textvariable = separation_history)
        history_label.grid(row=4, column=0, columnspan=3, padx=5, sticky = 'w')

        # Creating Outro Label
        outro_label = ctk.CTkLabel(self.window, text="Version ~ 1.0.0",  font = ("Arial", 18))
        outro_label.grid(row=5, column=0, columnspan=3, sticky='e', padx=5)
        
class AlgorithmicMixingAssistantApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Algorithmic Mixing Assistant")
        self.root.geometry("1000x700")

        self.create_widgets()

        # Configure Grid
        self.root.rowconfigure((1,2,3,4,5,6,7), weight=1, uniform="a")
        self.root.rowconfigure((7), weight=2, uniform="a")

        self.root.columnconfigure((0,1,2), weight=1, uniform="a")
        self.root.rowconfigure((0), weight=2, uniform="a")

        # optionmenu_var = ctk.StringVar()

    # def optionmenu_callback(self, choice):
    #     set_theme(choice) 
    #     print(f"Optionmenu dropdown clicked: {choice}")

    def open_separation_window(self):
        AudioSeparationWindow(self.root)

    def open_analysis_window(self):
        AnalysisWindow(self.root)

    def create_widgets(self):

        def close_window():
            root.quit()
            root.destroy()

        # Add a label to display the Title
        self.title_label = ctk.CTkLabel(self.root, text="Algorithmic Mixing Assistant", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.intro_label = ctk.CTkLabel(self.root, 
                       text = " This project aims to develop an algorithmic music mixing assistant designed to support\nsound engineers in achieving a mix. The assistant will analyze user-provided reference\ntracks (2-3) and the current mix, offering suggestions on EQ curves, panning,\ncompression, tonal quality and peak RMS/LUFS measurements.This assistant will function\nsolely as a suggester, allowing users to make independent decisions and explore\ncreative solutions. While beginners will use the tool to achieve technical standards\nmore efficiently, professional engineers may find it valuable as it may provide\npossible solutions to a problem. Success will be measured by the assistant's ability\nto offer suggestions that positively influence the mix, bringing it closer to the reference tracks\nand empowering users to preserve the individuality and creative process in their mixes.", 
                       font = ("Arial", 20))
        self.intro_label.grid(row=1, column=0, columnspan=2, rowspan=6, padx=10, pady=10)

        # Add a button to open separation window
        self.separation_label = ctk.CTkLabel(self.root, text = "Separate Audio",font = ("Arial", 16))
        self.separation_label.grid(row=1, column=2, padx=10, pady=10)

        self.separation_button = ctk.CTkButton(self.root, text="Open", command=self.open_separation_window)
        self.separation_button.grid(row=2, column=2, padx=10, pady=10)

        # Add a button to open Analysis window
        self.analysis_label = ctk.CTkLabel(self.root, text = "Analyse Tracks",font = ("Arial", 16))
        self.analysis_label.grid(row=3, column=2, padx=10, pady=10)

        self.analysis_button = ctk.CTkButton(self.root, text="Open", command=self.open_analysis_window)
        self.analysis_button.grid(row=4, column=2, padx=10, pady=10)

        # # Add a button to close window
        # self.option_button = ctk.CTkOptionMenu(self.root, values=["Black and White", "Purple", "Dark Blue"], command=self.optionmenu_callback)
        # self.option_button.grid(row=5, column=2, padx=10, pady=10)

        # Add a button to close window
        self.close_button = ctk.CTkButton(self.root, text="Exit", command=close_window)
        self.close_button.grid(row=6, column=2, padx=10, pady=10)

        self.version_label = ctk.CTkLabel(self.root, text = "Version ~ 1.0.0", font = ("Arial", 18))
        self.version_label.grid(row=7, column=2, sticky='e' ,padx=10, pady=10)

root = ctk.CTk()
app = AlgorithmicMixingAssistantApp(root)
root.mainloop()
