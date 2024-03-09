import tkinter as tk
from tkinter import PhotoImage, filedialog
from ocr_extraction import get_final_text


def on_folder_button_click():
    filepath = filedialog.askopenfilename()  # Open a file dialog to select a file
    if filepath:  # Check if a file is selected
        entry_file.delete(0, tk.END)  # Clear any existing text in the entry field
        entry_file.insert(0, filepath)  # Insert the selected file path into the entry field
        entry_file.config(fg="black")


def on_run_button_click():
    file_path = entry_file.get()
    entity_info = entry_entity.get()

    if file_path.strip() == "" or file_path == placeholder_text_file or \
            entity_info.strip() == "" or entity_info == placeholder_text_entity:
        # If either entry is empty (i.e., containing placeholder text or is just whitespace), display a message
        error_label.config(text="Error: Both Entry fields must be filled in.", fg="red")
    else:
        # Both entries are filled in, clear the error message if it's already shown
        error_label.config(text="")  # Clear the error message
        print(get_final_text(file_path))
        pass


def on_entry_click(event):
    if entry_file.get() == placeholder_text_file:
        entry_file.delete(0, tk.END)  # Delete placeholder text when user clicks on entry
        entry_file.config(fg="black")  # Change text color to black


def on_focus_out(event):
    if not entry_file.get():
        entry_file.insert(0, placeholder_text_file)  # Insert placeholder text when entry is empty
        entry_file.config(fg="grey")  # Change text color back to grey


def on_entry_entity_click(event):
    if entry_entity.get() == placeholder_text_entity:
        entry_entity.delete(0, tk.END)  # Delete placeholder text when user clicks on entry
        entry_entity.config(fg="black")  # Change text color to black


def on_focus_out_entity(event):
    if not entry_entity.get():
        entry_entity.insert(0, placeholder_text_entity)  # Insert placeholder text when entry is empty
        entry_entity.config(fg="grey")  # Change text color back to grey


root = tk.Tk()
root.title("Unstructured Data Extraction")
root.geometry("450x220")

file_label = tk.Label(root, text="File")
file_label.place(x=50, y=20)

placeholder_text_file = r"C:\Users\kelly\Downloads\CV.pdf"  # Placeholder text for the file entry field
entry_file = tk.Entry(root, width=40, fg="grey")  # Set initial text color to grey
entry_file.insert(0, placeholder_text_file)  # Insert placeholder text
entry_file.bind("<FocusIn>", on_entry_click)
entry_file.bind("<FocusOut>", on_focus_out)
entry_file.place(x=50, y=50)

folder_icon = PhotoImage(file="Images/folder_icon.png")

# Calculate the subsample factors for folder_icon
subsample_factor_x_folder = folder_icon.width() // 22
subsample_factor_y_folder = folder_icon.height() // 17

# Resize the icon using the subsample method
folder_icon_resized = folder_icon.subsample(subsample_factor_x_folder, subsample_factor_y_folder)
folder_button = tk.Button(root, image=folder_icon_resized, command=on_folder_button_click)
folder_button.place(x=300, y=45)

extract_label = tk.Label(root, text="Information to extract")
extract_label.place(x=50, y=80)

placeholder_text_entity = "Name, Age, Education"  # Placeholder text for the entity entry field
entry_entity = tk.Entry(root, width=40, fg="grey")  # Set initial text color to grey
entry_entity.insert(0, placeholder_text_entity)  # Insert placeholder text
entry_entity.bind("<FocusIn>", on_entry_entity_click)
entry_entity.bind("<FocusOut>", on_focus_out_entity)
entry_entity.place(x=50, y=110)

run_icon = PhotoImage(file="Images/run_icon.png")

# Calculate the subsample factors for run_icon
subsample_factor_x_run = run_icon.width() // 22
subsample_factor_y_run = run_icon.height() // 17

# Resize the icon using the subsample method
run_icon_resized = run_icon.subsample(subsample_factor_x_run, subsample_factor_y_run)
run_button = tk.Button(root, image=run_icon_resized, command=on_run_button_click)
run_button.place(x=300, y=105)

# Create the error label
error_label = tk.Label(root, text="", fg="red")
error_label.place(x=50, y=140)

root.mainloop()
