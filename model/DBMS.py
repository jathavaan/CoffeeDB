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

        return len(result) > 0

    def getCoffeeByValue(self) -> list[dict]:
        cursor = self.getCursor()
        result = []

        query = """
                select CoffeeRoastery.name, RoastedCoffee.name, RoastedCoffee.kiloPrice, RoastedCoffee.kiloPrice / avg(distinct Tasting.points) from Tasting
                inner join RoastedCoffee on Tasting.roastedCoffeeID
                inner join CoffeeRoastery on RoastedCoffee.roastaryID
                where Tasting.roastedCoffeeID == RoastedCoffee.roastedCoffeeID
                and CoffeeRoastery.roastaryID == RoastedCoffee.roastaryID
                group by Tasting.roastedCoffeeID 
                order by RoastedCoffee.kiloPrice / avg(distinct Tasting.points) asc
                """

        for row in cursor.execute(query):
            roasteryName, coffeeName, kiloPrice, score = row

            data = {
                "roasteryName": roasteryName,
                "coffeeName": coffeeName,
                "kiloPrice": kiloPrice,
                "score": score
            }

            result.append(data)

        self.getCon().commit()
        return result


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
    def bh3(self):
        ret = Retrieve()
        result = ret.getCoffeeByValue()

        print("Here are the coffees that got the highest score compared to price")
        for row in result:
            print("Roastery Name:", row["roasteryName"])
            print("Coffee name:", row["coffeeName"])
            print("Kilo price:", row["kiloPrice"])
            print("Score:", round(row["score"], 2), "\n")


main = Main()
main.bh3()
