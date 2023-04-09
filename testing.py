import tkinter as tk
from tkinter import messagebox

# root = tk.Tk()
# root.geometry("800x500")
# root.title("my first gui")

# label = tk.Label(root, text="Hello World", font=('Arial', 18))
# label.pack(padx=20, pady=20)

# textbox = tk.Text(root, height=3,  font=('Arial', 16))
# textbox.pack(padx=10)

# buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# buttonframe.columnconfigure(2, weight=1)

# btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

# btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

# btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18))
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

# btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18))
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

# btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

# btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18))
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

# buttonframe.pack(fill='x')

# anotherbtn = tk.Button(root, text='test')
# anotherbtn.place(x=200, y=200, height=100, width=100)


# root.mainloop()

class mygui:
    
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)
        

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show message", command=self.show_message)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="your message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='Show message box', font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))  
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))

    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            print('hello')

    def closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
mygui()