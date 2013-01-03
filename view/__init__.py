from Tkinter import *
from ttk import *
import tkMessageBox
import MySQLdb
from controller import *
from model import *
from execute import *

def newClick():
    root = Tk()
    root.geometry("350x300+300+300")
    appn = CreateNewExperiment(root)
    root.mainloop()

def listClick(e):
    list = e.widget
    index = (int)(list.curselection()[0])
    value = list.get(index)
    tkMessageBox.showinfo("Experiment details", "Experiment " + str(value))

class View(Frame):             
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
            
    def initUI(self):
        self.parent.title("Control Panel")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
    
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(6, pad=7)
            
        lbl = Label(self, text="Experiments")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        area = Listbox(self)
        model = Model()
        rows=model.returnAllExperiments()
        
        area.grid(row=1, column=0, columnspan=2, rowspan=3,
        padx=5, sticky=E + W + S + N)
        for row in rows:
            area.insert(1, ""+row[0])
            area.bind('<<ListboxSelect>>', listClick)
            
        # Display the Experiment details
            
        abtn = Button(self, text="New", command=newClick)
        abtn.grid(row=1, column=3)
    
        cbtn = Button(self, text="Save")
        cbtn.grid(row=2, column=3, pady=4)
            
        hbtn = Button(self, text="Add")
        hbtn.grid(row=4, column=3, padx=5)
    
        obtn = Button(self, text="Remove")
        obtn.grid(row=5, column=3)  
        
def onClickExperiment():
    root = Tk()
    root.geometry("350x300+300+300")
    appExp = View(root)
    root.mainloop()

def onClickSchedule():
    root = Tk()
    root.geometry("350x300+300+300")
    appSch = Schedule(root)
    root.mainloop()
 
def onClickRun():
    root = Tk()
    root.geometry("350x300+300+300")
    appRun = Run(root)
    root.mainloop()

class Home(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initModel()
        self.initUI()
      
    '''
    Create a new instance of 'model'
    '''  
    def initModel(self):
        model=Model()
        
    '''
    Initialize the content on the Home Screen
    Has 3 buttons
    1. Experiment
    2. Schedules
    3. Run
    '''
    def initUI(self):
        self.parent.title("Control Panel")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
    
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(6, pad=7)
        
        '''
        Experiment Button
        '''
        experiments = Button(self,text="EXPERIMENT", command=onClickExperiment)
        experiments.grid(row=0,column=0,sticky=W)
        
        '''
        Schedules Button
        '''
        schedules = Button(self, text="SCHEDULES",command=onClickSchedule)
        schedules.grid(row=1,column=0,sticky=W)
        
        '''
        Run Button
        '''
        run = Button(self, text="RUN", command=onClickRun)
        run.grid(row=2,column=0)


class Schedule(Frame):
    
    def onClickNew(self):
        root = Tk()
        root.geometry("350x300+300+300")
        appNewSch = CreateSchedule(root)
        root.mainloop()
    
    def listDetailClick(self,e):
        listExp = e.widget
        index = (int)(listExp.curselection()[0])
        value = listExp.get(index)
        rows=Model().returnListParam(value)
        for row in rows:
            self.param1var=StringVar()
            self.param1lb=Label(self,textvariable=self.param1var)
            self.param1lb.grid(row=4,column=0)
            self.param1var.set(row[0])
            self.param1val.set(row[3])
            
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        
        
    '''
    Initialize the UI for the Schedules 
    '''
    def initUI(self):
        
        self.parent.title("Schedules")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
    
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(6, pad=7)
        
        '''
        List of all existing schedules for updating
        Make a call to the Model api 'returnAllSchedules()'
        '''
        self.area2 = Listbox(self)
        modelrun = Model()
        rowsrun=modelrun.returnAllSchedules()
        for row in rowsrun:
            self.area2.insert(1, ""+row[0])
            self.area2.bind('<<ListboxSelect>>', self.listDetailClick)
            
        self.area2.grid(row=0, column=0,columnspan=2, rowspan=3, padx=5, sticky=E + W + S + N)
        
        self.param1var=StringVar()
        self.param1lb=Label(self,textvariable=self.param1var)
        self.param1lb.grid(row=4,column=0)
        
        self.param1val=StringVar()
        self.param1vallb=Label(self,textvariable=self.param1val)
        self.param1vallb.grid(row=4,column=1)
        
        self.param2var=StringVar()
        self.param2lb=Label(self,textvariable=self.param2var)
        self.param2lb.grid(row=5,column=0)
        
        self.param2val=StringVar()
        self.param2vallb=Label(self,textvariable=self.param2val)
        self.param2vallb.grid(row=5,column=1)
        
        self.param3var=StringVar()
        self.param3lb=Label(self,textvariable=self.param3var)
        self.param3lb.grid(row=6,column=0)
        
        self.param3val=StringVar()
        self.param3vallb=Label(self,textvariable=self.param3val)
        self.param3vallb.grid(row=6,column=1)
        
        self.param4var=StringVar()
        self.param4lb=Label(self,textvariable=self.param4var)
        self.param4lb.grid(row=7,column=0)
        
        self.param4val=StringVar()
        self.param4vallb=Label(self,textvariable=self.param4val)
        self.param4vallb.grid(row=7,column=1)
        
        '''
        Button to create a new Schedule
        '''
        new=Button(self,text="New",command=self.onClickNew)
        new.grid(row=8,column=0)
        
        '''
        Save button to save the new/updated schedule
        '''
        save=Button(self,text="Save")
        save.grid(row=9,column=0)
         

class CreateSchedule(Frame):
    
    def onSave(self):
        model=Model()
        model.addNewSchedule(self.scheduleNameText.get(),self.scheduleDescriptionText.get(),self.interStimulusIntervalText.get(),self.numberOfTrialBlocksText.get(),self.area.get(self.area.curselection()[0]))
        model.addNewScheduleParameter(self.parameterNameText.get(),self.moduleIDText.get(),self.valueText.get(),self.parameterNameText2.get(),self.moduleIDText2.get(),self.valueText2.get(),self.parameterNameText3.get(),self.moduleIDText3.get(),self.valueText3.get(),self.parameterNameText4.get(),self.moduleIDText4.get(),self.valueText4.get(),self.scheduleNameText.get())
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("New Schedule")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
    
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(6, pad=7)
        
        scheduleName = Label(self, text="Schedule Name")
        scheduleName.grid(row=0,column=0)
        self.scheduleNameText = Entry(self)
        self.scheduleNameText.grid(row=0,column = 2)
        
        scheduleDescription = Label(self, text="Schedule Description")
        scheduleDescription.grid(row=1,column=0)
        self.scheduleDescriptionText = Entry(self)
        self.scheduleDescriptionText.grid(row=1,column=2)
        
        scheduleExperiment = Label(self, text="Experiment")
        scheduleExperiment.grid(row=0, column=3)
        
        self.area = Listbox(self)
        modelsch = Model()
        rowssch=modelsch.returnAllExperiments()
        
        self.area.grid(row=0, column=4,columnspan=2, rowspan=3, padx=5, sticky=E + W + S + N)
        for row in rowssch:
            self.area.insert(1, ""+row[0])
        
        numberOfTrialBlocks = Label(self, text="Number of trial blocks")
        numberOfTrialBlocks.grid(row = 2, column = 0)
        self.numberOfTrialBlocksText = Entry(self)
        self.numberOfTrialBlocksText.grid(row = 2, column = 2)
        
        interStimulusInterval = Label(self, text="Inter Stimulus Interval")
        interStimulusInterval.grid(row = 3, column = 0)
        self.interStimulusIntervalText = Entry(self)
        self.interStimulusIntervalText.grid(row=3, column = 2)
        
        scheduleParameters = Label(self, text = "Parameters")
        scheduleParameters.grid(row=4,column=0)
        
        parameterName = Label(self, text="Parameter Name")
        parameterName.grid(row=5,column=0)
        
        moduleID = Label(self, text = "Module ID")
        moduleID.grid(row=5, column=2,sticky=W)
        
        value = Label(self, text="Value")
        value.grid(row=5,column=4,sticky=W)
        
        self.parameterNameText = Entry(self)
        self.parameterNameText.grid(row=6,column=0,sticky=W)
        
        self.moduleIDText = Entry(self)
        self.moduleIDText.grid(row=6, column=2,sticky=W)
        
        self.valueText = Entry(self)
        self.valueText.grid(row=6,column=4,sticky=W)
        
        self.parameterNameText2 = Entry(self)
        self.parameterNameText2.grid(row=7,column=0,sticky=W)
        
        self.moduleIDText2 = Entry(self)
        self.moduleIDText2.grid(row=7, column=2,sticky=W)
        
        self.valueText2 = Entry(self)
        self.valueText2.grid(row=7,column=4,sticky=W)

        self.parameterNameText3 = Entry(self)
        self.parameterNameText3.grid(row=8,column=0,sticky=W)
        
        self.moduleIDText3 = Entry(self)
        self.moduleIDText3.grid(row=8, column=2,sticky=W)
        
        self.valueText3 = Entry(self)
        self.valueText3.grid(row=8,column=4,sticky=W)

        self.parameterNameText4 = Entry(self)
        self.parameterNameText4.grid(row=9,column=0,sticky=W)
        
        self.moduleIDText4 = Entry(self)
        self.moduleIDText4.grid(row=9, column=2,sticky=W)
        
        self.valueText4 = Entry(self)
        self.valueText4.grid(row=9,column=4,sticky=W)

        save = Button(self,text="Save",command=self.onSave)
        save.grid(row=10,sticky=E)
        
    
'''
@summary: 
This class needs to be implemented
Please refer to the 'test' package for a sample code on how to 
run a test experiment to communicate the parameters entered by the user
with the TDT machines
'''
class Run(Frame):
    
    def listExpClick(self,e):
        listExp = e.widget
        index = (int)(listExp.curselection()[0])
        self.value = listExp.get(index)
        rows=Model().returnScheduleListForExperiment(self.value)
        self.area2.unbind(self, None)
        self.area2.delete(0, self.area2.size())
        for row in rows:
            self.area2.insert(1, ""+row[0])      
    
    def listSchClick(self,e):
        listSch = e.widget
        index = (int)(listSch.curselection()[0])
        self.schVal = listSch.get(index)
        self.rowsSchParams=Model().returnListParam(self.schVal)
    
    def finalRun(self):
        for row in self.rowsSchParams:
            self.exeParams=row[0]+"="+row[3]+"\n"
        exe=Execute()
        exe.execute(self.exeParams)
        
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Control Panel")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
    
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(6, pad=7)
        
        self.area = Listbox(self)
        modelrun = Model()
        rowsrun=modelrun.returnAllExperiments()
        
        self.area.grid(row=0, column=0,columnspan=2, rowspan=3, padx=5, sticky=E + W + S + N)
        for row in rowsrun:
            self.area.insert(1, ""+row[0])
            self.area.bind('<<ListboxSelect>>', self.listExpClick)
        
        self.area2 = Listbox(self)
        modelrun = Model()
        rowsrun=modelrun.returnAllSchedules()
        for row in rowsrun:
            self.area2.insert(1, ""+row[0])
            #self.area.bind('<<ListboxSelect>>', self.listSchClick)
        self.area2.grid(row=0, column=4,columnspan=2, rowspan=3, padx=5, sticky=E + W + S + N)
        self.exeParams
        
        run=Button(self,text="Run",command=self.finalRun)
        run.grid(row=4,column=0,sticky=W)

'''
@summary: 
This class is used to create a new Experiment 
'''        
class CreateNewExperiment(Frame):
    
    '''
    @summary: 
    called on clikc of the submit button
    make calls to addNewExperiment() & addNewExperimentParmaters() with the 
    respective arguments
    '''
    def onSubmit(self):
        model = Model()
        model.addNewExperiment(self.nameText.get(),self.expDescText.get(),self.var.get(),self.area.get(self.area.curselection()[0]))
        model.addNewExperimentParameter(self.var2.get(),self.expParamDeviceIDEntry.get(),self.expParamRPVDSText.get())
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        
    '''
    @summary: 
    Initialize the GUI with proper elements
    '''
    def initUI(self):
        self.parent.title("New Experiment")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
    
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(6, pad=7)
              
        name = Label(self, text="Experiment Name:")
        name.grid(row=0,column=0,pady=10,padx=10)
        
        varText = StringVar()
        self.nameText = Entry(self)
        self.nameText.grid(row=0,column=1,pady=10,padx=30, sticky=W)
        #self.nameText.set(self.nameText.get())
        
        self.expDesc = Label(self, text="Description")
        self.expDesc.grid(row=0,column=3,pady=10,padx=10)

        varDescText = StringVar()
        self.expDescText = Entry(self)
        self.expDescText.grid(row=0,column=5,padx=10,pady=10,sticky=E)
        #self.expDescText.set(self.expDescText.get())
        
        self.connType = Label(self, text="Connection Type:")
        self.connType.grid(row=1,column=0,pady=10,padx=10)
        
        self.var = StringVar()
        self.var.set("GB")
        self.option = OptionMenu(self, self.var, "GB","USB")
        self.option.grid(row=1,column=1,columnspan=4,pady=10,padx=30,sticky=W)
        
        self.area = Listbox(self)
        model=Model()
        rows=model.returnAllSchedules()
        for row in rows:
            self.area.insert(1,row[0])
        
        self.area.grid(row=1,column=4,padx=10,pady=10)
        
        self.expParam= Label(self, text="Experiment Parameters")
        self.expParam.grid(row=2,column=0,pady=20,padx=10,sticky=W)
        
        self.expParamDeviceType = Label(self, text="Device Type")
        self.expParamDeviceType.grid(row=3,column=0,padx=10,sticky=W)
        
        self.expParamDeviceID = Label(self, text="Device ID")
        self.expParamDeviceID.grid(row=3,column=2,padx=10,sticky=W)
        
        self.expParamRPVDS = Label(self, text = "RPVD's")
        self.expParamRPVDS.grid(row=3, column=4,padx=10,sticky=W)
        
        self.var2= StringVar()
        self.var2.set("RX6")
       
        self.expParamDeviceTypeOption = OptionMenu(self,self.var2,"RX6","RP6","RP5","RX5","RZ5","RZ6","RX7","RX8","RM1","RP2")
        self.expParamDeviceTypeOption.grid(row=4, column=0,columnspan=4,padx=10,pady=10,sticky=W)
        
        self.expParamDeviceIDEntry = Entry(self)
        self.expParamDeviceIDEntry.grid(row=4, column=2,padx=10,pady=10,sticky=W)
        
        self.expParamRPVDSText = Entry(self)
        self.expParamRPVDSText.grid(row=4,column=4,padx=10,pady=10,sticky=W)
        
        add = Button(self, text="Add")#, command=addParameter)
        add.grid(row=5, sticky=W)
        remove = Button(self,text="Remove")#,command=removeParameter)
        remove.grid(row=6,sticky=W)
                
        submit = Button(self,text="Submit",command=self.onSubmit)
        submit.grid(row=7,sticky=E)