from tkinter import *
from PIL import ImageTk, Image


class gui:
    def __init__(self) -> None:
        #main window
        self.root = Tk()
        self.root.geometry("1200x600")
        self.root.resizable(0, 0)
        self.root.title("IslamicLingo")
        self.CURRENTFRAME = None
        
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
        def start():
            self.CURRENTFRAME = self.root.children['!frame']
            self.CURRENTFRAME.pack_forget()
            self.CURRENTFRAME = self.qframe
            self.CURRENTFRAME.pack(padx=30, pady=30)
        self.startbutton = Button(self.startframe, text="GET STARTED", width=50, height=3, bg="#5ACC05", fg="#fff", font=("Helvetica", 15), command=start).pack()

        #--------------------------------------------------------------------------------------------------------------------------
        # endframe
        self.endframe = Frame(self.root)

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
    # Question frame
        self.qframe = Frame(self.root)

        self.currentq = None
        

        # Home button
        def returnhome():
            self.CURRENTFRAME = self.root.children['!frame3']
            self.CURRENTFRAME.pack_forget()
            self.startframe.pack(pady=50)
        self.homebutton = Button(self.qframe, text="Home", padx=20, pady=20, command=returnhome).grid(row=0, column=0)

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

        # navigation 
        self.navframe = Frame(self.qframe, bg="green", padx=30, pady=70)
        self.navframe.grid(row=1, column=2)

        self.navlabel = Label(self.navframe, text="Questions", font=("Arial", "20"), pady=20, bg='green').pack()

        self.navbuttonframe = Frame(self.navframe, bg="green")
        self.navbuttonframe.pack()
        
        
        print(self.CURRENTFRAME)
        def displayq1():
            self.middleq2frame.grid_forget()
            self.middleq3frame.grid_forget()
            self.middleq4frame.grid_forget()
            self.middleq5frame.grid_forget()
            self.currentq = 1
            self.middleq1frame.grid(row=1, column=1)
        def displayq2():
            self.middleq1frame.grid_forget()
            self.middleq3frame.grid_forget()
            self.middleq4frame.grid_forget()
            self.middleq5frame.grid_forget()
            self.currentq = 2
            self.middleq2frame.grid(row=1, column=1)
        def displayq3():
            self.middleq1frame.grid_forget()
            self.middleq2frame.grid_forget()
            self.middleq4frame.grid_forget()
            self.middleq5frame.grid_forget()
            self.currentq = 3
            self.middleq3frame.grid(row=1, column=1)
        def displayq4():
            self.middleq1frame.grid_forget()
            self.middleq2frame.grid_forget()
            self.middleq3frame.grid_forget()
            self.middleq5frame.grid_forget()
            self.currentq = 4
            self.middleq4frame.grid(row=1, column=1)
        def displayq5():
            self.middleq1frame.grid_forget()
            self.middleq2frame.grid_forget()
            self.middleq3frame.grid_forget()
            self.middleq4frame.grid_forget()
            self.currentq = 5
            self.middleq5frame.grid(row=1, column=1)


        self.q1nav = Button(self.navbuttonframe, text="1", padx=10, pady=10, command=displayq1).pack(side=RIGHT, padx=10)
        self.q2nav = Button(self.navbuttonframe, text="2", padx=10, pady=10, command=displayq2).pack(side=RIGHT, padx=10)
        self.q3nav = Button(self.navbuttonframe, text="3", padx=10, pady=10, command=displayq3).pack(side=RIGHT, padx=10)
        self.q4nav = Button(self.navbuttonframe, text="4", padx=10, pady=10, command=displayq4).pack(side=RIGHT, padx=10)
        self.q5nav = Button(self.navbuttonframe, text="5", padx=10, pady=10, command=displayq5).pack(side=RIGHT, padx=10)

        #submit button
        def choice(num):
            if self.currentq == 1:
                self.q1choicearr.append(num)
                print(self.q1choicearr)
            elif self.currentq == 2:
                self.q2choicearr.append(num)
            elif self.currentq == 3:
                self.q3choicearr.append(num)
            elif self.currentq == 4:
                self.q4choicearr.append(num)
            elif self.currentq == 5:
                self.q5choicearr.append(num)
                

        def submitq(currentq):
            if currentq == 1:
                if self.q1choicearr == [1, 4, 6]:
                    print(True)
                else:
                    print(False)
            elif currentq == 2:
                if self.q2choicearr == [4, 6, 7]:
                    print(True)
                else:
                    print(False)
            elif currentq == 3:
                if self.q3choicearr == [1, 5, 6]:
                    print(True)
                else:
                    print(False)
            elif currentq == 4:
                if self.q4choicearr == [6, 4, 3]:
                    print(True)
                else:
                    print(False)
            elif currentq == 5:
                if self.q5choicearr == [5, 1, 4]:
                    print(True)
                else:
                    print(False)
        self.submitqbutton = Button(self.navframe, text="SUBMIT QUESTION", padx=26, pady=10, command=lambda: submitq(self.currentq)).pack(pady=30)

        #finish button
        def finish():
            self.CURRENTFRAME = self.root.children['!frame3']
            self.CURRENTFRAME.pack_forget()
            self.CURRENTFRAME = self.endframe
            self.CURRENTFRAME.pack(padx=50)
        self.finbutton = Button(self.navframe, text="FINISH QUIZ", padx=20, pady=10, command=finish).pack(pady=30)

        #-----------------------------------------------------------------------------------------------------
        # question 1
        self.middleq1frame = Frame(self.qframe)
        self.middleq1frame.grid(row=1, column=1)
        self.CURRENTFRAME = self.middleq1frame
        
        self.instruction = Label(self.middleq1frame, text="Write this in English", font=("Arial", '15', 'bold')).pack()
        self.question = Label(self.middleq1frame, text="الأرز والماء", font=("", "70"), width=13).pack()

        #choice
        self.q1choiceframe = Frame(self.middleq1frame)
        self.q1choiceframe.pack(pady=70)

        self.q1choicearr = []

        self.q1choice1 = Button(self.q1choiceframe, text="Rice", width=10, command=lambda: choice(1)).pack(side=LEFT, padx=8)
        self.q1choice2 = Button(self.q1choiceframe, text="Juice", width=10, command=lambda: choice(2)).pack(side=LEFT, padx=8)
        self.q1choice3 = Button(self.q1choiceframe, text="Door", width=10, command=lambda: choice(3)).pack(side=LEFT, padx=8)
        self.q1choice4 = Button(self.q1choiceframe, text="and", width=10, command=lambda: choice(4)).pack(side=LEFT, padx=8)
        self.q1choice5 = Button(self.q1choiceframe, text="Eat", width=10, command=lambda: choice(5)).pack(side=LEFT, padx=8)
        self.q1choice6 = Button(self.q1choiceframe, text="Water", width=10, command=lambda: choice(6)).pack(side=LEFT, padx=8)
        self.q1choice7 = Button(self.q1choiceframe, text="Walk", width=10, command=lambda: choice(7)).pack(side=LEFT, padx=8)



    #---------------------------------------------------------------------------------------------------------
    # question 2 
        self.middleq2frame = Frame(self.qframe)
        
        self.instruction = Label(self.middleq2frame, text="Write this in English", font=("Arial", '15', 'bold')).pack()
        self.question = Label(self.middleq2frame, text="القط والكلب", font=("", "70"), width=13).pack()

        #choice
        self.q2choiceframe = Frame(self.middleq2frame)
        self.q2choiceframe.pack(pady=70)

        self.q2choicearr = []

        self.q2choice1 = Button(self.q2choiceframe, text="Lizard", width=10, command=lambda: choice(1)).pack(side=LEFT, padx=8)
        self.q2choice2 = Button(self.q2choiceframe, text="is", width=10, command=lambda: choice(2)).pack(side=LEFT, padx=8)
        self.q2choice3 = Button(self.q2choiceframe, text="Food", width=10, command=lambda: choice(3)).pack(side=LEFT, padx=8)
        self.q2choice4 = Button(self.q2choiceframe, text="Cat", width=10, command=lambda: choice(4)).pack(side=LEFT, padx=8)
        self.q2choice5 = Button(self.q2choiceframe, text="People", width=10, command=lambda: choice(5)).pack(side=LEFT, padx=8)
        self.q2choice6 = Button(self.q2choiceframe, text="and", width=10, command=lambda: choice(6)).pack(side=LEFT, padx=8)
        self.q2choice7 = Button(self.q2choiceframe, text="Dog", width=10, command=lambda: choice(7)).pack(side=LEFT, padx=8)

        #---------------------------------------------------------------------------------------------------------
    # question 3
        self.middleq3frame = Frame(self.qframe)
        
        self.instruction = Label(self.middleq3frame, text="Write this in English", font=("Arial", '15', 'bold')).pack()
        self.question = Label(self.middleq3frame, text="الشمس والقمر", font=("", "70"), width=13).pack()

        #choice
        self.q3choiceframe = Frame(self.middleq3frame)
        self.q3choiceframe.pack(pady=70)

        self.q3choicearr = []

        self.q3choice1 = Button(self.q3choiceframe, text="Sun", width=10, command=lambda: choice(1)).pack(side=LEFT, padx=8)
        self.q3choice2 = Button(self.q3choiceframe, text="The", width=10, command=lambda: choice(2)).pack(side=LEFT, padx=8)
        self.q3choice3 = Button(self.q3choiceframe, text="Eating", width=10, command=lambda: choice(3)).pack(side=LEFT, padx=8)
        self.q3choice4 = Button(self.q3choiceframe, text="Beautiful", width=10, command=lambda: choice(4)).pack(side=LEFT, padx=8)
        self.q3choice5 = Button(self.q3choiceframe, text="and", width=10, command=lambda: choice(5)).pack(side=LEFT, padx=8)
        self.q3choice6 = Button(self.q3choiceframe, text="Moon", width=10, command=lambda: choice(6)).pack(side=LEFT, padx=8)
        self.q3choice7 = Button(self.q3choiceframe, text="Sunny", width=10, command=lambda: choice(7)).pack(side=LEFT, padx=8)

        #---------------------------------------------------------------------------------------------------------
    # question 4
        self.middleq4frame = Frame(self.qframe)
        
        self.instruction = Label(self.middleq4frame, text="Write this in English", font=("Arial", '15', 'bold')).pack()
        self.question = Label(self.middleq4frame, text="رجل وامرأة", font=("", "70"), width=13).pack()

        #choice
        self.q4choiceframe = Frame(self.middleq4frame)
        self.q4choiceframe.pack(pady=70)

        self.q4choicearr = []

        self.q4choice1 = Button(self.q4choiceframe, text="Kid", width=10, command=lambda: choice(1)).pack(side=LEFT, padx=8)
        self.q4choice2 = Button(self.q4choiceframe, text="playing", width=10, command=lambda: choice(2)).pack(side=LEFT, padx=8)
        self.q4choice3 = Button(self.q4choiceframe, text="Woman", width=10, command=lambda: choice(3)).pack(side=LEFT, padx=8)
        self.q4choice4 = Button(self.q4choiceframe, text="and", width=10, command=lambda: choice(4)).pack(side=LEFT, padx=8)
        self.q4choice5 = Button(self.q4choiceframe, text="Elderly", width=10, command=lambda: choice(5)).pack(side=LEFT, padx=8)
        self.q4choice6 = Button(self.q4choiceframe, text="Man", width=10, command=lambda: choice(6)).pack(side=LEFT, padx=8)
        self.q4choice7 = Button(self.q4choiceframe, text="is", width=10, command=lambda: choice(7)).pack(side=LEFT, padx=8)

        #---------------------------------------------------------------------------------------------------------
    # question 5 
        self.middleq5frame = Frame(self.qframe)
        
        self.instruction = Label(self.middleq5frame, text="Write this in English", font=("Arial", '15', 'bold')).pack()
        self.question = Label(self.middleq5frame, text="انا نائم", font=("", "70"), width=13).pack()

        #choice
        self.q5choiceframe = Frame(self.middleq5frame)
        self.q5choiceframe.pack(pady=70)

        self.q5choicearr = []

        self.q5choice1 = Button(self.q5choiceframe, text="am", width=10, command=lambda: choice(1)).pack(side=LEFT, padx=8)
        self.q5choice2 = Button(self.q5choiceframe, text="Awake", width=10, command=lambda: choice(2)).pack(side=LEFT, padx=8)
        self.q5choice3 = Button(self.q5choiceframe, text="Hungry", width=10, command=lambda: choice(3)).pack(side=LEFT, padx=8)
        self.q5choice4 = Button(self.q5choiceframe, text="Sleepy", width=10, command=lambda: choice(4)).pack(side=LEFT, padx=8)
        self.q5choice5 = Button(self.q5choiceframe, text="I", width=10, command=lambda: choice(5)).pack(side=LEFT, padx=8)
        self.q5choice6 = Button(self.q5choiceframe, text="Walking", width=10, command=lambda: choice(6)).pack(side=LEFT, padx=8)
        self.q5choice7 = Button(self.q5choiceframe, text="Eating", width=10, command=lambda: choice(7)).pack(side=LEFT, padx=8)

        







        self.root.mainloop()

gui()

