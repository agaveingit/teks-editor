import customtkinter
from customtkinter import filedialog

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("themes/dark-blue.json")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
text = customtkinter.CTkTextbox(app, width=200, height=100)
text.pack(pady=20)

def saveas():
    global text
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), 
                    ("All files", "*.*")]
    )
    if not file_path:
        return
    
    try:
        content = text.get("1.0", "end-1c")
        with open(file_path, 'w') as file:
            file.write(content)
    
        print(f"File berhasil disimpan di: {file_path}")

    except Exception as e:
        print(f"Gagal menyimpan file: {e}")

def open_file():
    file = filedialog.askopenfile(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), 
                    ("All files", "*.*")]
    )

def button_function():
    saveas()

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()