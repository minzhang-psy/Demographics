'''
Title: Demographic
Author: Min Zhang

'''
application_title='demographic'
main_python_file='demographic.py'
import time
from tkinter import *
import csv
import os
from tkinter.messagebox import *
from tkinter import filedialog
from datetime import date




LARG_FONT = ("Arial", 25)
class TkDemo():
    def __init__(self, *args, **kwargs):
        #Set up window 
        window = Tk()
        window.title("Demographic")
        window.attributes('-fullscreen', True)
        #window.configure (background = "#9B9B9B")
        #Press Escape to close the window 
        window.bind ('<Escape>', lambda e: window.destroy())
        menubar=Menu(window)      
        window.config(menu=menubar)
        height = window.winfo_screenheight()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        width = window.winfo_screenwidth()

        title = Label(window, text="Demographics", font=LARG_FONT)
        title.pack()
        
        #This allow file choose window goes away 
        window.update()
        
        #Drop down menu for study list
        '''
        #read master study list 
        mastersheet = "/Users/mayrlab/Dropbox/finalized_experiments/Demographic/ExperimenterMasterSheet.csv"
        file = list(csv.reader(open(mastersheet)))

        self.study = StringVar()
        studyList = []
        
        for row in file:
            studyList.append(row[0])
        '''
        self.study = StringVar()
        studyList = os.listdir("/Users/mayrlab/Dropbox/finalized_experiments")
        popupMenu = OptionMenu(window, self.study, *studyList) 
        Label(window, text = 'Choose a study').place(x=width/2-70 ,y=30)
        popupMenu.place(x=width/2+50,y=30)

        
        #ID
        frame = Frame(window)
        frame.pack(padx=50, pady=10, anchor="w")
        labelID = Label(frame, text="ID  ")
        labelID.grid(row=1,column=0)
        self.ID = StringVar()
        entryID = Entry(frame,textvariable=self.ID)
        entryID.grid(row=1,column=1)

        
        
        #age
        frame_1 = Frame(window)
        frame_1.pack(fill=X, padx=50, pady=10, anchor="w")
        labelAge = Label(frame_1, text="Age")
        labelAge.grid(row=1,column=0)
        self.Age = StringVar()
        entryage = Entry(frame_1,textvariable=self.Age)
        entryage.grid(row=1,column=1)

        #hand
        frame_hand = Frame(window)
        frame_hand.pack(fill=X, padx=50, pady=10, anchor="w")
        labelhand = Label(frame_hand,text="Which hand do you write with?")
        labelhand.grid(row=3,column=1)
        self.hand = StringVar()
        entryhand = Entry(frame_hand,textvariable=self.hand)
        entryhand.grid(row=3,column=2)

        #gender
        frame_2 = Frame(window)
        frame_2.pack(fill=X, padx=50, pady=10, anchor="w")
        label_2=Label(frame_2, text="Gender   ")
        label_2.grid(row = 1, column = 1)

        self.gender = StringVar()
        gender_male = Radiobutton(frame_2, text = "Male",
                                  variable = self.gender,
                                  value='Male')
        gender_male.grid(row=2, column=2, sticky="w")
        gender_female = Radiobutton(frame_2, text = "Female",
                                    variable = self.gender,
                                    value = 'Female')
        gender_female.grid(row = 3, column = 2, sticky="w")
        gender_other = Radiobutton(frame_2, text = "Other",
                                    variable = self.gender,
                                    value = 'other')
        gender_other.grid(row = 4, column = 2, sticky="w")
        gender_other = Radiobutton(frame_2, text = "Prefer not to answer",
                                    variable = self.gender,
                                    value = 'Prefer not to answer')
        gender_other.grid(row = 5, column = 2, sticky="w")

        #Race
        frame_3 = Frame(window)
        frame_3.pack(fill=X, padx=50, pady=10, anchor="w")
        label_3=Label(frame_3, text="Race      ")
        label_3.grid(row = 1, column = 1, sticky="w")

        self.race = StringVar()
        race1 = Radiobutton(frame_3, text = "American Indian or Alaska Native",
                                    variable = self.race,
                                    value = 'American Indian or Alaska Native')
        race1.grid(row = 2, column = 2, sticky="w")
        race2 = Radiobutton(frame_3, text = "Asian",
                                    variable = self.race,
                                    value = 'Asian')
        race2.grid(row = 3, column = 2, sticky="w")
        race3 = Radiobutton(frame_3, text = "Black or African American",
                                    variable = self.race,
                                    value = 'Black or African American')
        race3.grid(row = 4, column = 2, sticky="w")
        race4 = Radiobutton(frame_3, text = "Native Hawaiian or other Pacific Islander",
                                    variable = self.race,
                                    value = 'Native Hawaiian or other Pacific Islander')
        race4.grid(row = 5, column = 2, sticky="w")
        race5 = Radiobutton(frame_3, text = "White",
                                    variable = self.race,
                                    value = 'White')
        race5.grid(row = 6, column = 2, sticky="w")
        race6 = Radiobutton(frame_3, text = "More than one race",
                                    variable = self.race,
                                    value = 'More than one race')
        race6.grid(row = 7, column = 2, sticky="w")
        race7 = Radiobutton(frame_3, text = "Other",
                                    variable = self.race,
                                    value = 'Other')
        race7.grid(row = 8, column = 2, sticky="w")
        race8 = Radiobutton(frame_3, text = "Prefer not to answer",
                                    variable = self.race,
                                    value = 'Prefer not to answer')
        race8.grid(row = 9, column = 2, sticky="w")

        #Ethnicity
        frame_4 = Frame(window)
        frame_4.pack(fill=X, padx=50, pady=10, anchor="w")
        label_4=Label(frame_4, text="Ethnicity")
        label_4.grid(row = 1, column = 1, sticky="w")

        self.ethnicity = StringVar()
        ethnicity1 = Radiobutton(frame_4, text = "Hispanic or Latino",
                                    variable = self.ethnicity,
                                    value = 'Hispanic or Latino')
        ethnicity1.grid(row = 2, column = 2, sticky="w")

        ethnicity2 = Radiobutton(frame_4, text = "Not Hispanic or Latino",
                                    variable = self.ethnicity,
                                    value = 'Not Hispanic or Latino')
        ethnicity2.grid(row = 3, column = 2, sticky="w")

        ethnicity4 = Radiobutton(frame_4, text = "Prefer not to answer",
                                    variable = self.ethnicity,
                                    value = 'Prefer not to answe')
        ethnicity4.grid(row = 5, column = 2, sticky="w")
        
        #School year
        frame_5 = Frame(window)
        frame_5.pack(fill=X, padx=50, pady=10, anchor="w")
        label_5=Label(frame_5, text="If currently a college student")
        label_5.grid(row = 1, column = 1, sticky="w")

        self.year = StringVar()
        self.otheryear = StringVar()
        self.level = StringVar()
        labelyear=Label(frame_5,text="  Year in University:")
        labelyear.grid(row = 2, column = 1, sticky="w")
        
        Freshman = Radiobutton(frame_5, text = "Freshman     ",
                                    variable = self.year,
                                    value = 'Freshman')
        Freshman.grid(row = 2, column = 3, sticky="w")
        Sophomore = Radiobutton(frame_5, text = "Sophomore     ",
                                    variable = self.year,
                                    value = 'Sophomor')
        Sophomore.grid(row = 2, column = 4, sticky="w")
        Junior = Radiobutton(frame_5, text = "Junior     ",
                                    variable = self.year,
                                    value = 'Junior')
        Junior.grid(row = 2, column = 5, sticky="w")
        Senior = Radiobutton(frame_5, text = "Senior     ",
                                    variable = self.year,
                                    value = 'Senior')
        Senior.grid(row = 2, column = 6, sticky="w")
        SuperSenior = Radiobutton(frame_5, text = "Super Senior     ",
                                    variable = self.year,
                                    value = 'Super Senior     ')
        SuperSenior.grid(row = 2, column = 7, sticky="w")

        Other = Radiobutton(frame_5, text = "Other",
                                    variable = self.year,
                                    value = 'Other')
        Other.grid(row = 2, column = 8, sticky="w")
        
        
        entryyear = Entry(frame_5,textvariable=self.otheryear)
        entryyear.grid(row=2,column=9)
        

            
        frame_6 = Frame(window)
        frame_6.pack(fill=X, padx=50, anchor="w")
        
        label6=Label(frame_6, text="If NOT currently a college student")
        label6.grid(row = 1, column = 1, sticky="w")
        label6_1=Label(frame_6, text="   Level of Schooling Completed:")
        label6_1.grid(row = 2, column = 1, sticky="w")
        nohigh = Radiobutton(frame_6, text = "Some high school     ",
                                    variable = self.level,
                                    value = 'Some high school')
        nohigh.grid(row = 2, column = 3, sticky="w")
        high = Radiobutton(frame_6, text = "High school     ",
                                    variable = self.level,
                                    value = 'High school')
        high.grid(row = 2, column = 4, sticky="w")
        somecollege = Radiobutton(frame_6, text = "Some college     ",
                                    variable = self.level,
                                    value = 'Some college')
        somecollege.grid(row = 2, column = 5, sticky="w")
        college = Radiobutton(frame_6, text = "College     ",
                                    variable = self.level,
                                    value = 'College')
        college.grid(row = 2, column = 6, sticky="w")
        college = Radiobutton(frame_6, text = "Some/all post-graduate     ",
                                    variable = self.level,
                                    value = 'Some/all post-graduate')
        college.grid(row = 2, column = 7, sticky="w")

        #sleep
        frame_7 = Frame(window)
        frame_7.pack(fill=X, padx=50, pady=10, anchor="w")
        self.sleep = StringVar()
        label_7=Label(frame_7, text="How many hours did you sleep last night?")
        label_7.grid(row = 1, column = 1, sticky="w")
        entrysleep = Entry(frame_7,textvariable=self.sleep)
        entrysleep.grid(row = 1, column = 2, sticky="w")

        #health
        frame_8 = Frame(window)
        frame_8.pack(fill=X, padx=50, pady=10, anchor="w")

        self.health = StringVar()
        label_8=Label(frame_8, text="Please rate your current physical health compared to other people your age on the following 5-point scale where:")
        label_8.grid(row = 1)
        label_8_1=Label(frame_8, text="1 = much worse than average, 3 = average, 5 = much better than average.")
        label_8_1.grid(row = 2)

        frame_9 = Frame(window)
        frame_9.pack(fill=X, padx=50, anchor="w")
        space = Label(frame_9,text='                                       ')
        space.grid(row = 3, column = 1)
        health1 = Radiobutton(frame_9, text = " 1          ",
                                    variable = self.health,
                                    value = '1')
        health1.grid(row = 3, column = 2)
        health2 = Radiobutton(frame_9, text = " 2          ",
                                    variable = self.health,
                                    value = '2')
        health2.grid(row = 3, column = 3)
        health3 = Radiobutton(frame_9, text = " 3          ",
                                    variable = self.health,
                                    value = '3')
        health3.grid(row = 3, column = 4)
        health4 = Radiobutton(frame_9, text = " 4          ",
                                    variable = self.health,
                                    value = '4')
        health4.grid(row = 3, column = 5)
        health5 = Radiobutton(frame_9, text = " 5          ",
                                    variable = self.health,
                                    value = '5')
        health5.grid(row = 3, column = 6)
        
        
        Button(window,
               height=5, width=20,
               text='Submit',
               font=("Arial", 25),
               command=self.allsubmit).pack()
                                        
    
        window.mainloop()


    def allsubmit(self):
        os.chdir("/Users/mayrlab/Dropbox/finalized_experiments/Demographic")
        today = date.today().strftime("%Y")
        filename = today + "_demographic.csv"
        with open(filename,'a',encoding='utf-8') as f:
            if self.study.get() == '':
                showinfo('Alert','Please ask experimenter for help')
            elif self.ID.get() == '':
                showinfo("Alert","Please ask experimenter for help")
            elif self.Age.get() == '':
                showinfo("Alert", 'Please enter age')
            elif self.hand.get() == '':
                showinfo('Alert','Please enter which hand you write with')
            elif self.gender.get() == '':
                showinfo("Alert", 'Please enter your gender')
            elif self.race.get() == '':
                showinfo("Alert", 'Please enter your race')
            elif self.ethnicity.get() == '':
                showinfo("Alert", 'Please enter your ethnicity')
            elif self.year.get() == '' and self.otheryear.get() == '' and self.level.get() == '':
                showinfo("Alert", 'Please enter your education level')
            elif self.sleep.get() == '':
                showinfo("Alert", 'Please enter how many hours you slept last night')
            elif self.health.get() == '':
                showinfo("Alert", 'Please enter your health rating')
            else:
                today = date.today().strftime("%m/%d/%Y")
                with open(filename,'a',encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([today, self.study.get(), self.ID.get(), self.hand.get(),
                                     self.Age.get(),self.gender.get(),
                                     self.race.get(), self.ethnicity.get(),
                                     self.year.get(), self.otheryear.get(),
                                     self.level.get(), self.sleep.get(),
                                     self.health.get()])
                showinfo("Thanks", "Thanks for participating in our study!")
                                                                                                                                                                                               
TkDemo()

      
#mainloop()
#window.mainloop()
