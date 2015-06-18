from tkinter import*
import tkinter.messagebox
from main import *
import networkx as nx
import matplotlib.pyplot as plt
import graph


import Tkinter
import tkMessageBox
from main import *
import networkx as nx
import matplotlib.pyplot as plt
import graph
import sys


reload(sys)
sys.setdefaultencoding("utf-8")


def changeLabel():
    site = link.get()
    num = depthname.get()

    headertext.set("Loading data from "+site+", please wait...")


    (_ROOT, _DEPTH, _BREADTH) = range(3)

    G=nx.Graph()
    crawl = analyse_web(site,num)


    for child in crawl:
        print child,crawl[child]
        G.add_node(child)
        if crawl[child]['parent'] != 'root':
            
            G.add_edge(crawl[child]['parent'],child)

             # display

    nx.draw(G,node_size=20,alpha=0.5,node_color="blue", with_labels=True)
    plt.savefig("node_colormap.png") # save as png
    plt.show()

#def aboutProject():
#    tkinter.messagebox.showinfo("A MINI app to display The Web as a graph to Depth n")
#    return


app =  Tkinter.Tk()
app.title("LINK ANALYSER")
app.geometry('450x300+200+200')

#menubar = Menu(app)
#filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Quit", command=app.quit)
#menubar.add_cascade(label="File", menu=filemenu)

#helpmenu = Menu(menubar, tearoff=0)
#helpmenu.add_command(label="About Me", command=aboutProject)
#menubar.add_cascade(label="Help", menu=helpmenu)

#app.config(menu=menubar)

headertext = Tkinter.StringVar()
headertext.set("")
label0 = Tkinter.Label(app,textvariable=headertext,height=4)
label0.pack()

labeltext = Tkinter.StringVar()
labeltext.set("Website url")
label1 = Tkinter.Label(app,textvariable=labeltext,height=1)
label1.pack()

url = Tkinter.StringVar(None)
link = Tkinter.Entry(app,textvariable=url)
link.pack()

labeltext = Tkinter.StringVar()
labeltext.set("Depth")
label1 = Tkinter.Label(app,textvariable=labeltext,height=1)
label1.pack()

deptvalue = Tkinter.IntVar(None)
depthname = Tkinter.Entry(app,textvariable=deptvalue)
depthname.pack()

button1 = Tkinter.Button(app,text="Submit",width=20,command=changeLabel)
button1.pack(side='bottom' ,padx=15,pady=15)

app.mainloop()
def clicked():

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
labeltext.set("Click button to analyse data")
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

button1 = Tkinter.Button(app,text="Click Here",width=20,command=clicked)
button1.pack(side='bottom' ,padx=15,pady=15)

app.mainloop()