#!/usr/bin/env python3
#---------------------------------------------------------------------------------------
# Aaron's Fitness Application
# May 2020
#---------------------------------------------------------------------------------------
        
#---------------------------------------------------------------------------------------
# Libraries
#---------------------------------------------------------------------------------------
# - System
#---------------------------------------------------------------------------------------
import sys
#---------------------------------------------------------------------------------------
# - PyQt5 Application Library
#---------------------------------------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#---------------------------------------------------------------------------------------
# Global variables for formatting
#---------------------------------------------------------------------------------------

globalAppTitle = "Aaron's Home Fitness App"
globalWindowBackgroundColor = "background-color: cyan"
globalTextFont1 = QFont("Arial",70) # Main font
globalTextFont2 = QFont("Arial",40) # Subordinate font
globalTextColors = "background-color: yellow ; color: black"
globalTextFieldWidth = 300
globalTextFieldHeight = 100

#---------------------------------------------------------------------------------------
# Global variables for related to exercise plan
#---------------------------------------------------------------------------------------

IntensityLevel = "None"
MuscleGroup = "None"

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# The main window
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

class MainWindow(QMainWindow):

    #---------------------------------------------------------------------------------------
    # Initialize class
    #---------------------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)

        self.initUI()

    #---------------------------------------------------------------------------------------
    # Set class-specific details
    #---------------------------------------------------------------------------------------
        
    def initUI(self):
        
        #---------------------------------------------------------------------------------------
        # Initialize the window to the appropriate dimensions
        #---------------------------------------------------------------------------------------

        self.setWindowTitle(globalAppTitle)
        self.setStyleSheet(globalWindowBackgroundColor)

        self.top = 100
        self.left = 100
        self.width = 1200
        self.height = 800
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.line1 = QLabel("Aaron's Home Fitness", self)
        self.line1.setFont(globalTextFont1)
        self.line1.setStyleSheet("background-color: rgb(0,100,255) ; color: white")
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.resize(1100,100)
        self.line1.move(50,50)

        #---------------------------------------------------------------------------------------
        # Prompt for user input
        #---------------------------------------------------------------------------------------
        
        self.line2 = QLabel("Select Your Intensity Level Below", self)
        self.line2.setFont( QFont("Arial",50))
        self.line2.setStyleSheet("background-color: cyan ; color: black")
        self.line2.setAlignment(Qt.AlignCenter)
        self.line2.resize(1100,100)
        self.line2.move(50,250)

        #---------------------------------------------------------------------------------------
        # Workout intensity buttons
        #---------------------------------------------------------------------------------------

        self.easyButton = QPushButton("Easy", self)
        self.easyButton.setFont(globalTextFont2)
        self.easyButton.setStyleSheet("background-color: rgb(0,255,0) ; color: black")
        self.easyButton.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.easyButton.move(125,400)
        self.easyButton.clicked.connect(self.goWindow1Easy)
        
        self.mediumButton = QPushButton("Medium", self)
        self.mediumButton.setFont(globalTextFont2)
        self.mediumButton.setStyleSheet("background-color: yellow ; color: black")
        self.mediumButton.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.mediumButton.move(450,400)
        self.mediumButton.clicked.connect(self.goWindow1Medium)

        self.hardButton = QPushButton("Hard", self)
        self.hardButton.setFont(globalTextFont2)
        self.hardButton.setStyleSheet("background-color: rgb(255,0,0) ; color: black")
        self.hardButton.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.hardButton.move(125,400)
        self.hardButton.clicked.connect(self.goWindow1Hard)
        hloc = 1200 - globalTextFieldWidth - 125
        self.hardButton.move(hloc,400)
        
        self.extremeButton = QPushButton("Extreme", self)
        self.extremeButton.setFont(globalTextFont2)
        self.extremeButton.setStyleSheet("background-color: rgb(0,0,0) ; color: white")
        self.extremeButton.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.extremeButton.move(125,400)
        self.extremeButton.clicked.connect(self.goWindow1Extreme)
        self.extremeButton.move(450,525)
        
        #---------------------------------------------------------------------------------------
        # End of workout intensity buttons
        #---------------------------------------------------------------------------------------
        
        self.pushButton = QPushButton("Quit", self)
        self.pushButton.setFont(globalTextFont2)
        self.pushButton.setStyleSheet("background-color: rgb(0,100,255) ; color: white")
        self.pushButton.resize(130,70)
        self.pushButton.move(535,800-50-70)
        self.pushButton.clicked.connect(self.goQuit)

        self.show()

    #---------------------------------------------------------------------------------------
    # Clicking on each button will trigger the next window and set the global
    # "IntensityLevel" variable to the appropriate value
    #---------------------------------------------------------------------------------------

    def goQuit(self):
        QApplication.quit()
    
    def goWindow1Easy(self):
        global IntensityLevel
        IntensityLevel = "Easy"
        self.cams = Window1()
        self.cams.show()
        self.close()

    def goWindow1Medium(self):
        global IntensityLevel
        IntensityLevel = "Medium"
        self.cams = Window1()
        self.cams.show()
        self.close()

    def goWindow1Hard(self):
        global IntensityLevel
        IntensityLevel = "Hard"
        self.cams = Window1()
        self.cams.show()
        self.close()

    def goWindow1Extreme(self):
        global IntensityLevel
        IntensityLevel = "Extreme"
        self.cams = Window1()
        self.cams.show()
        self.close()
        
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# Muscle Group Selection Window
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

class Window1(QDialog):

    #---------------------------------------------------------------------------------------
    # Initialize class
    #---------------------------------------------------------------------------------------
    
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.initUI()

    #---------------------------------------------------------------------------------------
    # Set class-specific details
    #---------------------------------------------------------------------------------------

    def initUI(self):

        #---------------------------------------------------------------------------------------
        # Initialize the window to the appropriate dimensions
        #---------------------------------------------------------------------------------------
        
        self.setWindowTitle(globalAppTitle)
        self.setStyleSheet(globalWindowBackgroundColor)

        self.top = 100
        self.left = 100
        self.width = 1200
        self.height = 800
        self.setGeometry(self.top, self.left, self.width, self.height)

        #---------------------------------------------------------------------------------------
        # Prompt to ask the user for the selected muscle group
        #---------------------------------------------------------------------------------------
        
        self.line1 = QLabel("Select Target Area", self)
        self.line1.setFont(globalTextFont1)
        self.line1.setStyleSheet(globalTextColors)
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.resize(1100,100)
        self.line1.move(50,50)

        #---------------------------------------------------------------------------------------
        # Craete a 3x3 array of buttons that allow one to select the muscle group
        #---------------------------------------------------------------------------------------
        
        self.a11 = QPushButton("Triceps", self)
        self.a11.setFont(globalTextFont2)
        self.a11.setStyleSheet(globalTextColors)
        self.a11.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a11.move(50,200)
        self.a11.clicked.connect(self.goWindow2Triceps)
        
        self.a21 = QPushButton("Biceps", self)
        self.a21.setFont(globalTextFont2)
        self.a21.setStyleSheet(globalTextColors)
        self.a21.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a21.move(50,350)
        self.a21.clicked.connect(self.goWindow2Biceps)
        
        self.a31 = QPushButton("Glutes", self)
        self.a31.setFont(globalTextFont2)
        self.a31.setStyleSheet(globalTextColors)
        self.a31.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a31.move(50,500)
        self.a31.clicked.connect(self.goWindow2Glutes)
        
        self.a12 = QPushButton("Chest", self)
        self.a12.setFont(globalTextFont2)
        self.a12.setStyleSheet(globalTextColors)
        self.a12.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a12.move(450,200)
        self.a12.clicked.connect(self.goWindow2Chest)
        
        self.a22 = QPushButton("Shoulders", self)
        self.a22.setFont(globalTextFont2)
        self.a22.setStyleSheet(globalTextColors)
        self.a22.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a22.move(450,350)
        self.a22.clicked.connect(self.goWindow2Shoulders)
        
        self.a32 = QPushButton("Forearms", self)
        self.a32.setFont(globalTextFont2)
        self.a32.setStyleSheet(globalTextColors)
        self.a32.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a32.move(450,500)
        self.a32.clicked.connect(self.goWindow2Forearms)
        
        self.a13 = QPushButton("Back", self)
        self.a13.setFont(globalTextFont2)
        self.a13.setStyleSheet(globalTextColors)
        self.a13.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a13.move(850,200)
        self.a13.clicked.connect(self.goWindow2Back)
        
        self.a23 = QPushButton("Legs", self)
        self.a23.setFont(globalTextFont2)
        self.a23.setStyleSheet(globalTextColors)
        self.a23.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a23.move(850,350)
        self.a23.clicked.connect(self.goWindow2Legs)
        
        self.a33 = QPushButton("Core", self)
        self.a33.setFont(globalTextFont2)
        self.a33.setStyleSheet(globalTextColors)
        self.a33.resize(globalTextFieldWidth,globalTextFieldHeight)
        self.a33.move(850,500)
        self.a33.clicked.connect(self.goWindow2Core)

        #---------------------------------------------------------------------------------------
        # End of muscle group buttons
        #---------------------------------------------------------------------------------------

        #self.pushButton = QPushButton("Back", self)
        #self.pushButton.setFont(globalTextFont2)
        #self.pushButton.setStyleSheet("background-color: rgb(0,100,255) ; color: white")
        #self.pushButton.resize(130,70)
        #self.pushButton.move(50,800-50-70)
        #self.pushButton.clicked.connect(self.goMainWindow)

        self.pushButton = QPushButton("Home", self)
        self.pushButton.setFont(globalTextFont2)
        self.pushButton.setStyleSheet("background-color: rgb(0,100,255) ; color: white")
        self.pushButton.resize(130,70)
        self.pushButton.move(535,800-50-70)
        self.pushButton.clicked.connect(self.goMainWindow)

        #self.pushButton = QPushButton("Next", self)
        #self.pushButton.setFont(globalTextFont2)
        #self.pushButton.setStyleSheet("background-color: rgb(0,100,255) ; color: white")
        #self.pushButton.resize(130,70)
        #self.pushButton.move(1200-130-50,800-50-70)
        #self.pushButton.clicked.connect(self.goWindow2)

        self.show()

    #---------------------------------------------------------------------------------------
    # Buttons re-direct user to the appropriate window and if a muscle group is selected,
    # the global variable is set to that muscle group
    #---------------------------------------------------------------------------------------
        
    def goMainWindow(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close() 

    def goWindow2Triceps(self):
        global MuscleGroup
        MuscleGroup = "Triceps"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Biceps(self):
        global MuscleGroup
        MuscleGroup = "Biceps"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Glutes(self):
        global MuscleGroup
        MuscleGroup = "Glutes"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Chest(self):
        global MuscleGroup
        MuscleGroup = "Chest"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Shoulders(self):
        global MuscleGroup
        MuscleGroup = "Shoulders"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Forearms(self):
        global MuscleGroup
        MuscleGroup = "Forearms"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Back(self):
        global MuscleGroup
        MuscleGroup = "Back"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Legs(self):
        global MuscleGroup
        MuscleGroup = "Legs"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
    def goWindow2Core(self):
        global MuscleGroup
        MuscleGroup = "Core"
        self.cams = Window2()
        self.cams.show()
        self.close() 
        
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# Suggested Workout Window
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

class Window2(QDialog):

    #---------------------------------------------------------------------------------------
    # Initialize class
    #---------------------------------------------------------------------------------------
    
    def __init__(self, parent=None):

        super().__init__(parent)

        self.initUI()

    #---------------------------------------------------------------------------------------
    # Set class-specific details
    #---------------------------------------------------------------------------------------

    def initUI(self):

        #---------------------------------------------------------------------------------------
        # First, set up all the exercises based on the
        # user input.  Later, set the window dimensions
        # and complete all the text fields with that
        # information accordingly.
        #---------------------------------------------------------------------------------------
        # Global variable that contains the intensity level
        #---------------------------------------------------------------------------------------
        global IntensityLevel
        #---------------------------------------------------------------------------------------
        # Global variable that contains the muscle group
        #---------------------------------------------------------------------------------------
        global MuscleGroup
        #---------------------------------------------------------------------------------------
        # Show the information in terminal (for debugging)
        #---------------------------------------------------------------------------------------
        print("Intenisty level: " , IntensityLevel , " Muscle Group: " , MuscleGroup)
        #---------------------------------------------------------------------------------------
        # Variables containing the number of suggested exercises
        # and their resepective values: nExercises, e1, e2, e3, e4, e5, e6
        #---------------------------------------------------------------------------------------
        nExercises = 0
        e1="None"
        e2="None"
        e3="None"
        e4="None"
        e5="None"
        e6="None"
        #---------------------------------------------------------------------------------------
        # Easy workouts - All Possibilities
        #---------------------------------------------------------------------------------------
        if IntensityLevel=="Easy":

            if MuscleGroup=="Triceps":
                print("Easy-Triceps")
                nExercises = 3
                e1="Tricep Extensions x5"
                e2="Tricep Kickback x5"
                e3="Tricep Dips x10"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Biceps":
                print("Easy-Biceps")
                nExercises = 3
                e1="Downward dog push-ups x10"
                e2="Towel Curl x5 each"
                e3="Elevated Pike Push-ups x5"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Glutes":
                print("Easy-Glutes")
                nExercises = 3
                e1="Bottoms-up lunge x5 each"
                e2="Glute Bridge x5"
                e3="Step ups x5 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Chest":
                print("Easy-Chest")
                nExercises = 3
                e1="Push ups x5"
                e2="Plyometric push-ups x5"
                e3="Incline Push-ups x5"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Shoulders":
                print("Easy-Shoulders")
                nExercises = 3
                e1="Plank raise tap crunch x5 each"
                e2="Reverse Fly x10"
                e3="Arnold Press x5"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Forearms":
                print("Easy-Forearms")
                nExercises = 3
                e1="Fingertip pushups x5"
                e2="Crab Walk x30 seconds"
                e3="Forearm Squeeze x5 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Back":
                print("Easy-Back")
                nExercises = 3
                e1="Superman x30 seconds"
                e2="Plank x30 seconds"
                e3="Aquaman x30 seconds"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Legs":
                print("Easy-Legs")
                nExercises = 3
                e1="Quat x5"
                e2="Lunges x5 each"
                e3="Wall sits x30 seconds"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Core":
                print("Easy-Core")
                nExercises = 3
                e1="Leg Raises x5"
                e2="Sit Ups x5"
                e3="Bicycles x15 seconds"
                e4="None"
                e5="None"
                e6="None"
            else:
                print("Error:  Muscle Group Value")
        #---------------------------------------------------------------------------------------
        # Medium workouts - All Possibilities
        #---------------------------------------------------------------------------------------
        elif IntensityLevel=="Medium":

            if MuscleGroup=="Triceps":
                print("Medium-Triceps")
                nExercises = 3
                e1="Tricep Extensions x 10"
                e2="Tricep Kickback x10"
                e3="Tricep Dips x 15"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Biceps":
                print("Medium-Biceps")
                nExercises = 3
                e1="Downward dog push-ups x15"
                e2="Towel Curl x 10 each"
                e3="Elevated Pike Push-ups x10"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Glutes":
                print("Medium-Glutes")
                nExercises = 3
                e1="Bottoms-up lunge x10 each"
                e2="Glute Bridge x10"
                e3="Step ups x10 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Chest":
                print("Medium-Chest")
                nExercises = 3
                e1="Push ups x10"
                e2="Plyometric push-ups x10"
                e3="Incline Push-ups x10"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Shoulders":
                print("Medium-Shoulders")
                nExercises = 3
                e1="Plank raise tap crunch x10 each"
                e2="Reverse Fly x15"
                e3="Arnold Press x10"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Forearms":
                print("Medium-Forearms")
                nExercises = 3
                e1="Fingertip pushups x7"
                e2="Crab Walk x1 minute"
                e3="Forearm Squeeze x10 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Back":
                print("Medium-Back")
                nExercises = 3
                e1="Superman x 1 minute"
                e2="Plank x 1 minut"
                e3="Aquaman x 1 minute"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Legs":
                print("Medium-Legs")
                nExercises = 3
                e1="Quat x15"
                e2="Lunges x 10 each"
                e3="Wall sits x 1 minute"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Core":
                print("Medium-Core")
                nExercises = 3
                e1="Leg Raises x10"
                e2="Sit Ups x 10"
                e3="Bicycles x 30 seconds"
                e4="None"
                e5="None"
                e6="None"
            else:
                print("Error:  Muscle Group Value")
        #---------------------------------------------------------------------------------------
        # Hard workouts - All Possibilities
        #---------------------------------------------------------------------------------------
        elif IntensityLevel=="Hard":

            if MuscleGroup=="Triceps":
                print("Hard-Triceps")
                nExercises = 3
                e1="Tricep Extensions x 15"
                e2="Tricep Kickback x15"
                e3="Tricep Dips x 20"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Biceps":
                print("Hard-Biceps")
                nExercises = 3
                e1="Downward dog push-ups x20"
                e2="Towel Curl x 15 each"
                e3="Elevated Pike Push-ups x15"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Glutes":
                print("Hard-Glutes")
                nExercises = 3
                e1="Bottoms-up lunge x15 each"
                e2="Glute Bridge x15"
                e3="Step ups x20 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Chest":
                print("Hard-Chest")
                nExercises = 3
                e1="Push ups x20"
                e2="Plyometric push-ups x15"
                e3="Incline Push-ups x15"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Shoulders":
                print("Hard-Shoulders")
                nExercises = 3
                e1="Plank raise tap crunch x15 each"
                e2="Reverse Fly x20"
                e3="Arnold Press x15"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Forearms":
                print("Hard-Forearms")
                nExercises = 3
                e1="Fingertip pushups x10"
                e2="Crab Walk x3 minutes"
                e3="Forearm Squeeze x20 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Back":
                print("Hard-Back")
                nExercises = 3
                e1="Superman x 1 minute 30 seconds"
                e2="Plank x2 minute"
                e3="Aquaman x1 minute 30 seconds"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Legs":
                print("Hard-Legs")
                nExercises = 3
                e1="Quat x25"
                e2="Lunges x20 each"
                e3="Wall sits x2 minutes"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Core":
                print("Hard-Core")
                nExercises = 3
                e1="Leg Raises x15"
                e2="Sit Ups x20"
                e3="Bicycles x1 minute"
                e4="None"
                e5="None"
                e6="None"
            else:
                print("Error:  Muscle Group Value")
        #---------------------------------------------------------------------------------------
        # Extreme workouts - All Possibilities
        #---------------------------------------------------------------------------------------
        elif IntensityLevel=="Extreme":

            if MuscleGroup=="Triceps":
                print("Extreme-Triceps")
                nExercises = 3
                e1="Tricep Extensions x 20"
                e2="Tricep Kickback x20"
                e3="Tricep Dips x30"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Biceps":
                print("Extreme-Biceps")
                nExercises = 3
                e1="Downward dog push-ups x25"
                e2="Towel Curl x20 each"
                e3="Elevated Pike Push-ups x25"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Glutes":
                print("Extreme-Glutes")
                nExercises = 3
                e1="Bottoms-up lunge x20 each"
                e2="Glute Bridge x25"
                e3="Step ups x25 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Chest":
                print("Extreme-Chest")
                nExercises = 3
                e1="Push ups x3"
                e2="Plyometric push-ups x25"
                e3="Incline Push-ups x25"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Shoulders":
                print("Extreme-Shoulders")
                nExercises = 3
                e1="Plank raise tap crunch x20 each"
                e2="Reverse Fly x25"
                e3="Arnold Press x20"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Forearms":
                print("Extreme-Forearms")
                nExercises = 3
                e1="Fingertip pushups x20"
                e2="Crab Walk x5 minutes"
                e3="Forearm Squeeze x30 each"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Back":
                print("Extreme-Back")
                nExercises = 3
                e1="Superman x3 minutes"
                e2="Plank x5 minutes"
                e3="Aquaman x3 minutes"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Legs":
                print("Extreme-Legs")
                nExercises = 3
                e1="Quat x40"
                e2="Lunges x30 each"
                e3="Wall sits x5 minutes"
                e4="None"
                e5="None"
                e6="None"
            elif MuscleGroup=="Core":
                print("Extreme-Core")
                nExercises = 3
                e1="Leg Raises x25"
                e2="Sit Ups x30"
                e3="Bicycles x2 minutes"
                e4="None"
                e5="None"
                e6="None"
            else:
                print("Error:  Muscle Group Value")
        #---------------------------------------------------------------------------------------
        else:
            print("Error:  Intensity Value")
        #---------------------------------------------------------------------------------------
        # Initialize the window to the appropriate dimensions
        #---------------------------------------------------------------------------------------
        self.setWindowTitle(globalAppTitle)
        self.setStyleSheet(globalWindowBackgroundColor)

        self.top = 100
        self.left = 100
        self.width = 1200
        self.height = 800
        self.setGeometry(self.top, self.left, self.width, self.height)

        #---------------------------------------------------------------------------------------
        # Show the title of the workout as long as number of exercises is >= 1
        # otherwise report an error (for debugging purposes)
        #---------------------------------------------------------------------------------------
        
        if nExercises > 1:
        
            self.line1 = QLabel("Your Suggested Workout Is (3 sets)", self)
            self.line1.setFont(globalTextFont1)
            self.line1.setStyleSheet(globalTextColors)
            self.line1.setAlignment(Qt.AlignCenter)
            self.line1.resize(1100,100)
            self.line1.move(50,50)

        else:
        
            self.line1 = QLabel("Error:  nExercises <= 0", self)
            self.line1.setFont(globalTextFont1)
            self.line1.setStyleSheet(globalTextColors)
            self.line1.setAlignment(Qt.AlignCenter)
            self.line1.resize(1100,100)
            self.line1.move(50,50)

        #---------------------------------------------------------------------------------------
        # If nExercises is greater than or equal to 1 show exercises #1
        #---------------------------------------------------------------------------------------
            
        if nExercises >= 1: 

            self.w1 = QLabel("Exercise 1: "+e1, self)
            self.w1.setFont(globalTextFont2)
            self.w1.setStyleSheet(globalTextColors)
            self.w1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.w1.resize(1100,60)
            self.w1.move(50,200)

        #---------------------------------------------------------------------------------------
        # If nExercises is greater than or equal to 2 show exercises #2
        #---------------------------------------------------------------------------------------

        if nExercises >= 2: 

            self.w2 = QLabel("Exercise 2: "+e2, self)
            self.w2.setFont(globalTextFont2)
            self.w2.setStyleSheet(globalTextColors)
            self.w2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.w2.resize(1100,60)
            self.w2.move(50,270)

        #---------------------------------------------------------------------------------------
        # If nExercises is greater than or equal to 3 show exercises #3
        #---------------------------------------------------------------------------------------

        if nExercises >= 3:

            self.w3 = QLabel("Exercise 3: "+e3, self)
            self.w3.setFont(globalTextFont2)
            self.w3.setStyleSheet(globalTextColors)
            self.w3.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.w3.resize(1100,60)
            self.w3.move(50,340)

        #---------------------------------------------------------------------------------------
        # If nExercises is greater than or equal to 4 show exercises #4
        #---------------------------------------------------------------------------------------

        if nExercises >= 4: 

            self.w4 = QLabel("Exercise 4: "+e4, self)
            self.w4.setFont(globalTextFont2)
            self.w4.setStyleSheet(globalTextColors)
            self.w4.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.w4.resize(1100,60)
            self.w4.move(50,410)

        #---------------------------------------------------------------------------------------
        # If nExercises is greater than or equal to 5 show exercises #5
        #---------------------------------------------------------------------------------------

        if nExercises >= 5: 

            self.w5 = QLabel("Exercise 5: "+e5, self)
            self.w5.setFont(globalTextFont2)
            self.w5.setStyleSheet(globalTextColors)
            self.w5.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.w5.resize(1100,60)
            self.w5.move(50,480)
        
        #---------------------------------------------------------------------------------------
        # If nExercises is greater than or equal to 6 show exercises #6
        #---------------------------------------------------------------------------------------

        if nExercises >= 6: 

            self.w6 = QLabel("Exercise 6: "+e6, self)
            self.w6.setFont(globalTextFont2)
            self.w6.setStyleSheet(globalTextColors)
            self.w6.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.w6.resize(1100,60)
            self.w6.move(50,550)
            
        #---------------------------------------------------------------------------------------
        # Navigation buttons
        #---------------------------------------------------------------------------------------

        self.pushButton = QPushButton("Back", self)
        self.pushButton.setFont(globalTextFont2)
        self.pushButton.setStyleSheet("background-color: rgb(0,100,255) ; color: white")
        self.pushButton.resize(130,70)
        self.pushButton.move(50,800-50-70)
        self.pushButton.clicked.connect(self.goWindow2)

        self.pushButton = QPushButton("Home", self)
        self.pushButton.setFont(globalTextFont2)
        self.pushButton.setStyleSheet("background-color: rgb(0,100,255) ; color: white")
        self.pushButton.resize(130,70)
        self.pushButton.move(535,800-50-70)
        self.pushButton.clicked.connect(self.goMainWindow)

        self.show()

    #---------------------------------------------------------------------------------------
    # Navigation button functions
    #---------------------------------------------------------------------------------------

    def goMainWindow(self):
        self.cams = MainWindow()
        self.cams.show()
        self.close() 

    def goWindow2(self):
        self.cams = Window1()
        self.cams.show()
        self.close() 





        
#---------------------------------------------------------------------------------------
# MAIN PROGRAM CALL
#---------------------------------------------------------------------------------------

if __name__ == '__main__':

    # Create the application
    app = QApplication(sys.argv)
    # Create the instance of the main window
    window = MainWindow()
    # Start the application
    sys.exit(app.exec_())




