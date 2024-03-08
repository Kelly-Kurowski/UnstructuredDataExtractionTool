import tkinter as tk
from tkinter import PhotoImage

def on_folder_button_click():
    # Your button click event handler here
    pass

def on_entry_click(event):
    if entry_file.get() == placeholder_text:
        entry_file.delete(0, tk.END)  # Delete placeholder text when user clicks on entry
        entry_file.config(fg="black")  # Change text color to black

def on_focus_out(event):
    if not entry_file.get():
        entry_file.insert(0, placeholder_text)  # Insert placeholder text when entry is empty
        entry_file.config(fg="grey")  # Change text color back to grey

root = tk.Tk()
root.title("Extract Unstructured Data Activity")
root.geometry("500x220")

file_label = tk.Label(root, text="File")
file_label.place(x=50, y=20)

placeholder_text = r"C:\Users\kelly\Downloads\CV.pdf"  # Placeholder text for the entry field
entry_file = tk.Entry(root, width=40, fg="grey")  # Set initial text color to grey
entry_file.insert(0, placeholder_text)  # Insert placeholder text
entry_file.bind("<FocusIn>", on_entry_click)
entry_file.bind("<FocusOut>", on_focus_out)
entry_file.place(x=50, y=50)

folder_icon = PhotoImage(file="Images/folder_icon.png")

# Calculate the subsample factors
subsample_factor_x = folder_icon.width() // 22
subsample_factor_y = folder_icon.height() // 18

# Resize the icon using the subsample method
folder_icon_resized = folder_icon.subsample(subsample_factor_x, subsample_factor_y)
folder_button = tk.Button(root, image=folder_icon_resized, command=on_folder_button_click)
folder_button.place(x=300, y=45)

extract_label = tk.Label(root, text="Data to extract")
extract_label.place(x=50, y=80)

root.mainloop()