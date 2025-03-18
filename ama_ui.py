import os 
import tkinter as tk
from tkinter import filedialog

# Function to select the input folder
def select_input_folder():
    input_folder_path = filedialog.askdirectory(title="Select the Input Folder")
    input_label.config(text=f"Input Folder: {input_folder_path}")

    input_folder_var.set(input_folder_path)
    
# Function to select the output folder
def select_output_folder():
    output_file_path = filedialog.askdirectory(title="Select the Output File")
    output_label.config(text=f"Output File: {output_file_path}")

    output_folder_var.set(output_file_path)

# Function to select an audio file
def select_audio_file():
    audio_file_path = filedialog.askopenfilename(title="Select the Audio File")
    audio_label.config(text=f"Audio File: {audio_file_path}")

    audio_file_var.set(audio_file_path)


# Function to break (close) the root window
def break_window():
    root.quit()
    root.destroy()  


# Create the root window
root = tk.Tk()
root.title("Select File Paths")

input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
audio_file_var = tk.StringVar()

# Add a label to display the selected input folder
input_label = tk.Label(root, text="Input Folder: Not selected")
input_label.pack(pady=10)

# Add a button to select the input folder
input_button = tk.Button(root, text="Select Input Folder", command=select_input_folder)
input_button.pack(pady=5)

# Add a label to display the selected output file
output_label = tk.Label(root, text="Output File: Not selected")
output_label.pack(pady=10)

# Add a button to select the output file
output_button = tk.Button(root, text="Select Output File", command=select_output_folder)
output_button.pack(pady=5)

# Add a label to display the selected input folder
audio_label = tk.Label(root, text="Audio File: Not selected")
audio_label.pack(pady=10)

# Add a button to select the input folder
audio_button = tk.Button(root, text="Select Audio File", command=select_audio_file)
audio_button.pack(pady=5)

# Add a button to break (close) the root window
close_button = tk.Button(root, text="Close Window", command=break_window)
close_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

input_folder = input_folder_var.get()
output_folder = output_folder_var.get()
audio_file = audio_file_var.get()

audio_basename = os.path.basename(audio_file)


print(f"{input_folder}")
print(f"{output_folder}")
print(f"{audio_basename}")
