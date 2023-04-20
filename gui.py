from tkinter import *
from PIL import ImageTk, Image


class gui:
    def __init__(self) -> None:
        #main window
        self.root = Tk()
        self.root.geometry("1200x600")
        self.root.resizable(0, 0)
        self.root.title("IslamicLingo")
        
        #favicon
        ico = Image.open('image/mosque.png')
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo) 

        #startframe
        self.startframe = Frame(self.root)
       # self.startframe.pack(pady=50)

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

    # -----------------------------------------------------------------------------------------------------
    # Question 1 frame
        self.qframe = Frame(self.root)
        self.qframe.pack(padx=30, pady=30)

        # Home button
        self.homebutton = Button(self.qframe, text="Home", padx=20, pady=20).grid(row=0, column=0)

        #spacer
        self.spacer = Label(self.qframe,text="                                             ").grid(row=0, column=1)
        
        #logo
        self.endlogo = ImageTk.PhotoImage(Image.open("image/mosque.png").resize((89, 87)))
        self.endtitle = ImageTk.PhotoImage(Image.open("image/islamiclingo.png").resize((233, 43)))

        self.qlogoframe = Frame(self.qframe)
        self.qlogoframe.grid(row=0, column=2)

        self.endlogolabel = Label(self.qlogoframe, image=self.endlogo)
        self.endtitlelabel = Label(self.qlogoframe, image=self.endtitle)
        self.endlogolabel.pack(side=LEFT)
        self.endtitlelabel.pack(side=LEFT)

        # question
        self.middleqframe = Frame(self.qframe)
        self.middleqframe.grid(row=1, column=1)

        self.instruction = Label(self.middleqframe, text="Write this in English", font=("Arial", '15', 'bold')).pack()
        self.question = Label(self.middleqframe, text="الأرز والماء", font=("", "70"), width=13).pack()

        #choice
        self.choiceframe = Frame(self.middleqframe)
        self.choiceframe.pack(pady=70)

        self.choice1 = Button(self.choiceframe, text="Rice", width=10).pack(side=LEFT, padx=8)
        self.choice2 = Button(self.choiceframe, text="Juice", width=10).pack(side=LEFT, padx=8)
        self.choice3 = Button(self.choiceframe, text="Door", width=10).pack(side=LEFT, padx=8)
        self.choice4 = Button(self.choiceframe, text="Road", width=10).pack(side=LEFT, padx=8)
        self.choice5 = Button(self.choiceframe, text="Eat", width=10).pack(side=LEFT, padx=8)
        self.choice6 = Button(self.choiceframe, text="Drink", width=10).pack(side=LEFT, padx=8)
        self.choice7 = Button(self.choiceframe, text="Walk", width=10).pack(side=LEFT, padx=8)

        # navigation 
        self.navframe = Frame(self.qframe, bg="green", padx=30, pady=70)
        self.navframe.grid(row=1, column=2)

        self.navlabel = Label(self.navframe, text="Questions", font=("Arial", "20"), pady=20, bg='green').pack()

        self.navbuttonframe = Frame(self.navframe, bg="green")
        self.navbuttonframe.pack()

        self.q1nav = Button(self.navbuttonframe, text="1", padx=10, pady=10).pack(side=RIGHT, padx=10)
        self.q2nav = Button(self.navbuttonframe, text="2", padx=10, pady=10).pack(side=RIGHT, padx=10)
        self.q3nav = Button(self.navbuttonframe, text="3", padx=10, pady=10).pack(side=RIGHT, padx=10)
        self.q4nav = Button(self.navbuttonframe, text="4", padx=10, pady=10).pack(side=RIGHT, padx=10)
        self.q5nav = Button(self.navbuttonframe, text="5", padx=10, pady=10).pack(side=RIGHT, padx=10)

        #finish button
        self.finbutton = Button(self.navframe, text="FINISH", padx=20, pady=10).pack(pady=30)

        #back and forward button
        self.backforwardframe = Frame(self.navframe, bg='green')
        self.backforwardframe.pack()

        self.backbutton = Button(self.backforwardframe, text="BACK", padx=20, pady=10).pack(side=LEFT, padx=20)
        self.forwardbutton = Button(self.backforwardframe, text="FORWARD", padx=20, pady=10).pack(padx=20)


        self.root.mainloop()

gui()

