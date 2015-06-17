from tkinter import*
import tkinter.messagebox
from main import *
import networkx as nx
import matplotlib.pyplot as plt
import graph



def changeLabel():

	site = link.get()
	num = depthname.get()

	(_ROOT, _DEPTH, _BREADTH) = range(3)

	G=nx.Graph()
	data,root = analyse_web(site,num)

	children = data[root].children
	parent[depth] = root
	G.add_node('root')
	    

	depth += 1

	for child in children:

	    G.add_node(format(children))
	    
	    G.add_edge(format(children),'root')

	         # display
	plot(data,root,G)
	nx.draw(G)
	plt.savefig("node_colormap.png") # save as png
	plt.show()

app =  Tkinter.Tk()
app.title("LINK ANALYSER.......")
app.geometry('450x300+200+200')

labeltext = Tkinter.StringVar()
labeltext.set("Click button")
label1 = Tkinter.Label(app,textvariable=labeltext,height=4)
label1.pack()

checkboxval = Tkinter.IntVar()
checkbox1 = Tkinter.Checkbutton(app,variable=checkboxval,text="Happy?")
checkbox1.pack()

url = Tkinter.StringVar(None)
link = Tkinter.Entry(app,textvariable=url)
link.pack()

Deptvalue = Tkinter.IntVar(None)
depthname = Tkinter.Entry(app,textvariable=Deptvalue)
depthname.pack()

button1 = Tkinter.Button(app,text="Click Here",width=20,command=changeLabel)
button1.pack(side='bottom' ,padx=15,pady=15)

app.mainloop()