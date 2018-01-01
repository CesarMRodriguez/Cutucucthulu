from generic_stage import GenericStage
from database_management import DatabaseConnection
import globals

class StageDB(GenericStage):

    def __init__(self):
        self.prompt = "reconmaster/db_config>"
        self.mainOption = "db_config"

    def getDescription(self):
        return 'db_config: management of parameters and information'

    def printHelp(self):
        self.printGeneralOptions()
        
        print 'Options for DB Stage: '
        print '\tconnect:   change connection to database'
        print '\tcheck:     check the status of the connection to the database'
        print '\tshow:      show the workspaces available to execute the scans'
        print '\tselect:    select the workspace you want to work with'
        print '\tcreate:    create a new workspace to work with'
        print '\tdelete:    removes a workspace'

    def executeOptions(self, value):
        optionFound = False
        if value == 'connect':
            self.selectConnection()
            optionFound = True
        elif value == 'check':  
            self.checkDatabaseState()
            optionFound = True
        elif value == 'show':
            self.showWorkspaces()
            optionFound = True
        elif value == 'select':
            self.selectWorkspace()
            optionFound = True
        elif value == 'create':
            self.createWorkspace()
            optionFound = True
        elif value == 'delete':
            self.deleteWorkspace()
            optionFound = True
        
        if not optionFound:
            print 'The function "' + value + '" does not exist.'

    def selectConnection(self):
        host = raw_input(self.prompt + "Select host of database[127.0.0.1]: ")
        if len(host) == 0:
            host = "127.0.0.1"
        port = raw_input(self.prompt + "Select port of database[27017]: ")
        if len(port) == 0:
            port = 27017
        else:
            port = int(port)
        try: 
            newDb = DatabaseConnection(host,port)
            newDb.printVersion()
            globals.db.close()
            globals.db = newDb
            print("Database was properly reconfigured")
        except:
            print("Error connecting to {}:{}".format(host,str(port)))

    def checkDatabaseState(self):
        try: 
            valor = globals.db.printVersion()
            print("the database is working properly")
        except:
            print("Error in the database connection. Try to reconnect")


    def showWorkspaces(self):
        workspaces = globals.db.getWorkspaces()
        for workspace in workspaces:
            if (workspace == globals.selectedWorkspace):
                print workspace+'*'
            else:
                print workspace

    def selectWorkspace(self):
        workspace = raw_input(self.prompt + "Workspace to select: ")
        #check if the database exists
        workspaces = globals.db.getWorkspaces()
        workspaceFound = False
        for dbworkspace in workspaces:
            if (workspace == dbworkspace):
                workspaceFound = True

        if workspaceFound:
            globals.selectedWorkspace = workspace
        else:
            print("The workspace selected does not exist.")       

    def deleteWorkspace(self):
        workspace = raw_input(self.prompt + "Workspace to delete: ")
        if workspace == "default":
            print 'Default workspace can not be deleted'
            return

        if workspace == globals.selectedWorkspace:
            globals.selectedWorkspace = "default"

        globals.db.deleteWorkspace(workspace)
    
    def createWorkspace(self):
        workspace = raw_input(self.prompt + "Workspace to create: ")
        #check if the database exists
        workspaces = globals.db.getWorkspaces()
        workspaceFound = False
        for dbworkspace in workspaces:
            if (workspace == dbworkspace):
                workspaceFound = True

        if not workspaceFound:
            globals.selectedWorkspace = workspace
            globals.db.createWorkspace(workspace)
        else:
            print("The workspace already exists.")       

