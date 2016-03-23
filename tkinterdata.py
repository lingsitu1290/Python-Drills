#Python3
#The Tech Academy Python 73

from tkinter import *
from tkinter import ttk
import sqlite3

#initiate root 
root = Tk()
root.wm_title("Make a Webpage")
root.minsize(width=250 ,height=150)

#start a text box in GUI 
e = Entry(root)
e.pack()
e.focus_set()
#Script to make a webpage
def makeWebpage():
	f = open('helloworld.html','w')

	string = e.get()

	message = """<html>
	<body> """ + string + """
	</body>
	</html>"""

	f.write(message)
	f.close()

#Script to add to the database
def createDatabase():
	string = e.get()

	message = """<html>
	<body> """ + string + """
	</body>
	</html>"""

	#Connect to database

	conn = sqlite3.connect('webpage.db')

	c =conn.cursor()

	c.execute("CREATE TABLE IF NOT EXISTS webPages(content TEXT)")

	c.execute("INSERT INTO webPages(content) VALUES (?)", ([message]))

	conn.commit()

	
def queryDatabase():

	conn = sqlite3.connect('webpage.db')

	c =conn.cursor()

	c.execute("SELECT * FROM webPages")

	#print everything in database
	#allData = c.fetchall()

	#webpageList = Listbox(root)
	#webpageList.pack()

	#print everything that is stored in the database as listbox
	#for row in allData: 		
		#webpageList.insert(END, row)


	#webpageList.bind('<<ListboxSelect>>', selectWebPage)


	conn.commit()

def selectWebPage(event):
	#Get the content from the listbox that is selected, this will return a tuple
	selected = webpageList.get(webpageList.curselection())
	#Get the index of the selected item in the listbox 

	f = open('helloworld.html','w')	

	#return the string corresponding to the selected index
	message = selected[0]

	print(message)

	f.write(message)
	f.close()

	

#put a button in the GUI that when clicked will run the script makeWebpage
button = ttk.Button(root, text = "Make a webpage!",command = makeWebpage)
button.pack()


button1 = ttk.Button(root, text= "Add to database!", command = createDatabase)
button1.pack()

button2 = ttk.Button(root, text= "Fetch all from database", command = queryDatabase)
button2.pack()

conn = sqlite3.connect('webpage.db')

c =conn.cursor()

c.execute("SELECT * FROM webPages")

#print everything in database
allData = c.fetchall()

webpageList = Listbox(root)
webpageList.pack()

#print everything that is stored in the database in a listbox
for row in allData: 		
	webpageList.insert(END, row)


webpageList.bind('<<ListboxSelect>>', selectWebPage)


root.mainloop()




