#Tech Academy 
#Drill 74

from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

class htmlsearcher:

	def __init__(self):
   
		root = Tk()
		root.wm_title("HTML Scraper")
		root.minsize(width=400 ,height=300)


		self.website = Entry(root, width = 40)
		self.website.insert(0, 'Enter webpage URL:')
		self.website.pack()

		self.element = Entry(root, width = 40)
		self.element.insert(0, 'Enter the element content you want to extract:')
		self.element.pack()

		self.text1 = Text(root, width =40, height = 40)
		self.text1.pack()

		button = Button(root, text = "Submit for Results!",command = self.getinfo
			)
		button.pack()


		root.mainloop()


	def getinfo(self):
		url = self.website.get()
		element = self.element.get() 

        #get contents from URL with requests 
		r  = requests.get("http://" +url)

		data = r.text

		soup = BeautifulSoup(data, 'html.parser')

		#for each line, insert into the Text box in tkinter
		for line in soup.find_all(element):
				self.text1.insert(END, line)


def main():
	root = htmlsearcher()
	

if __name__== "__main__":
	main()

