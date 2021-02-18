class table:
    def __init__(self, columesName, tableName, columesVaribles):
        self.columesName = columesName
        self.tableName = tableName
        self.columesVaribles = columesVaribles

    def addColume(self, columeName, varible):
        self.columesName.append(columeName)
        self.columesVaribles.append(varible)
    
    def getColumes(self):
        table = f"("
        for i, colume in enumerate(self.columesName):
            if(i < len(self.columesName)):
                table = table + f"{colume},"
            else:
                table = table + f"{colume})"
        return table

    def getColumesS(self):
        table = f"("
        for i, colume in enumerate(self.columesName):
            if(i < len(self.columesName)):
                table = table + f"%s,"
            else:
                table = table + f"%s)"
        return table
        
    def getColumesAndValues(self):
        table = f"("
        for i, colume, var in enumerate(self.columesName),self.columesVaribles:
            if(i < len(self.columesName)):
                table = table + f"{colume} {var},"
            else:
                table = table + f"{colume} {var})"
        return table