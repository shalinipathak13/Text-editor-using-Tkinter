from tkinter  import Tk, Menu, filedialog, END, messagebox, simpledialog
import tkinter.scrolledtext as ScrolledText
import os

#root for main Window
root = Tk(className = 'Text Editor')
textArea = ScrolledText.ScrolledText(root, width=100, height=80)

#Functions:

def newFile():
	#there is content?
	if len(textArea.get('1.0',END+'-1c'))>0:
		if messagebox.askyesno("Save?","Do you wish to save"):
			saveFile()
			textArea.delete('1.0',END)
		else:
			textArea.delete('1.0',END)

	root.title("TEXT EDITOR")

def openFile():
	file= filedialog.askopenfile(parent=root, title='Select a text file', defaultextension="*.txt" , filetypes=(("Text file", "*.txt"), ("All Files", "*.*")))

	root.title(os.path.basename(file.name)+" - TEXT EDITOR")

	if file != None:
		contents = file.read()
		textArea.insert('1.0',contents)
		file.close()

def saveFile():
	file= filedialog.asksaveasfile(mode='w',filetypes=(("Text file", "*.txt"), ("All Files", "*.*")))

	if file != None:
		#slice off the last characterfrom ger, as an extra return (enter) is added
		data = textArea.get('1.0',END+'-1c')
		file.write(data)
		file.close() 

def findInFile():
	findString = simpledialog.askstring("Find...", "Enter text:")
	textData= textArea.get('1.0',END)

	occurance=textData.upper().count(findString.upper())
	if occurance>0:
		label = messagebox.showinfo("Result", findString +  " was found " + str(occurance)+" times!" )

	else:
		label = messagebox.showinfo("Result", "Not Found!")




	

def about():
	label = messagebox.showinfo("About", "A python alternative notepad")

def exitRoot():
	if messagebox.showyesno("Quit","Are you sure you want to quit?"):
		root.destroy()




#Menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command= newFile)
fileMenu.add_command(label="Open", command= openFile)
fileMenu.add_command(label="Save", command= saveFile)
fileMenu.add_command(label="Find", command= findInFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit" ,command= exitRoot)

helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=about)



textArea.pack()
#keep window open
root.mainloop()