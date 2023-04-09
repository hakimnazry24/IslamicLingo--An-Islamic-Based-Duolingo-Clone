from tkinter import *
from PIL import ImageTk, Image


class gui:
    def __init__(self) -> None:
        #main window
        self.root = Tk()
        self.root.geometry("1400x800")
        self.root.resizable(0, 0)
        self.root.title("IslamicLingo")
        
        #favicon
        ico = Image.open('image/mosque.png')
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo) 

        #frame
        self.frame = Frame(self.root)
        self.frame.pack(pady=50)

        #logo and title
        self.logo = ImageTk.PhotoImage(Image.open("image/mosque.png").resize((198, 192)))
        self.title = ImageTk.PhotoImage(Image.open("image/islamiclingo.png").resize((517, 95)))

        self.logolabel = Label(self.frame, image=self.logo)
        self.titlelabel = Label(self.frame, image=self.title)
        self.logolabel.pack(pady=20)
        self.titlelabel.pack(pady=20)

        #title subtext
        self.titlesubtext = Label(self.frame, text="Learn our beautiful Arabic language interactively without hassle.", font=("Helvetica", 12))
        self.titlesubtext.pack(pady=20)

        #start button
        self.startbutton = Button(self.frame, text="GET STARTED", width=50, height=3, bg="#5ACC05", fg="#fff", font=("Helvetica", 15))
        self.startbutton.pack()


        self.root.mainloop()

gui()

