import Tkinter
import tkMessageBox
class interface:
	def __init__(self,width,height):
		self.width = width
		self.height = height


	def draw(self):
		app =  Tkinter.Tk()
		app.title("Test")
		app.geometry(`self.width`+'x'+`self.height`+'+200+200')

	