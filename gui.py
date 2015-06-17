import Tkinter
import tkMessageBox
class interface:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.url = ''


	def draw(self):
		app =  Tkinter.Tk()
		app.title("Web Analyzer")
		app.geometry(`self.width`+'x'+`self.height`+'+200+200')

		labeltext = Tkinter.StringVar()
		labeltext.set("Analyze")
		label1 = Tkinter.Label(app,textvariable=labeltext,height=4)
		label1.pack()

		url = Tkinter.StringVar(None)
		site = Tkinter.Entry(app,textvariable=url)
		site.pack()

		dep = Tkinter.StringVar(None)
		depth = Tkinter.Entry(app,textvariable=dep)
		depth.pack()



		button1 = Tkinter.Button(app,text="Click Here",width=20,command=changeLabel)
		button1.pack(side='bottom' ,padx=15,pady=15)

		app.mainloop()

	def beenclicked():
		radiovalue = relstatus.get()
		TkMessageBox.showinfo("You clicked",radiovalue)
		return
	def changeLabel():
		name = "Thanks for the click "+ yourname.get()
		labeltext.set(name)
		yourname.delete(0,END)
		yourname.insert(0,"My name is Segun")


gui = interface(400,500)
gui.draw()