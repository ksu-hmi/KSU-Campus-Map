import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

screen = tk.Tk()


def search():
	floors_file = open("Floors.txt", "r")
	flag = 0
	start = 0
	searched = entry_box.get()
	last_position = floors_file.tell()
	
	# print (floors_file.readline())
	"""for line in floors_file.readline():
		print ("test 1")
		print (line)
		for word in line.split():
			print ("test 2")
			print (word)
			if word == searched:
				print ("test 3")
				flag = 1
				while word != ',':
	
				print (line)"""\
	
	if searched == '':
		pass
	
	#elif int(searched) >= 0 or int(searched) < 0:
	#	pass
	
	elif searched in floors_file.read():
		
		floors_file.seek(last_position)		
		
		for line in floors_file.readlines():
			
			if searched in line:			
				start = 1

			if start == 0:
				pass
			else:
				if "," in line:				
					break
				else:
					print (line)
		flag = 1
	
	if flag == 0:
		not_valid = tk.Label(screen, text="Not A Valid Input, Search Again")
		not_valid.place(x=625, y=25)
		print("Not a valid input")
	
	floors_file.close()


# screen title and size
screen.title("Campus")
screen.geometry("930x610")

# What can be searched for
title_question = tk.Label(screen, text="Classes to Search:")
title_question.pack(side = TOP)


# Entry Box
entry_box = tk.Entry(screen)
entry_box.pack(side = TOP)

# Search Button
search_button = tk.Button(screen, text="Search", bg="Blue",command=search)
search_button.place(x = 550, y = 20)

img = ImageTk.PhotoImage(Image.open("campus.png"))
panel = tk.Label(screen, image = img)
panel.pack(side = BOTTOM)


screen.mainloop()
