from Tkinter import Tk, Listbox, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style
from view import *
from model import *

'''
Controller: This class is called from the entry point fo the software
It redirects the flow to initHome(), which is a 'view' API to create the 
Home screen.
 
'''

class Controller:
    def __init__(self):
        self.initHome()
        #self.initView()
        
    def initModel(self):
        model=Model()
        
    '''
    Initialize a Home screen
    '''
    def initHome(self):
        root = Tk()
        root.geometry("350x300+300+300")
        home=Home(root)
        root.mainloop()
        
    def initView(self):
        root = Tk()
        root.geometry("350x300+300+300")
        app = View(root)
        root.mainloop()
