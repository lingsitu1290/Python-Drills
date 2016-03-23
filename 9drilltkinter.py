#Python3
#The Tech Academy Python 72 or 76 

from tkinter import *
from tkinter import ttk

root = Tk()
root.wm_title("Make a Webpage")
root.minsize(width=250 ,height=150)

e = Entry(root)
e.pack()
e.focus_set()


def makeWebpage():
	f = open('helloworld.html','w')

	string = e.get()

	message = """<html>
	<body> """ + string + """
	</body>
	</html>"""

	f.write(message)
	f.close()

button = ttk.Button(root, text = "Make a webpage!", command= makeWebpage)
button.pack()

root.mainloop()


