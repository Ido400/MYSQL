import mysql.connector 
import logging as log

class mysql:
    def __init__(self, host, user, pass_=None):
        self.host = host
        self.user = user
        self.pass_ = pass_
        self.database = database
    
    def connect(self):
        self.mydb = mysql.connector.connect(
            host=f"{self.host}",
            user=f"{self.user}",
            pass_=f"{self.pass_}",
        )
        self.mycursor = self.mydb.cursor()
    
    def connect(self, database):
        self.mydb = mysql.connector.connect(
            host=f"{self.host}",
            user=f"{self.user}",
            pass_=f"{self.pass_}",
            database=f"{database}"      
        )
        self.mycursor = self.mydb.cursor()
    
    def reconnect_db(self):
        self.mydb.reconnect(attempts=1, delay=0)
    

    def insert(self, newList, tableObject):
        self.reconnect_db()
        valueInsert = self.valueInsert(newList)
        table = tableObject.getColumes()
        tableS = tableObject.getColumes()
        sql = f"INSERT INTO {tableObject.tableName} {table} VALUES {valueInsert}" 
        self.mycursor.execute(sql)
        self.mydb.commit()
    

    def __valueInsert(self, newList):
        valueInsert = f"("
        for i, value in enumerate(newList):
            if(i < len(newList)):
                valueInsert = valueInsert +  f"{value},"
            else:
                valueInsert = valueInsert + f"{value})"
        return valueInsert

    def select(self, tableObject, selectColumes="*"):
        if(type(selectColumes) != str):
            columes = self.__valueInsert(selectColumes)
        else:
            columes = selectColumes
        sql = f"SELECT {columes} FROM {tableObject.tableName}"
        mycursor.execute(sql)
        myreasult = mycursor.fetchall()
        return myreasult
    
    def select(self, tableObject, whereList, selectColumes="*"):
        if(type(selectColumes) != str):
            columes = self.__valueInsert(selectColumes)
        else:
            columes = selectColumes
        where = self.__whereList(whereList)
        sql = f"SELECT {columes} FROM {tableObject.tableName} WHERE {where}"
        self.mycursor.execute(sql)
        myreasult = self.mycursor.fetchall()
        return myreasult

    def  __whereList(self, whereList):
        whereString = f""
        if(len(whereList) == 1):
            return f"{whereList[0]}"
        for i, where in enumerate(whereList):
            if(i < len(whereList)):
                whereString = whereString + f"{where} AND"
            else:
                whereString = whereString + f"{where}"
        return whereString

    def delete(self, tableObject, whereList):
        where = self.__whereList(whereList)
        sql = f"DELETE FROM {tableObject.tableName} WHERE {where}"
        self.mycursor.execute(sql)
        self.mydb.commit()
    
    def upadte(self, tableObject, updateList, whereList):
        where = self.__whereList(whereList)
        update = self.__whereList(updateList)
        sql = f"UPDATE {tableObject.tableName} SET {update} WHERE {where}"
        self.mycursor.execute(sql)
        self.mydb.commit()
    
    def createDB(self, dbObject):
        try:
            sql = f"CREATE DATABASE {dbObject.dbName}"
            self.mycursor.execute(sql)
            self.connect(dbObject.dbName)
            self.__createTables(dbObject)
        except Exception as e:
            print(log.ERROR(e))

    def  __createTables(self, dbObject):
        try:
            for table in dbObject.tablesObject:
                tableValues = table.getColumesAndValues()
                sql = "CREATE TABLE {table.tableName} {tableValues}"
                self.mycursor.execute(sql)
        except Exception as e:
            print(log.ERROR(e))

   
                        
