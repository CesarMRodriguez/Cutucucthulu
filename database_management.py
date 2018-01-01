from pymongo import MongoClient

class DatabaseConnection:

    def __init__(self,dbHost,dbPort):
        self.connection = MongoClient(dbHost, dbPort)
        self.db = self.connection.reconmaster
    
    def close(self):
        self.connection.close()

    def printVersion(self):
        server_info = self.connection.server_info()
        return server_info

    def getWorkspaces(self):
        workspaceList = []
        for config_val in  self.db.workspaces.find():
            workspaceList.append(config_val['name'])
        if len(workspaceList) == 0:
            self.createWorkspace("default")
            workspaceList.append("default")
        return workspaceList
        

    def createWorkspace(self, workspace):
        self.db.workspaces.insert_one({"name":workspace})

    def deleteWorkspace(self, workspace):
        result = self.db.workspaces.delete_one({"name":workspace})
        if result.deleted_count == 1:
            print 'Workspace deleted successfully'

    def initDatabase(self):
        res = self.db.workspaces.find_one({"name":"default"})
        if res == None:
            self.createWorkspace("default")