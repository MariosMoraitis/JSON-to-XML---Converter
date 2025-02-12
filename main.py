from convert import prepare_n_write
#from tkinter import * # type: ignore
from tkinter import filedialog
import customtkinter as ctk
import os

json_stored_path = []
output_stored_path = []

def json_button_click() -> None:
    json_file_path: str = filedialog.askopenfilename(filetypes=[('json/txt files', '*.json;*.txt')])
    if json_file_path:
        # Clear stored data
        json_stored_path.clear()
        output_stored_path.clear()
        result_label.configure(text="")
        open_file_button.pack_forget()
        # Apply new data
        json_stored_path.append(json_file_path)
        json_path_label.configure(text='Selected File: ' + json_file_path)
        check_conditions()

def convert_button_click() -> None:
    output_xml = prepare_n_write(json_stored_path[0])
    result_label.configure(text="Saved at: " + str(output_xml))
    output_stored_path.append(output_xml)
    open_file_button.pack()

def check_conditions() -> None:
    if json_path_label.cget("text"):
        convert_button.configure(state=ctk.NORMAL)
    else:
        convert_button.configure(state=ctk.DISABLED)

def open_file_button_click() -> None:
    path = os.path.dirname(os.path.abspath(output_stored_path[0]))
    os.startfile(path)

# Initialize the main window
root = ctk.CTk()
root.title('Soap Converter')
root.geometry('800x230')
root.resizable(False, False)

top_button_frame = ctk.CTkFrame(master=root)
top_button_frame.pack(side="top", pady=10)

# JSON Button + File Path Label
json_row = ctk.CTkFrame(master=top_button_frame)
json_row.pack(side="top", pady=5, fill="x")

json_button = ctk.CTkButton(master=json_row, text='Load JSON', command=json_button_click)
json_button.pack(side="left", padx=10)

json_path_label = ctk.CTkLabel(master=json_row, text="", width=300, anchor="w")
json_path_label.pack(side="left", padx=10)

# Convert Button (No Label)
convert_button = ctk.CTkButton(master=top_button_frame, text='Convert',state=ctk.DISABLED ,command=convert_button_click)
convert_button.pack(side="top", pady=10)

result_label = ctk.CTkLabel(master=root, text='',width=300, font=('Arial', 15))
result_label.pack(padx=10, pady=15)

open_file_button = ctk.CTkButton(master=root, text='Open File Location',command=open_file_button_click)
open_file_button.pack(side="top", pady=20)
open_file_button.pack_forget()
    
root.mainloop()