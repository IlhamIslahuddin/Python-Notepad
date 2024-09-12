##NOTE: PLEASE ALLOW 5 SECONDS TO LOAD BEFORE RUNNING

import tkinter as tk
from tkinter import messagebox, filedialog, PhotoImage, INSERT
import random
import string

class MyNotepad:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x800")
        self.root.minsize(150,150)
        self.root.title("My Notepad")
        self.root.configure(bg='lightblue')
        self.char_count = tk.Frame(self.root,bd=1,relief='sunken')
        self.char_count.pack(side='bottom',fill='x')
        self.char_count_var = tk.StringVar()
        self.char_count_checked = tk.IntVar()
        self.draw_space_var = tk.StringVar()
        self.draw_space_checked = tk.IntVar()
        self.post_it_var = tk.StringVar()
        self.post_it_checked = tk.IntVar()
        self.char_count_label = tk.Label(self.char_count, textvariable=self.char_count_var, anchor='w',padx=5,pady=5, font=('Arial',12,'italic'))
        self.char_count_label.pack(fill='x')
        #default font settings
        self.current_font = 'Arial'
        self.font_size = 14
        self.font_weight = 'normal'
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.actionmenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.fontmenu = tk.Menu(self.menubar,tearoff=0, font=('Arial',12))
        self.fontsmenu = tk.Menu(self.fontmenu,tearoff=0, font=('Arial',12))
        self.fontsizesmenu = tk.Menu(self.fontmenu,tearoff=0, font=('Arial',12))
        self.fontweightmenu = tk.Menu(self.fontmenu,tearoff=0, font=('Arial',12))
        self.settingsmenu = tk.Menu(self.menubar, tearoff=0, font=('Arial',12))
        self.backgroundmenu = tk.Menu(self.settingsmenu, tearoff=0, font=('Arial',12))
        self.fontcolourmenu = tk.Menu(self.settingsmenu,tearoff=0, font=('Arial',12))
        self.fontalignmentmenu = tk.Menu(self.settingsmenu,tearoff=0, font=('Arial',12))
        self.fontmenu.add_cascade(menu=self.fontsizesmenu, label="Font Sizes")
        self.fontmenu.add_cascade(menu=self.fontweightmenu, label="Font Weights")
        self.fontmenu.add_cascade(menu=self.fontsmenu, label="Fonts")
        self.settingsmenu.add_cascade(menu=self.backgroundmenu,label="Change Background Colour")
        self.settingsmenu.add_cascade(menu=self.fontcolourmenu,label="Change Font Colour")
        self.settingsmenu.add_cascade(menu=self.fontalignmentmenu,label="Change Text Alignment")
        self.filemenu.add_command(label="Open File", command=self.open_file, accelerator="Ctrl O")
        self.filemenu.add_command(label="Save As...", command=self.save_as_text_file, accelerator="Ctrl S")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Add PNG Image", command=self.add_image)
        self.filemenu.add_command(label="Close Window", command=self.on_closing, accelerator="Alt F4")
        self.actionmenu.add_command(label="Copy to Clipboard", command=self.save_all_to_clipboard)
        self.actionmenu.add_command(label="Paste from Clipboard", command=self.paste_from_clipboard, accelerator="Ctrl V")
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label="Undo",command=self.undo, accelerator="Ctrl Z")
        self.actionmenu.add_command(label="Redo",command=self.redo, accelerator="Ctrl Y")
        self.actionmenu.add_command(label="Clear Notepad", command=self.clear, accelerator="Ctrl |")
        self.actionmenu.add_command(label="Highlight", command= self.highlight, accelerator="Ctrl {")
        self.actionmenu.add_command(label="Remove Highlight", command= self.remove_highlight, accelerator="Ctrl }")
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label="Set all text to lowercase", command=self.set_to_lowercase)
        self.actionmenu.add_command(label="Set all text to UPPERCASE", command=self.set_all_to_uppercase)
        self.settingsmenu.add_checkbutton(label="Show Character Count", command=self.character_count,variable=self.char_count_checked)
        self.settingsmenu.add_checkbutton(label="Add Canvas", command=self.create_draw_space,variable=self.draw_space_checked)
        self.settingsmenu.add_checkbutton(label="Add Checklist", command=self.create_post_it,variable=self.post_it_checked)
        self.backgroundmenu.add_command(label="Light Blue", command=lambda: self.change_background("lightblue"))
        self.backgroundmenu.add_command(label="Light Yellow", command=lambda: self.change_background("lightyellow"))
        self.backgroundmenu.add_command(label="Red", command=lambda: self.change_background("red"))
        self.backgroundmenu.add_command(label="Light Green", command=lambda: self.change_background("lightgreen"))
        self.fontcolourmenu.add_command(label="Blue", command=lambda: self.change_font_colour("blue"))
        self.fontcolourmenu.add_command(label="Yellow", command=lambda: self.change_font_colour("yellow"))
        self.fontcolourmenu.add_command(label="Red", command=lambda: self.change_font_colour("red"))
        self.fontcolourmenu.add_command(label="Green", command=lambda: self.change_font_colour("green"))
        self.fontalignmentmenu.add_command(label="Left", command=lambda: self.change_alignment("left"))
        self.fontalignmentmenu.add_command(label="Center", command=lambda: self.change_alignment("center"))
        self.fontalignmentmenu.add_command(label="Right", command=lambda: self.change_alignment("right"))
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")
        self.menubar.add_cascade(menu=self.fontmenu, label='Fonts')
        self.menubar.add_cascade(menu=self.settingsmenu, label='Settings')
        self.fontsizesmenu.add_command(label='14',font=('Arial',14),command=lambda: self.set_new_font_size(14))
        self.fontsizesmenu.add_command(label='16',font=('Arial',16),command=lambda: self.set_new_font_size(16))
        self.fontsizesmenu.add_command(label='18',font=('Arial',18),command=lambda: self.set_new_font_size(18))
        self.fontsizesmenu.add_command(label='20',font=('Arial',20),command=lambda: self.set_new_font_size(20))
        self.fontsizesmenu.add_command(label='22',font=('Arial',22),command=lambda: self.set_new_font_size(22))
        self.fontsizesmenu.add_command(label='24',font=('Arial',24),command=lambda: self.set_new_font_size(24))
        self.fontsizesmenu.add_command(label='26',font=('Arial',26),command=lambda: self.set_new_font_size(26))
        self.fontsizesmenu.add_command(label='28',font=('Arial',28),command=lambda: self.set_new_font_size(28))
        self.fontsizesmenu.add_command(label='30',font=('Arial',30),command=lambda: self.set_new_font_size(30))
        self.fontweightmenu.add_command(label='Normal',font=('Arial',12, 'normal'),command=lambda: self.set_new_font_weight('normal'))
        self.fontweightmenu.add_command(label='Italic',font=('Arial',12, 'italic'),command=lambda: self.set_new_font_weight('italic'))
        self.fontweightmenu.add_command(label='Bold',font=('Arial',12, 'bold'),command=lambda: self.set_new_font_weight('bold'))
        self.fontweightmenu.add_command(label='Bold + Italic',font=('Arial',12, 'bold italic'),command=lambda: self.set_new_font_weight('bold italic'))
        self.fontweightmenu.add_command(label='Underline',font=('Arial',12, 'underline'),command=lambda: self.set_new_font_weight('underline'))
        self.fontweightmenu.add_command(label='Underline + Bold',font=('Arial',12, 'underline bold'),command=lambda: self.set_new_font_weight('underline bold'))
        self.fontweightmenu.add_command(label='Underline + Italic',font=('Arial',12, 'underline italic'),command=lambda: self.set_new_font_weight('underline italic'))
        self.fontweightmenu.add_command(label='Underline + Bold + Italic',font=('Arial',12, 'underline bold italic'),command=lambda: self.set_new_font_weight('underline bold italic'))
        self.fontsmenu.add_command(label='Arial',font=('Arial',12),command=lambda: self.set_new_font('Arial'))
        self.fontsmenu.add_command(label='Courier New',font=('Courier New',12),command=lambda: self.set_new_font('Courier New'))
        self.fontsmenu.add_command(label='Comic Sans MS',font=('Comic Sans MS',12),command=lambda: self.set_new_font('Comic Sans MS'))
        self.fontsmenu.add_command(label='Times New Roman',font=('Times New Roman',12),command=lambda: self.set_new_font('Times New Roman'))
        self.fontsmenu.add_command(label='Impact',font=('Impact',12),command=lambda: self.set_new_font('Impact'))
        self.fontsmenu.add_command(label='MS Sans Serif',font=('MS Sans Serif',12),command=lambda: self.set_new_font('MS Sans Serif'))
        self.fontsmenu.add_command(label='Roman',font=('Roman',12),command=lambda: self.set_new_font('Roman'))
        self.fontsmenu.add_command(label='System',font=('System',12),command=lambda: self.set_new_font('System'))
        self.root.config(menu=self.menubar)
        self.textbox = tk.Text(self.root,font=(self.current_font,self.font_size,self.font_weight), selectbackground="lightgreen", selectforeground="black", undo=True)
        self.textbox.pack(padx=10,pady=10,expand=True,fill="both")
        #shortcuts
        self.textbox.bind("<Control-{>",self.highlight)
        self.textbox.bind("<Control-}>",self.remove_highlight)
        self.textbox.bind("<Control-|>",self.clear)
        self.textbox.bind("<Control-o>",self.open_file)
        self.textbox.bind("<Control-s>",self.save_as_text_file)
        self.root.after(0, self.check_state)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    def undo(self):
        try:
            self.textbox.edit_undo()
        except:
            pass
    def redo(self):
        try:
            self.textbox.edit_redo()
        except:
            pass
    def add_image(self):
        image_file_path = filedialog.askopenfilename(
            title="Select a PNG File", filetypes=[("Image files", "*.png")])
        if image_file_path:
            global image
            cursor_pos = self.textbox.index(INSERT)
            image = PhotoImage(file=image_file_path)
            self.textbox.image_create(cursor_pos, image=image)
    def change_alignment(self,alignment):
            self.textbox.tag_config(alignment,justify=alignment)
            self.textbox.tag_add(alignment,'1.0',tk.END)
    def change_background(self, colour):
        self.root.configure(bg=colour)
    def change_font_colour(self, colour):
        self.textbox.configure(fg=colour)
    def highlight(self,event=""):
        #event = "" sets default value for event so it is not always needed as an arg
        try:
            start = self.textbox.index("sel.first")
            end = self.textbox.index("sel.last")
            self.textbox.tag_add("sel_txt",start,end)
            self.textbox.tag_config('sel_txt', background='yellow',foreground='black')
        except:
            messagebox.showwarning(message="No text was selected for highlighting.")
    def remove_highlight(self,event=""):
        try:
            start = self.textbox.index("sel.first")
            end = self.textbox.index("sel.last")
            #used to get selected text
            self.textbox.tag_remove("sel_txt",start,end)
        except:
            messagebox.showwarning(message="No text was selected to remove highlighting.")
    def create_draw_space(self):
        if self.draw_space_checked.get() == 1:
            self.startx, self.starty = 0, 0
            self.endx, self.endy = 0, 0
            self.draw_space_window = tk.Toplevel(self.root)
            self.draw_space_window.title("Draw Space")
            self.draw_space = tk.Canvas(self.draw_space_window, bg='white')
            self.draw_space.pack(padx=10,pady=10,fill="both")
            self.brush_size = 3
            self.draw_space.bind('<B1-Motion>', self.draw)
            self.draw_space.bind('<Button-3>', self.erase)
        else:
            self.draw_space_window.destroy()
    def create_post_it(self):
        if self.post_it_checked.get() == 1:
            self.post_it_window = tk.Toplevel(self.root)
            self.post_it_window.title("Checklist")
            self.post_it_window.geometry("250x200")
            box_frame = tk.Frame(self.post_it_window)
            line1var = tk.IntVar
            line1 = tk.Checkbutton(box_frame, variable=line1var, onvalue=1, offvalue=0,text="Task 1")
            line1.pack(fill="x",pady=10,side="top")
            line2var = tk.IntVar
            line2 = tk.Checkbutton(box_frame, variable=line2var, onvalue=1, offvalue=0,text="Task 2")
            line2.pack(fill="x",pady=10,side="top")
            line3var = tk.IntVar
            line3 = tk.Checkbutton(box_frame, variable=line3var, onvalue=1, offvalue=0,text="Task 3")
            line3.pack(fill="x",pady=10,side="top")
            line4var = tk.IntVar
            line4 = tk.Checkbutton(box_frame, variable=line4var, onvalue=1, offvalue=0,text="Task 4")
            line4.pack(fill="x",pady=10,side="top")
            box_frame.pack(side="left",padx=10,pady=10)
        else:
            self.post_it_window.destroy()
    def draw(self, event):
        x = event.x
        y = event.y
        self.draw_space.create_oval((x-self.brush_size/2,y-self.brush_size/2,x+self.brush_size/2,y+self.brush_size/2), fill='black')
    def erase(self, event):
        self.draw_space.delete('all')
    def check_state(self):
        if self.char_count_checked.get() == 1:
          self.character_count()
        else:
            self.char_count_var.set("Character count: Disabled")
        self.root.after(2300,self.check_state)
    def character_count(self):
        text = self.textbox.get('1.0',tk.END)
        length = len(text) - 1
        status = "Character count: " + str(length)
        self.char_count_var.set(status)
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit the program? All data will be lost."):
            self.root.destroy()
    def clear(self,event=""):
        self.textbox.delete('1.0', tk.END)
    def save_as_text_file(self,event=""):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                text_content = self.textbox.get("1.0", tk.END)
                file.write(text_content)
    def open_file(self,event=""):
        open_file_path = filedialog.askopenfilename(
            title="Select a Text File", filetypes=[("Text files", "*.txt")])
        if open_file_path:
            file_title = open_file_path
            self.root.title(f"My Notepad - {file_title}")
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
        try:
            font_code = ''.join(random.choices(string.ascii_letters, k=6))
            start = self.textbox.index("sel.first")
            end = self.textbox.index("sel.last")
            self.textbox.tag_remove(font_code,start,end)
            self.textbox.tag_add(font_code,start,end)
            self.textbox.tag_config(font_code, font=(font,self.font_size,self.font_weight))
        except:
            self.current_font = font
            self.textbox.configure(font=(self.current_font,self.font_size,self.font_weight))
    def set_new_font_size(self,size):
        try:
            size_code = ''.join(random.choices(string.ascii_letters, k=6))
            start = self.textbox.index("sel.first")
            end = self.textbox.index("sel.last")
            self.textbox.tag_remove(size_code,start,end)
            self.textbox.tag_add(size_code,start,end)
            self.textbox.tag_config(size_code, font=(self.current_font,size,self.font_weight))
        except:
            self.font_size = size
            self.textbox.configure(font=(self.current_font,self.font_size,self.font_weight))
    def set_new_font_weight(self,weight):
        try:
            weight_code = ''.join(random.choices(string.ascii_letters, k=6))
            start = self.textbox.index("sel.first")
            end = self.textbox.index("sel.last")
            self.textbox.tag_remove(weight_code,start,end)
            self.textbox.tag_add(weight_code,start,end)
            self.textbox.tag_config(weight_code, font=(self.current_font,self.font_size,weight))
        except:
            self.font_weight = weight
            self.textbox.configure(font=(self.current_font,self.font_size,self.font_weight))
    def set_to_lowercase(self):
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

##NOTE: PLEASE ALLOW 5 SECONDS TO LOAD BEFORE RUNNING
