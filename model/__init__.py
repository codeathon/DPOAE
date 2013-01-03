import MySQLdb

'''
@author: rohit
@summary: 
The Model module defines all the necessary API's to communicate with the 
database.
'''

class Model:
    
    '''
    @summary: 
    Establish a connection with the MySql Database.
    Create a cursor for all the Queries
    '''
    def __init__(self):
        
        self.conn = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                     user="root",  # your username
                      passwd="root123",  # your password
                      db="mysqlq")  # name of the data base
        self.cursor = self.conn.cursor()

    '''
    @summary: 
    This API is used to add a new Experiment to the database.
    @param name: The name of the new Experiment to be added to the database
    @param desc: The textual description of the Experiment
    @param connType: GB / USB are the two types of Connections with the TDT devices
    @param schName: The name of the Schedule associated with the Experiment   
    '''
    def addNewExperiment(self,name,desc,connType,schName):
        self.cursor.execute("INSERT INTO EXPERIMENT(EXPERIMENT_NAME,EXPERIMENT_DESC,EXPERIMENT_CONN_TYPE,SCHEDULE_NAME) VALUES(%s,%s,%s,%s)",(name,desc,connType,schName))
        print(self.cursor.rowcount)
        self.conn.commit()
        
    '''
    @summary: 
    This API is used to return a list of all the experiments curerntly
    present in the database 
    '''
    def returnAllExperiments(self):
        query="SELECT * FROM EXPERIMENT"
        self.cursor.execute(query)
        rows=self.cursor.fetchall()
        return rows
    
    '''
    @summary: 
    This API is used to add a new Schedule to the database.
    
    @param name: The name of the new schedule to be added to the database.
    @param desc: The description of the new schedule to be added to the database.
    @param isi: The Inter Stimilus Interval of the new Schedule to be added to the database.
    @param numOfBlocks: The Number of times the schedule needs to be repeated.
    @param exp: The experiment associated with this schedule
    '''
    def addNewSchedule(self,name,desc,isi,numOfBlocks,exp):
        self.cursor.execute("INSERT INTO SCHEDULE(SCHEDULE_NAME,SCHEDULE_DESC,SCHEDULE_ISI, SCHEDULE_NUM_OF_BLOCKS,SCHEDULE_EXPERIMENT) VALUES(%s,%s,%s,%s,%s)",(name,desc,isi,numOfBlocks,exp))
        self.conn.commit()
        print(self.cursor.rowcount)

    '''
    @summary:
    This API is used to add the parameters of an experiment to the database
    
    @param deviceType: The type of the TDT device associated with this Experiment. It could
                    be one of the following:
                    1. RP6
                    2. RX6
                    3. RP5
                    4. RX5
                    5. RZ5
                    6. RZ6
                    7. RX7
                    8. RX8
                    9. RM1
                    10.RP2
                    There could be more, please confirm.
                    
    @param deviceID: The deviceID can be specified by the user
    @param rpvds: The path to the rpvds file is stored in this parameter 
    '''
    def addNewExperimentParameter(self,deviceType,deviceID,rpvds):
        self.cursor.execute("INSERT INTO EXPERIMENT_PARAMS(EXPERIMENT_PARAMS_DEVICE_TYPE,EXPERIMENT_PARAMS_DEVICE_ID,EXPERIMENT_PARAMS_RPVDS) VALUES(%s,%s,%s)",(deviceType,deviceID,rpvds))
        self.conn.commit()
        print(self.cursor.rowcount)
        
    '''
    @summary: 
    This API is used to add a new Scheduler Parameter 
    This goes to a different table called 'SCHEDULE_PARAMS' in the database
    All the paramsX are specified by the user of the system. 
    '''
    def addNewScheduleParameter(self,param1,module1,value1,param2,module2,value2,param3,module3,value3,param4,module4,value4,schName):
        self.cursor.execute("INSERT INTO SCHEDULE_PARAMS(SCHEDULE_PARAMS_NAME,SCHEDULE_PARAMS_MODULEID,SCHEDULE_PARAMS_VALUE,SCHEDULE_NAME) VALUES(%s,%s,%s,%s)",(param1,module1,value1,schName))
        self.cursor.execute("INSERT INTO SCHEDULE_PARAMS(SCHEDULE_PARAMS_NAME,SCHEDULE_PARAMS_MODULEID,SCHEDULE_PARAMS_VALUE,SCHEDULE_NAME) VALUES(%s,%s,%s,%s)",(param2,module2,value2,schName))
        self.cursor.execute("INSERT INTO SCHEDULE_PARAMS(SCHEDULE_PARAMS_NAME,SCHEDULE_PARAMS_MODULEID,SCHEDULE_PARAMS_VALUE,SCHEDULE_NAME) VALUES(%s,%s,%s,%s)",(param3,module3,value3,schName))
        self.cursor.execute("INSERT INTO SCHEDULE_PARAMS(SCHEDULE_PARAMS_NAME,SCHEDULE_PARAMS_MODULEID,SCHEDULE_PARAMS_VALUE,SCHEDULE_NAME) VALUES(%s,%s,%s,%s)",(param4,module4,value4,schName))       
        self.conn.commit()
        print(self.cursor.rowcount)
        
    '''
    @summary: 
    This API returns all the Schedules currently available in the database.
    '''
    def returnAllSchedules(self):
        query="SELECT * FROM SCHEDULE"
        self.cursor.execute(query)
        rows=self.cursor.fetchall()
        return rows
    
    '''
    @summary: 
    This API returns the list of Schedules associated with a particular Experiment
    '''
    def returnScheduleListForExperiment(self,exp):
        self.cursor.execute("SELECT * FROM SCHEDULE WHERE SCHEDULE_EXPERIMENT=%s",(exp))
        rows=self.cursor.fetchall()
        return rows
    
    '''
    @summary: 
    This API returns a list of Parameters for a particular Schedule
    '''
    def returnListParam(self,sch):
        self.cursor.execute("SELECT * FROM SCHEDULE_PARAMS WHERE SCHEDULE_NAME=%s",(sch))
        rows=self.cursor.fetchall()
        return rows