import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.font import Font

class MyNotepad:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x750")
        self.root.title("My Notepad")
        self.root.configure(bg='lightblue')

        self.current_font = Font(family="Arial", size=16)
        self.fonts = ['Arial','Courier New', 'Comic Sans MS', 'Times New Roman', 'Impact', 'MS Sans Serif', 'Roman', 'System']
        
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.actionmenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.fontmenu = tk.Menu(self.actionmenu,tearoff=0, font=('Arial',12))
        self.actionmenu.add_cascade(menu=self.fontmenu, label="Fonts")
        self.filemenu.add_command(label="Save as...", command=self.save_as_text_file)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.actionmenu.add_command(label="Copy to clipboard", command=self.save_all_to_clipboard)
        self.actionmenu.add_command(label="Paste from clipboard", command=self.paste_from_clipboard)
        self.actionmenu.add_command(label="Clear Notepad", command=self.clear)
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label="Set all text to lowercase", command=self.set_all_to_lowercase)
        self.actionmenu.add_command(label="Set all text to uppercase", command=self.set_all_to_uppercase)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")
        
        # for font in self.fonts:
        #     self.fontmenu.add_command(label=font,font=(font,12),command=lambda: self.set_new_font(font))
        self.fontmenu.add_command(label='Arial',font=('Arial',12),command=lambda: self.set_new_font('Arial'))
        self.fontmenu.add_command(label='Courier New',font=('Courier New',12),command=lambda: self.set_new_font('Courier New'))
        self.fontmenu.add_command(label='Comic Sans MS',font=('Comic Sans MS',12),command=lambda: self.set_new_font('Comic Sans MS'))
        self.fontmenu.add_command(label='Times New Roman',font=('Times New Roman',12),command=lambda: self.set_new_font('Times New Roman'))
        self.fontmenu.add_command(label='Impact',font=('Impact',12),command=lambda: self.set_new_font('Impact'))
        self.fontmenu.add_command(label='MS Sans Serif',font=('MS Sans Serif',12),command=lambda: self.set_new_font('MS Sans Serif'))
        self.fontmenu.add_command(label='Roman',font=('Roman',12),command=lambda: self.set_new_font('Roman'))
        self.fontmenu.add_command(label='System',font=('System',12),command=lambda: self.set_new_font('System'))
        
        self.root.config(menu=self.menubar)
        
        self.textbox = tk.Text(self.root,font=(self.current_font))
        self.textbox.pack(padx=10,pady=10,expand=True,fill="both")
        
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
    
    def paste_from_clipboard(self):
        to_paste = self.root.clipboard_get()
        self.textbox.insert(tk.INSERT,to_paste)
    
    def set_new_font(self,font):
        self.current_font = Font(family=font, size=16)
        self.textbox.configure(font=self.current_font)
        
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
