import sqlite3 as sql


def initCon() -> sql:
    return sql.connect('../coffeeDB.db')


def createCursor(con: sql.Connection) -> sql.Cursor:
    return con.cursor()


def closeCon(con: sql.Connection):
    con.close()


class Insert:
    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql.Cursor:
        return self.__cursor

    def insertCountry(self, countryName) -> bool:
        pass


class Retrieve:
    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql.Cursor:
        return self.__cursor


class Alter:
    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql:
        return self.__cursor


class Delete:
    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql.Cursor:
        return self.__cursor
