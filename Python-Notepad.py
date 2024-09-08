import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel

class MyNotepad:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x750")
        self.root.title("My Notepad")
        
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.filemenu.add_command(label="Save as...", command=self.save_as_text_file)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.actionmenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.actionmenu.add_command(label="Save all to clipboard", command=self.save_all_to_clipboard)
        self.actionmenu.add_command(label="Clear Notepad", command=self.clear)
        self.actionmenu.add_command(label="Set all text to lowercase", command=self.set_all_to_lowercase)
        self.actionmenu.add_command(label="Set all text to uppercase", command=self.set_all_to_uppercase)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")
        self.root.config(menu=self.menubar)
        
        self.textbox = tk.Text(self.root, height=28,font=('Arial',17))
        self.textbox.pack(padx=10,pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit the program? All data will be lost."):
            self.root.destroy()
            
    def clear(self):
        self.textbox.delete('1.0', tk.END)
    
    def save_as_text_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                text_content = self.textbox.get("1.0", tk.END)
                file.write(text_content)
                
    def save_all_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.textbox.get('1.0',tk.END))
        
    def set_all_to_lowercase(self):
        text_to_lower = self.textbox.get('1.0',tk.END)
        text_to_lower = text_to_lower.lower()
        self.textbox.delete('1.0',tk.END)
        self.textbox.insert(tk.INSERT,text_to_lower)
        
    def set_all_to_uppercase(self):
        text_to_upper = self.textbox.get('1.0',tk.END)
        text_to_upper = text_to_upper.upper()
        self.textbox.delete('1.0',tk.END)
        self.textbox.insert(tk.INSERT,text_to_upper)
        
        
if __name__ == "__main__":
    MyNotepad()
