import tkinter as tk
from tkinter import messagebox, filedialog

class MyNotepad:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x750")
        self.root.title("My Notepad")
        self.root.configure(bg='lightblue')
        self.char_count = tk.Frame(self.root,bd=1,relief='sunken')
        self.char_count.pack(side='bottom',fill='x')

        self.char_count_var = tk.StringVar()
        self.char_count_checked = tk.IntVar()

        self.draw_space_var = tk.StringVar()
        self.draw_space_checked = tk.IntVar()

        self.char_count_label = tk.Label(self.char_count, textvariable=self.char_count_var, anchor='w',padx=5,pady=5)
        self.char_count_label.pack(fill='x')

        self.current_font = 'Arial'
        self.font_size = 12
        self.fonts = ['Arial','Courier New', 'Comic Sans MS', 'Times New Roman', 'Impact', 'MS Sans Serif', 'Roman', 'System']
        
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.actionmenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.fontmenu = tk.Menu(self.actionmenu,tearoff=0, font=('Arial',12))
        self.fontsizesmenu = tk.Menu(self.fontmenu,tearoff=0, font=('Arial',12))
        self.settingsmenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.actionmenu.add_cascade(menu=self.fontmenu, label="Fonts")
        self.fontmenu.add_cascade(menu=self.fontsizesmenu, label="Font sizes")
        self.filemenu.add_command(label="Open file", command=self.open_file)
        self.filemenu.add_command(label="Save as...", command=self.save_as_text_file)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.actionmenu.add_command(label="Copy to clipboard", command=self.save_all_to_clipboard)
        self.actionmenu.add_command(label="Paste from clipboard", command=self.paste_from_clipboard)
        self.actionmenu.add_command(label="Clear Notepad", command=self.clear)
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label="Set all text to lowercase", command=self.set_all_to_lowercase)
        self.actionmenu.add_command(label="Set all text to uppercase", command=self.set_all_to_uppercase)
        self.settingsmenu.add_checkbutton(label="Show character count", command=self.character_count,variable=self.char_count_checked)
        self.settingsmenu.add_checkbutton(label="Add canvas", command=self.draw_space,variable=self.draw_space_checked)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")
        self.menubar.add_cascade(menu=self.settingsmenu, label='Settings')
        
        # for font in self.fonts:
        #     self.fontmenu.add_command(label=font,font=(font,12),command=lambda: self.set_new_font(font))
        self.fontmenu.add_command(label='Change font size',font=('Arial',12))
        self.fontsizesmenu.add_command(label='Font size: 16',font=('Arial',16),command=lambda: self.set_new_font_size(16))
        self.fontsizesmenu.add_command(label='Font size: 18',font=('Arial',18),command=lambda: self.set_new_font_size(18))
        self.fontsizesmenu.add_command(label='Font size: 20',font=('Arial',20),command=lambda: self.set_new_font_size(20))
        self.fontsizesmenu.add_command(label='Font size: 22',font=('Arial',22),command=lambda: self.set_new_font_size(22))
        self.fontsizesmenu.add_command(label='Font size: 24',font=('Arial',24),command=lambda: self.set_new_font_size(24))
        self.fontsizesmenu.add_command(label='Font size: 30',font=('Arial',30),command=lambda: self.set_new_font_size(30))
        self.fontsizesmenu.add_command(label='Font size: 36',font=('Arial',36),command=lambda: self.set_new_font_size(36))
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
        self.textbox.pack(padx=10,pady=5,expand=True,fill="both")

        self.root.after(0, self.check_state)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def draw_space(self):
        if self.draw_space_checked.get() == 1:
            self.startx, self.starty = 0, 0
            self.endx, self.endy = 0, 0
            self.draw_space = tk.Canvas(self.root)
            self.draw_space.pack(padx=10,pady=10)
            self.draw_space.bind('<Button>', self.get_click)
            self.draw_space.bind('<ButtonRelease>', self.release_click)
        else:
            self.draw_space.pack_forget()

    def get_click(self,event):
        self.startx = event.x
        self.starty = event.y

    def release_click(self,event):
        self.endx = event.x
        self.endy = event.y
        self.draw_space.create_line(self.startx, self.starty, self.endx, self.endy, fill='blue')

    def check_state(self):
        if self.char_count_checked.get() == 1:
          self.character_count()
        else:
            self.char_count_var.set("Character count: Disabled")
        self.root.after(2200,self.check_state)

    def character_count(self):
        text = self.textbox.get('1.0',tk.END)
        length = len(text) - 1
        status = "Character count: " + str(length)
        self.char_count_var.set(status)
                   
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
    
    def open_file(self):
        open_file_path = filedialog.askopenfilename(
            title="Select a Text File", filetypes=[("Text files", "*.txt")])
        if open_file_path:
            with open(open_file_path, 'r') as file:
                content = file.read()
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, content)

    def save_all_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.textbox.get('1.0',tk.END))
    
    def paste_from_clipboard(self):
        to_paste = self.root.clipboard_get()
        self.textbox.insert(tk.INSERT,to_paste)
    
    def set_new_font(self,font):
        self.current_font = font
        self.textbox.configure(font=(self.current_font,self.font_size))
    
    def set_new_font_size(self,size):
        self.font_size = size
        self.textbox.configure(font=(self.current_font,self.font_size))

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
