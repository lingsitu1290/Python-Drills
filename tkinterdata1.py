#Python3
#The Tech Academy Python 73

from tkinter import *
from tkinter import ttk
import sqlite3

class makeWeb:

	def __init__(self):

		root = Tk()
		root.wm_title("Make a Webpage")
		root.minsize(width=300 ,height=200)

		#start a text box in GUI for name of website
		self.name = Entry(root)
		self.name.insert(0, 'Enter webpage name:')
		self.name.pack()

		#start a text box in GUI for body of website
		self.content = Entry(root)
		self.content.insert(0, 'Enter body content:')
		self.content.pack()

		#button to create webpage and add to database referenced to makewebpage method
		button = ttk.Button(root, text = "Make a webpage and add to database!",command = self.makeWebpage
			)
		button.pack()


		button2 = ttk.Button(root, text = "Fetch all from database!",command = self.querydatabase
			)
		button2.pack()


		conn = sqlite3.connect('webPages.db')

		c =conn.cursor()

		c.execute("CREATE TABLE IF NOT EXISTS webPages(content TEXT)")

		#print everything in database
		allData = c.fetchall()

		self.webpageList = Listbox(root, width = 50 , height = 30)
		self.webpageList.pack()

		#print everything that is stored in the database in a listbox
		for row in allData: 		
			self.webpageList.insert(END, row)

		self.webpageList.pack()

		self.webpageList.bind('<<ListboxSelect>>', self.selectWebPage
			)


		root.mainloop()

	def makeWebpage(self):

		#get name of website from entry box from GUI
		name = self.name.get()

		#create an html page with name
		f = open(name+'.html','w')

		#get the contents of the body entry box
		body = self.content.get()

		message = """<html>
		<body> """ + body+ """
		</body>
		</html>"""

		#write the selected contents of body into a html page
		f.write(message)
		
		f.close()


		conn = sqlite3.connect('webPages.db')

		c =conn.cursor()

		c.execute("CREATE TABLE IF NOT EXISTS webPages(content TEXT)")

		c.execute("INSERT INTO webPages(content) VALUES (?)", ([message]))

		conn.commit()


	def querydatabase(self):
		conn = sqlite3.connect('webPages.db')

		c =conn.cursor()

		c.execute("SELECT * FROM webPages")

		allData = c.fetchall()

		#delete all existing entries in the listbox
		self.webpageList.delete(0,END)
		
		for row in allData:	
			self.webpageList.insert(END, row) 	

		conn.commit()

	def selectWebPage(self,selected):

		#Get the content from the listbox that is selected, this will return a tuple
		#Get the index of the selected item in the listbox 
		selected = self.webpageList.get(self.webpageList.curselection())

		#create html page selected.html to store selected content 
		f = open('selected.html','w')
		#write the contents of selected into a html page, this will be the 0 index of the returned tuple
		f.write(selected[0])

		f.close()

def main():
	root = makeWeb()
	

if __name__== "__main__":
	main()

	



	

	


