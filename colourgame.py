import tkinter 
import random

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0

tl = 30

def startGame(event):
	if tl == 30:
		countdown()
	nextColour()

def countdown():
	global tl

	if tl>0:
		tl -= 1
		timeLabel.config(text = "Time left:"+ str(tl))
		timeLabel.after(1000, countdown)

def nextColour():

	global score
	global tl 

	if tl>0:
		e.focus_set()
		if e.get().lower() == colours[1].lower():
			score += 1
        # clearing text entry box
		e.delete(0, tkinter.END)
		random.shuffle(colours)

		label.config(fg = str(colours[1]), text = str(colours[0]))

		scoreLabel.config(text = "Score:" + str(score))

root = tkinter.Tk()
root.title("COLOUR GAME")
root.geometry("375x200")

instructions = tkinter.Label(root, text= "Type in the colour of the words, and not the word text!", font = ('Helvetica', 12))
instructions.pack()

timeLabel = tkinter.Label(root, text="Time left: "+ str(tl), font = ('Helvetica',12))

timeLabel.pack()

e=tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()



