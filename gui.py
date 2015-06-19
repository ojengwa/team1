import Tkinter
from Tkinter import Menu
import tkMessageBox 
from main import *
import networkx as nx
import matplotlib.pyplot as plt
import sys
from time import clock


reload(sys)
sys.setdefaultencoding("utf-8")
app = None
link = None
depthname = None

def display_gui(web='',dept=1):
    global app, link, depthname
    app =  Tkinter.Tk()
    app.title("LINK ANALYSER")
    app.geometry('450x300+200+200')

    menubar = Menu(app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Quit", command=app.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About Us", command=aboutProject)
    menubar.add_cascade(label="Help", menu=helpmenu)

    app.config(menu=menubar)

    headertext2 = Tkinter.StringVar()
    headertext2.set("")
    label10 = Tkinter.Label(app,textvariable=headertext2,height=1)
    label10.pack()

    headertext = Tkinter.StringVar()
    headertext.set("")
    label0 = Tkinter.Label(app,textvariable=headertext,height=4)
    label0.pack()

    labeltext = Tkinter.StringVar()
    labeltext.set("Website url")
    label1 = Tkinter.Label(app,textvariable=labeltext,height=1)
    label1.pack()

    url = Tkinter.StringVar(None)
    url.set(web)
    link = Tkinter.Entry(app,textvariable=url,)
    link.pack()

    labeltext = Tkinter.StringVar()
    labeltext.set("Depth")
    label1 = Tkinter.Label(app,textvariable=labeltext,height=1)
    label1.pack()

    deptvalue = Tkinter.IntVar(None)
    deptvalue.set(dept)
    depthname = Tkinter.Entry(app,textvariable=deptvalue,text=dept)
    depthname.pack()

    button1 = Tkinter.Button(app,text="Submit",width=20,command=changeLabel)
    button1.pack(side='bottom' ,padx=15,pady=15)

    app.mainloop()


def do_get(site,num):
    start = clock()
    (_ROOT, _DEPTH, _BREADTH) = range(3)
    print site,num
    G=nx.Graph()
    crawl = analyse_web(site,num)



    for child in crawl:
        
        G.add_node(child)
        if crawl[child]['parent'] != 'root':
            
            G.add_edge(crawl[child]['parent'],child)

             # display

    nx.draw(G,node_size=20,alpha=0.5,node_color="blue", with_labels=True)
    #fig, ax = plt.subplots()
    plt.savefig("node_colormap.png") # save as png
    print ("Total time: "+`clock() - start`)
    plt.show()
    
    


def changeLabel():
    global app, link, depthname
    site = link.get()
    num = depthname.get()
    
    if site[:7]!= "http://" and site[:8]!= "https://":
        tkMessageBox.showinfo("Error","The url is invalid")
        return
    elif int(num)<1:
        tkMessageBox.showinfo("Error","The depth should be greater than 1")
        return
    app.destroy()
    
    #display_gui()
    #t1.join()
    do_get(site,num)
    

    display_gui(site,num)
    
