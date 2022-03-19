import sqlite3 as sql
from datetime import datetime

from model.classes import User, Country, Tasting


def initCon() -> sql:
    """
    Initialize connection
    :return connection:
    """
    return sql.connect('../coffeeDB.db')


def createCursor(con: sql.Connection) -> sql.Cursor:
    """
    Creates cursor
    :param con:
    :return cursor:
    """
    return con.cursor()


class Insert:
    """Insert data into DB"""

    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql.Cursor:
        return self.__cursor

    def insertCountry(self, countryName) -> bool:
        pass

    def addUser(self, email: str, password: str, firstName: str, lastName: str, countryID: int) -> bool:
        """
        Adds user to DB

        Checks if inputed data is valid through User class
        Checks if email has already been registered

        :param email:
        :param password:
        :param firstName:
        :param lastName:
        :param countryID:
        :return:
        """
        ret = Retrieve()
        email = email.lower()  # Email should be lowercase
        if ret.registeredEmail(email):
            raise ValueError("A user with this email has already been registered")

        User(0, email, password, firstName, lastName, countryID)
        cursor = self.getCursor()

        try:
            cursor.execute(
                """
                INSERT INTO User (email, password, firstName, surname, countryID) 
                VALUES (?, ?, ?, ?, ?)
                """, (email, password, firstName, lastName, countryID)
            )
            self.getCon().commit()
            self.getCon().close()
            return True
        except Exception as e:
            return False

    def addTasting(self, tasteNotes: str, points: int, tastingDate: datetime.date, userID: int,
                   roastedCoffeeID: int) -> bool:
        """
        Adds a tasting created by the user
        :param tasteNotes:
        :param points:
        :param tastingDate:
        :param userID:
        :param roastedCoffeeID:
        :return:
        """
        Tasting(0, tasteNotes, points, tastingDate, userID, roastedCoffeeID)  # Checks if inputed data is valid
        cursor = self.getCursor()

        try:
            cursor.execute(
                """
                INSERT INTO Tasting (tasteNotes, points, tastingDate, userID, roastedCoffeeID)
                VALUES (?, ?, ?, ?, ?)
                """, (tasteNotes, points, tastingDate, userID, roastedCoffeeID)
            )

            self.getCon().commit()
            self.getCon().close()
            return True
        except Exception as e:
            return False


class Retrieve:
    """Retrieve data from DB"""

    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql.Cursor:
        return self.__cursor

    def getUsers(self) -> list[User]:
        """
        Retrieve all data from DB

        :return userList:
        """
        userList = []
        cursor = self.getCursor()

        for row in cursor.execute("SELECT * FROM User"):
            userID, email, password, firstName, surname, countryID = row
            userList.append(User(userID, email, password, firstName, surname, countryID))

        self.getCon().commit()
        self.getCon().close()

        return userList

    def getCountries(self) -> list[Country]:
        """
        Gets all countries
        :return countryList:
        """
        countryList = []
        cursor = self.getCursor()

        for row in cursor.execute("SELECT * FROM Country"):
            countryID, name = row
            countryList.append(Country(countryID, name))

        return countryList

    def getCoffeeByDescription(self, search: str) -> list[dict]:
        cursor = self.getCursor()
        result = []

        for row in cursor.execute(
                """
                select distinct CoffeeRoastery.name, RoastedCoffee.name from Tasting
                inner join RoastedCoffee on Tasting.roastedCoffeeID
                inner join CoffeeRoastery on RoastedCoffee.roastaryID
                where Tasting.roastedCoffeeID == RoastedCoffee.roastedCoffeeID
                and RoastedCoffee.roastaryID == CoffeeRoastery.roastaryID
                and (Tasting.tasteNotes like ? or RoastedCoffee.description like ?)
                """, ("%" + search + "%", "%" + search + "%")
        ):
            roasteryName, coffeeName = row

            data = {
                "roasteryName": roasteryName,
                "coffeeName": coffeeName
            }

            result.append(data)

        self.getCon().commit()
        return result

    def registeredEmail(self, email: str) -> bool:
        """
        Checks if there are any equal emails in the DB
        :param email:
        :return bool:
        """
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
    """Alter data in DB"""

    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql:
        return self.__cursor


class Delete:
    """Deletes data from DB"""

    def __init__(self):
        self.__con = initCon()
        self.__cursor = createCursor(self.__con)

    def getCon(self) -> sql.Connection:
        return self.__con

    def getCursor(self) -> sql.Cursor:
        return self.__cursor


class Main:
    def bh4(self):
        userInput = str(input("Enter searchword: "))

        ret = Retrieve()
        result = ret.getCoffeeByDescription(userInput)

        if len(result) == 0:
            print("\nNo matches")
            return
        else:
            print("\nReturned the following result(s):")
            for row in result:
                print(f"\t=> Roastery: {row['roasteryName']}\n\t=> Coffee: {row['coffeeName']}\n")


main = Main()
main.bh4()
