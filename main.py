from tkinter import *
from tkinter import filedialog

root = Tk("Text Editor")
text = Text(root)
text.grid()

def saveas():
    global text
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), 
                    ("All files", "*.*")])
    if not file_path:
        return
    
    try:
        content = text.get("1.0", "end-1c")
        with open(file_path, 'w') as file:
            file.write(content)
    
        print(f"File berhasil disimpan di: {file_path}")

    except Exception as e:
        print(f"Gagal menyimpan file: {e}")

button = Button(root, text = "Save", command = saveas)
button.grid() 

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font = Menubutton(root, text="Font") 
font.grid() 

font.menu = Menu(font, tearoff = 0) 
font["menu"] = font.menu

helvetica = IntVar() 
courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable = courier,
command = FontCourier)

font.menu.add_checkbutton(label="Helvetica", variable = helvetica, 
command = FontHelvetica)

root.mainloop()