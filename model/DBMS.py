import sqlite3 as sql

from model.classes import User


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

    def addUser(self, email: str, password: str, firstName: str, lastName: str, countryID: int):
        ret = Retrieve()
        email = email.lower()  # Email should be lowercase
        if ret.registeredEmail(email):
            raise ValueError("A user with this email has already been registered")

        cursor = self.getCursor()
        cursor.execute(
            """
            INSERT INTO User (email, password, firstName, surname, countryID) 
            VALUES (?, ?, ?, ?, ?)
            """, (email, password, firstName, lastName, countryID)
        )

        self.getCon().commit()
        self.getCon().close()


class Retrieve:
    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql.Cursor:
        return self.__cursor

    def getUsers(self) -> list[User]:
        userList = []
        cursor = self.getCursor()

        for row in cursor.execute("SELECT * FROM User"):
            userID, email, password, firstName, surname, countryID = row
            userList.append(User(userID, email, password, firstName, surname, countryID))

        self.getCon().commit()
        self.getCon().close()

        return userList

    def registeredEmail(self, email: str) -> bool:
        email = email.lower()

        cursor = self.getCursor()
        result = cursor.execute(
            """
            SELECT * FROM User
            WHERE User.email = ?
            """, (email,)
        ).fetchall()

        self.getCon().commit()
        self.getCon().close()

        return len(result) > 0


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


ret = Retrieve()
ins = Insert()

try:
    ins.addUser("test@user.com", "TestUser1234", "Test", "User", 2)
except Exception as e:
    print("Error:", e)

for user in ret.getUsers():
    print(user.getUserID(), "|", user.getFirstName(), user.getSurname())
