## About ##

# Number Guessing Game - Santino Scialabba
# CMPSC 132 Final Project
# Users attempt to guess a randomly generated number in the fewest number of attempts
# Uses the Tkinter GUI library

## Citations ##
# What is the best GUI library for Python?
# https://www.reddit.com/r/Python/comments/wedvzi/what_is_the_best_gui_library_for_python/
# Python Tkinter
# https://www.geeksforgeeks.org/python/python-gui-tkinter/
# Enhancing Text Presentation with Tkinter Fonts
# https://www.geeksforgeeks.org/python/tkinter-fonts/
# List available font families in `tkinter`
# https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
# Tkinter.grid spacing options?
# https://stackoverflow.com/questions/28019402/tkinter-grid-spacing-options
# How do I change button size in Python?
# https://stackoverflow.com/questions/14247709/how-do-i-change-button-size-in-python
# hide frame on button press tkinter python
# https://stackoverflow.com/questions/55093812/hide-frame-on-button-press-tkinter-python
# random — Generate pseudo-random numbers
# https://docs.python.org/3/library/random.html

## Imported libraries ##

import tkinter as tk
import tkinter.font as tkFont
import math
import random

## Global variables ##

MIN_DIFFICULTY_LEVEL = 1 # Minimum difficulty level configurable by user
MAX_DIFFICULTY_LEVEL = 5 # Maximum difficulty level configurable by user
MIN_ATTEMPTS = 5 # Minimum number of attempts configurable by user
MAX_ATTEMPTS = 15 # Maximum number of attempts configurable by user
difficultyLevel = math.ceil((MAX_DIFFICULTY_LEVEL - MIN_DIFFICULTY_LEVEL) / 2)
maxAttempts = math.ceil((MAX_ATTEMPTS - MIN_ATTEMPTS) / 2)
guessesRemaining = 0 # Global variable that keeps track of guesses remaining
randomNumber = 0 # Global variable that stores the generated random number
guessNum = 0 # Global variable that stores what guess the user is currently on
guessElements = [] # Global list that stores the UI elements for the user inputted guesses so that they can be easily deleted after the user starts a new game

root = tk.Tk() # Creates the window that appears after running the program

## Frames ##
titleFrame = tk.Frame(root) # Stores the title
configFrame = tk.Frame(root) # Stores all the configuration UI (Max guesses, difficulty, start button)
gameFrame = tk.Frame(root) # Stores all the game UI (Guess input, submit button, guess history, reset button)

## Fonts ##
titleFont = tkFont.Font(family="Ubuntu", size=36, weight="bold")
subtitleFont = tkFont.Font(family="Ubuntu", size=24, weight="bold")
textFont = tkFont.Font(family="Ubuntu", size=16)
buttonFont = tkFont.Font(family="Ubuntu", size=16, weight="bold")

## UI Elements ##
titleFrame.pack() # Places the title into the window
configFrame.pack() # Places the configuration menu into the window

# Title
title = tk.Label(titleFrame, text="Number Guessing Game (0-10)", font = titleFont) # Title UI element
title.pack()

# Configuration
difficultyLabel = tk.Label(configFrame, text= "Difficulty", font = textFont)
difficultyDisplay = tk.Label(configFrame, text = str(difficultyLevel), font = buttonFont, bg = "white", height = 2, width = 3) # Displays current difficulty
difficultyDownButton = tk.Label(configFrame, text="-", font = buttonFont, bg = "red", height = 2, width = 3) # Adjusts difficulty down
difficultyUpButton = tk.Label(configFrame, text="+", font = buttonFont, bg = "green", height = 2, width = 3) # Adjusts difficulty up
maxAttemptsLabel = tk.Label(configFrame, text= "Attempts", font = textFont)
maxAttemptsDisplay = tk.Label(configFrame, text = str(maxAttempts), font = buttonFont, bg = "white", height = 2, width = 3) # Displays current max attempts
maxAttemptsDownButton = tk.Label(configFrame, text="-", font = buttonFont, bg = "red", height = 2, width = 3) # Adjusts max attempts down
maxAttemptsUpButton = tk.Label(configFrame, text="+", font = buttonFont, bg = "green", height = 2, width = 3) # Adjusts max attempts up
playButton = tk.Label(configFrame, text="Play", font = buttonFont, bg = "green", height = 2, width = 8) # Adjusts max attempts up

difficultyLabel.grid(row=0, column=0, columnspan=4)
difficultyDisplay.grid(row=0, column=4)
difficultyDownButton.grid(row=0, column=5)
difficultyUpButton.grid(row=0, column=6)
maxAttemptsLabel.grid(row=1, column=0, columnspan=4)
maxAttemptsDisplay.grid(row=1, column=4)
maxAttemptsDownButton.grid(row=1, column=5)
maxAttemptsUpButton.grid(row=1, column=6)
playButton.grid(row=2, column=0, columnspan=7)

configFrame.grid_columnconfigure(0, minsize=125)
configFrame.grid_rowconfigure(0, minsize=100)
configFrame.grid_rowconfigure(1, minsize=100)
configFrame.grid_rowconfigure(2, minsize=200)

# Game
guessLabel = tk.Label(gameFrame, text= "Guess", font = textFont)
guessInput = tk.Entry(gameFrame)
guessSubmit = tk.Label(gameFrame, text="Submit", font = buttonFont, bg = "green", height = 1, width = 6)
guessInvalid = tk.Label(gameFrame, text= "Guess out of range (0-10)", font = textFont)
gameReset = tk.Label(gameFrame, text="Reset", font = buttonFont, bg = "green", height = 1, width = 6)

guessLabel.grid(row = 0, column = 0)
guessInput.grid(row = 0, column = 1)
guessSubmit.grid(row = 0, column = 2)

gameFrame.grid_columnconfigure(0, minsize=100)
gameFrame.grid_columnconfigure(1, minsize=100)
gameFrame.grid_columnconfigure(2, minsize=200)

## Functions ##

# When difficulty down button pressed, decrease difficulty by one if permitted (difficulty level must be greater than MIN_DIFFICULTY_LEVEL)
# Then, update config UI
def difficultyDown(event):
    global difficultyLevel
    global MIN_DIFFICULTY_LEVEL
    if difficultyLevel > MIN_DIFFICULTY_LEVEL:
        difficultyLevel -= 1
        updateConfig()

# When difficulty up button pressed, increase difficulty by one if permitted (difficulty level must be less than MAX_DIFFICULTY_LEVEL)
# Then, update config UI
def difficultyUp(event):
    global difficultyLevel
    global MAX_DIFFICULTY_LEVEL
    if difficultyLevel < MAX_DIFFICULTY_LEVEL:
        difficultyLevel += 1
        updateConfig()

# When max attempts down button pressed, decrease max number of attempts by one if permitted (max attempts must be greater than MIN_ATTEMPTS)
# Then, update config UI
def maxAttemptsDown(event):
    global maxAttempts
    global MIN_ATTEMPTS
    if maxAttempts > MIN_ATTEMPTS:
        maxAttempts -= 1
        updateConfig()

# When max attempts up button pressed, increase max number of attempts by one if permitted (max attempts must be less than MAX_ATTEMPTS)
# Then, update config UI
def maxAttemptsUp(event):
    global maxAttempts
    global MAX_ATTEMPTS
    if maxAttempts < MAX_ATTEMPTS:
        maxAttempts += 1
        updateConfig()

# Checks values of difficultyLevels and maxAttempts, updates difficultyDisplay label and maxAttemptsDisplay label
def updateConfig():
    global difficultyLevel
    global maxAttempts
    global difficultyDisplay
    global maxAttemptsDisplay
    difficultyDisplay.config(text=str(difficultyLevel))
    maxAttemptsDisplay.config(text=str(maxAttempts))

# If the config menu is visible, make config menu invisible and game menu visible
# If the config menu is not visible, make config menu visible and game menu invisible
def toggleVisibility():
    global configFrame
    global gameFrame
    if configFrame.winfo_manager():
        configFrame.pack_forget()
        gameFrame.pack()
    else:
        configFrame.pack()
        gameFrame.pack_forget()

# Takes a decimal number in the format 0.xxxxx... and truncates it to the format x.xx
# Leaves the specified number of decimals - 1
def truncate(number, decimalPlaces):
    return math.trunc(number * 10 ** decimalPlaces) / (10 ** (decimalPlaces - 1))

# When the user submits a guess, do the following:
# 1.) Check to see if guesses remain. If there are no guesses left, do nothing and skip steps 2-9
# 2.) Check to see if the value submitted is a number. If it is not numeric, do nothing and skip steps 3-9
# 3.) Check to see if the number is between 0 and 10 inclusive. If it is not, display the guessInvalid UI element and skip steps 4-9. If it is, make the guessInvalid UI element invisible
# 4.) Increase guessNum by 1, decrease guessesRemaining by 1
# 5.) Create UI elements that display the attempt #, the guess, and whether the guess was too low, too high, or correct
# 6.) Add the UI elements to the grid
# 7.) If the user guessed the correct number, display a winner message, then make the reset button visible
# 8.) If the user reached the maximum number of guesses, display a loser message,  then make the reset button visible
# 9.) Clear the guess box
def submitGuess(event):
    global gameFrame
    global maxAttempts
    global guessesRemaining
    global randomNumber
    global guessNum
    if guessesRemaining < 1: # If the user has no guesses remaining, do nothing
        return
    try:
        guess = float(guessInput.get()) # If the guess can be cast to float, it is a number
    except ValueError:
        return # If an exception is thrown, do nothing
    if guess < 0 or guess > 10: # If the guess is out of range, display message saying that the guess is out of range and do nothing
        guessInvalid.grid(row=1, column=0, columnspan=3)
        return
    else: # If the guess is in range, make guessInvalid invisible
        guessInvalid.grid_forget()
    guessNum += 1 # Increase guess number by 1
    guessesRemaining -= 1 # Decrease guesses remaining by 1
    submissionNum = tk.Label(gameFrame, text="Guess #" + str(guessNum), font=textFont) # Create submission # label
    guessElements.append(submissionNum) # Add submissionNum to UI elements list
    guessString = str(guess)
    for i in range(difficultyLevel - len(guessString) + 1): # Adds trailing zeros so that the UI label has the same decimal precision as the randomly generated number
        guessString += "0"
    submissionLabel = tk.Label(gameFrame, text=guessString, font=textFont) # Create guess label
    guessElements.append(submissionLabel) # Add guessElements to UI elements list
    if guess < randomNumber: # If guess is lower than the correct number, create label that displays "Too low!" and add it to the list of UI elements
        highOrLow = tk.Label(gameFrame, text= "Too low!", font=textFont)
        guessElements.append(highOrLow)
    elif guess > randomNumber: # If guess is higher than the correct number, create label that displays "Too high!" and add it to the list of UI elements
        highOrLow = tk.Label(gameFrame, text="Too high!", font=textFont)
        guessElements.append(highOrLow)
    else: # If guess is correct, create label that displays "Correct!", display winner message, display reset button, add correct and winner label to UI elements
        highOrLow = tk.Label(gameFrame, text="Correct!", font=textFont)
        guessElements.append(highOrLow)
        gameWonLabel = tk.Label(gameFrame, text="You Won!", font=textFont)
        guessElements.append(gameWonLabel)
        gameWonLabel.grid(row = guessNum + 2, column = 0, columnspan = 3)
        gameReset.grid(row = guessNum + 3, column = 0, columnspan = 3)
    if guessesRemaining == 0: # After the guess, if there are no guesses left, display loser message, display reset button, add loser label to UI elements
        gameLostLabel = tk.Label(gameFrame, text="Game Over! Better luck next time.", font=textFont)
        guessElements.append(gameLostLabel)
        gameLostLabel.grid(row = guessNum + 2, column = 0, columnspan = 3)
        gameReset.grid(row=guessNum + 3, column=0, columnspan=3)

    submissionNum.grid(row=guessNum + 1, column=0) # Add submission # label to grid
    submissionLabel.grid(row=guessNum + 1, column=1) # Add guess label to grid
    highOrLow.grid(row=guessNum + 1, column=2) # Add message label to grid
    guessInput.delete(0, tk.END) # Clear the guess box
    guessInput.insert(0, "")


# Assigns a random number from 1-10 with a number of decimal places that matches (difficultyLevel - 1)
# Example: difficulty level of 3 will have a random number x.xx, difficulty level of 5 will have a random number x.xxxx
def startGame(event):
    global difficultyLevel
    global maxAttempts
    global guessesRemaining
    global randomNumber
    global guessNum
    guessesRemaining = maxAttempts
    guessNum = 0
    randomNumber = truncate(random.random(), difficultyLevel)
    toggleVisibility()

# When the user presses the reset button, delete all previous guess UI elements, reset guessesRemaining and guessNum, make reset button invisible, run toggleVisibility() and updateConfig()
def resetGame(event):
    global difficultyLevel
    global maxAttempts
    global guessesRemaining
    global randomNumber
    global guessNum
    for i in guessElements: # Deletes all previous guess UI elements
        i.destroy()
    guessElements.clear() # Clears list of guess UI elements
    guessesRemaining = 0 # Reset guessesRemaining
    guessNum = 0 # Reset guessNum
    gameReset.grid_forget() # Make reset button invisible
    toggleVisibility()
    updateConfig()

## Button bindings ##

difficultyDownButton.bind('<Button-1>', difficultyDown)
difficultyUpButton.bind('<Button-1>', difficultyUp)
maxAttemptsDownButton.bind('<Button-1>', maxAttemptsDown)
maxAttemptsUpButton.bind('<Button-1>', maxAttemptsUp)
playButton.bind('<Button-1>', startGame)
guessSubmit.bind('<Button-1>', submitGuess)
gameReset.bind('<Button-1>', resetGame)

# Sets runtime environment
root.mainloop()