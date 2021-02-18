class db:
    def __init__(self, dbName, tablesObject):
        self.dbName = dbName
        self.tablesObject = tablesObject

    def add_table(self, tableObject):
        self.tablesObject.append(tableObject)
    