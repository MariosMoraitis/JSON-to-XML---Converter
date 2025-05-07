from convert import prepare_n_write
from tkinter import filedialog
import customtkinter as ctk
import os

json_stored_path = []
output_stored_path = []

def json_button_click() -> None:
    json_file_path: str = filedialog.askopenfilename(filetypes=[('json/txt files', '*.json;*.txt')])
    if json_file_path:
        json_stored_path.clear()
        output_stored_path.clear()
        result_label.configure(text="")
        open_file_button.pack_forget()
        json_stored_path.append(json_file_path)
        truncated = json_file_path if len(json_file_path) < 50 else "..." + json_file_path[-47:]
        json_path_label.configure(text='Selected: ' + truncated)
        check_conditions()

def convert_button_click() -> None:
    output_xml: str = prepare_n_write(json_stored_path[0], prefix_entry.get())
    result_label.configure(text = output_xml)
    output_stored_path.append(output_xml)
    open_file_button.pack(pady=(5, 0))

def check_conditions() -> None:
    if json_path_label.cget("text"):
        convert_button.configure(state=ctk.NORMAL)
    else:
        convert_button.configure(state=ctk.DISABLED)

def open_file_button_click() -> None:
    path = os.path.dirname(os.path.abspath(output_stored_path[0]))
    os.startfile(path)

# Main window
root = ctk.CTk()
root.title('JSON --> XML Converter')
root.geometry('500x280')
root.resizable(False, False)

main_frame = ctk.CTkFrame(master=root)
main_frame.pack(padx=15, pady=15, fill="both", expand=True)

# Row 1: JSON Button + Label
json_row = ctk.CTkFrame(master=main_frame)
json_row.pack(pady=(0, 10), fill="x")

json_button = ctk.CTkButton(master=json_row, text='Load JSON', command=json_button_click, width=100)
json_button.pack(side="left", padx=(0, 10))

json_path_label = ctk.CTkLabel(master=json_row, text="", anchor="w", width=300)
json_path_label.pack(side="left", fill="x", expand=True)

# Row 2: Prefix Entry
prefix_entry = ctk.CTkEntry(master=main_frame, placeholder_text="Optional tag prefix", width=250)
prefix_entry.pack(pady=(0, 10))

# Row 3: Convert Button
convert_button = ctk.CTkButton(master=main_frame, text='Convert', state=ctk.DISABLED, command=convert_button_click)
convert_button.pack(pady=(0, 10))

# Row 4: Result Label
result_label = ctk.CTkLabel(master=main_frame, text='', font=('Arial', 13), wraplength=450)
result_label.pack(pady=(0, 10))

# Row 5: Open File Button (hidden until needed)
open_file_button = ctk.CTkButton(master=main_frame, text='Open File Location', command=open_file_button_click)
open_file_button.pack_forget()

root.mainloop()