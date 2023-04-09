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

        #startframe
        self.startframe = Frame(self.root)
        self.startframe.pack(pady=50)

        #logo and title
        self.startlogo = ImageTk.PhotoImage(Image.open("image/mosque.png").resize((198, 192)))
        self.starttitle = ImageTk.PhotoImage(Image.open("image/islamiclingo.png").resize((517, 95)))

        self.startlogolabel = Label(self.startframe, image=self.startlogo)
        self.starttitlelabel = Label(self.startframe, image=self.starttitle)
        self.startlogolabel.pack(pady=20)
        self.starttitlelabel.pack(pady=20)

        #title subtext
        self.titlesubtext = Label(self.startframe, text="Learn our beautiful Arabic language interactively without hassle.", font=("Helvetica", 12))
        self.titlesubtext.pack(pady=20)

        #start button
        self.startbutton = Button(self.startframe, text="GET STARTED", width=50, height=3, bg="#5ACC05", fg="#fff", font=("Helvetica", 15))
        self.startbutton.pack()

        #--------------------------------------------------------------------------------------------------------------------------
        # endframe
        self.endframe = Frame(self.root)
        #self.endframe.pack(padx=50)

        #logo and title
        self.endlogo = ImageTk.PhotoImage(Image.open("image/mosque.png").resize((89, 87)))
        self.endtitle = ImageTk.PhotoImage(Image.open("image/islamiclingo.png").resize((233, 43)))

        self.endlogolabel = Label(self.endframe, image=self.endlogo)
        self.endtitlelabel = Label(self.endframe, image=self.endtitle)
        self.endlogolabel.pack(pady=10)
        self.endtitlelabel.pack()

        #congratulations label
        self.congrats = Label(self.endframe, text="Congratulations!\n You finished the game.", font=("Helvetica", 40, "bold"))
        self.congrats.pack(pady=20)

        #hadith label
        self.firstsubtext = Label(self.endframe, text="The Second Caliph Umar b.al-Khattab (R.A) always emphasized:", font=("Helvetica", 24))
        self.hadith = Label(self.endframe, text="\"تَعَلّمُوا العربيّةَ فَإنّها مِن دِينِكُم\"", font=("Helvetica", 24))
        self.hadithmeaning = Label(self.endframe, text="(Learn the Arabic language as it is part of your Din)." , font=("Helvetica", 24, "bold"))
        self.hadithsource = Label(self.endframe, text="Al-Bayhaqi: Shu‘ub al-Iman, Vol. 2, p. 257.", font=("Helvetica", 24))

        self.firstsubtext.pack(pady=40)
        self.hadith.pack()
        self.hadithmeaning.pack()
        self.hadithsource.pack(pady=40)







        self.root.mainloop()

gui()

