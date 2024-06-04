import tkinter as tk
from tkinter import PhotoImage
import subprocess

# Global variable to store the process handle
virtualmouse_process = None
proton_process = None

def start_virtual_mouse():
    global virtualmouse_process
    virtualmouse_process = subprocess.Popen(["python", "Virtual_Mouse.py"])  # Run virtualmouse.py

def terminate_virtual_mouse():
    global virtualmouse_process
    if virtualmouse_process:
        virtualmouse_process.terminate()  # Terminate the virtualmouse.py process

def start_Proton():
    global proton_process
    proton_process = subprocess.Popen(["python", "Proton.py"])

def terminate_Proton():
    global proton_process
    if proton_process:
        proton_process.terminate()
# Create the main tkinter window
root = tk.Tk()
root.title("Virtual Mouse Using Hand Gesture")

# Load the logo image
logo_img = PhotoImage(file="logo.png")

# Create a label to display the logo
logo_label = tk.Label(root, image=logo_img)
logo_label.pack(pady=10)

# Create a button to start the virtual mouse
start_button = tk.Button(root, text="Start Virtual Mouse", command=start_virtual_mouse)
start_button.pack(pady=10)

# Create a button to terminate the virtual mouse
terminate_button = tk.Button(root, text="Terminate Virtual Mouse", command=terminate_virtual_mouse)
terminate_button.pack(pady=10)

# Create a button to start the Proton
start_button = tk.Button(root, text="Start Proton", command=start_Proton)
start_button.pack(pady=10)

# Create a button to terminate the Proton
terminate_button = tk.Button(root, text="Terminate Proton", command=terminate_Proton)
terminate_button.pack(pady=10)

# Run the tkinter event loop
root.mainloop()
