'''
Title: Demographic
Author: Min Zhang
-----------------
Stand Alone Application:
# install this project using PyPI
$ pip install auto-py-to-exe
#Run
$ auto-py-to-exe


header
['Time', 'Study', 'SSID',  'Age', 'Gender','Race','Ethnicity']
'''
application_title='demographic'
main_python_file='demographic.py'
import time
from tkinter import *
import csv
import os
from tkinter.messagebox import *
from tkinter import filedialog
from datetime import datetime




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

        self.study = StringVar()
        studyList = os.listdir("/Experiments/")
        popupMenu = OptionMenu(window, self.study, *studyList) 
        Label(window, text = 'Choose a study').place(x=width/2-70 ,y=30)
        popupMenu.place(x=width/2+50,y=30)

        
        #SSID
        frame = Frame(window)
        frame.pack(padx=50, pady=10, anchor="w")
        labelID = Label(frame, text="SSID  ")
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


        #gender
        frame_2 = Frame(window)
        frame_2.pack(fill=X, padx=50, pady=10, anchor="w")
        label_2=Label(frame_2, text="Gender   ")
        label_2.grid(row = 1, column = 1)

        self.gender = StringVar()
        gender_male = Radiobutton(frame_2, text = "Male     ",
                                  variable = self.gender,
                                  value='Male')
        gender_male.grid(row=2, column=2, sticky="w")
        gender_female = Radiobutton(frame_2, text = "Female     ",
                                    variable = self.gender,
                                    value = 'Female')
        gender_female.grid(row = 2, column = 3, sticky="w")
        gender_other = Radiobutton(frame_2, text = "Other     ",
                                    variable = self.gender,
                                    value = 'other')
        gender_other.grid(row = 2, column = 4, sticky="w")
        gender_other = Radiobutton(frame_2, text = "Prefer not to answer     ",
                                    variable = self.gender,
                                    value = 'Prefer not to answer')
        gender_other.grid(row = 2, column = 5, sticky="w")

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
        ethnicity2.grid(row = 2, column = 3, sticky="w")

        ethnicity4 = Radiobutton(frame_4, text = "Prefer not to answer",
                                    variable = self.ethnicity,
                                    value = 'Prefer not to answe')
        ethnicity4.grid(row = 2, column = 4, sticky="w")
        
       
        
        #Submit Button 
        Button(window,
               height=3, width=20,
               text='Submit',
               font=("Arial", 25),
               command=self.allsubmit).pack()


        window.mainloop()



    def allsubmit(self):
        os.chdir("/Experiments/Domgraphic")
        today = datetime.today().strftime("%Y")
        filename = today + "_demographic.csv"
        with open(filename,'a',encoding='utf-8') as f:
            if self.study.get() == '':
                showinfo('Alert','Please ask experimenter for help')
            elif self.ID.get() == '':
                showinfo("Alert","Please ask experimenter for help")
            elif self.Age.get() == '':
                showinfo("Alert", 'Please enter age')
            elif self.gender.get() == '':
                showinfo("Alert", 'Please enter your gender')
            elif self.race.get() == '':
                showinfo("Alert", 'Please enter your race')
            elif self.ethnicity.get() == '':
                showinfo("Alert", 'Please enter your ethnicity')
            else:
                today = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                with open(filename,'a',encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([today, self.study.get(), self.ID.get(), 
                                     self.Age.get(),self.gender.get(),
                                     self.race.get(), self.ethnicity.get()])
                showinfo("Thanks", "Thanks for participating in our study!")
                                                                                                                                                                                               
TkDemo()

      
#mainloop()
#window.mainloop()
