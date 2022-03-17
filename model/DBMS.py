import sqlite3 as sql
from datetime import date

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
            return True
        except Exception as e:
            return False

    def addTasting(self, tasteNotes: str, points: int, userID: int, roastedCoffeeID: int) -> bool:
        """
        Adds a tasting created by the user
        :param tasteNotes:
        :param points:
        :param tastingDate:
        :param userID:
        :param roastedCoffeeID:
        :return:
        """
        tastingDate = date.today()
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

        self.getCon().commit()

        return countryList

    def getRoastedCoffees(self) -> list[dict]:
        roastedCoffeeList = []
        cursor = self.getCursor()

        query = """
                SELECT RoastedCoffee.roastedCoffeeID, RoastedCoffee.name, CoffeeRoastery.name FROM RoastedCoffee
                INNER JOIN CoffeeRoastery on RoastedCoffee.roastaryID
                WHERE RoastedCoffee.roastaryID == CoffeeRoastery.roastaryID
                """

        for row in cursor.execute(query):
            roastedCoffeeID, coffeeName, roasteryName = row
            result = {
                "roastedCoffeeID": roastedCoffeeID,
                "coffeeName": coffeeName,
                "roasteryName": roasteryName
            }
            roastedCoffeeList.append(result)

        self.getCon().commit()
        return roastedCoffeeList

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


class Main():
    def __init__(self):
        pass

    def loginAndRegister(self):
        userInput = str(input("Enter your email: "))
        userInput = userInput.lower()

        ret = Retrieve()
        ins = Insert()

        if ret.registeredEmail(userInput):
            # If email is already in use
            users = ret.getUsers()
            password = str(input("Enter password: "))

            user = list(filter(lambda row: row.getEmail() == userInput and row.getPassword() == password, users))

            while len(user) == 0:
                password = str(input("Incorrect password! Try again: "))
                user = list(filter(lambda row: row.getEmail() == userInput and row.getPassword() == password, users))

            print("Logged in\n")
            return user[0]
        else:
            # If email is not in use
            email = userInput
            password = str(input("Enter a password: "))
            firstName = str(input("Enter your first name: "))
            surname = str(input("Enter your surname: "))

            print("\nSelect a country from the list of countries")

            for row in ret.getCountries():
                print(row.getName())

            countryInput = str(input("\nEnter country: "))
            country = list(filter(lambda row: row.getName() == countryInput, ret.getCountries()))

            while len(country) == 0:
                # This does not work properly
                countryInput = str(input("Could not find any matches. Enter a country: "))
                country = list(filter(lambda row: row.getName() == countryInput, ret.getCountries()))

            country = country[0]

            ins.addUser(email, password, firstName, surname, country.getCountryID())
            print("\nUser registered")
            self.loginAndRegister()

    def bh1(self):
        user = self.loginAndRegister()

        ret = Retrieve()
        ins = Insert()
        result = ret.getRoastedCoffees()

        print("Select a roastery from the list")

        for row in result:
            print(f"\t=> {row['roasteryName']}")

        userInput = str(input("\nEnter desired roastery: "))
        roasteryMatches = list(filter(lambda row: row['roasteryName'] == userInput, result))
        if len(roasteryMatches) == 0:
            print("No matches")
            return

        print(f"\nSelect a coffee from the roastery {userInput}")

        for row in roasteryMatches:
            print(f"\t=> {row['coffeeName']}")

        userInput = str(input("\nEnter desired coffee: "))
        roastedCoffee = list(filter(lambda row: row['coffeeName'] == userInput, roasteryMatches))

        if len(roastedCoffee) == 0:
            print("No matches")
            return

        roastedCoffee = roastedCoffee[0]

        userID = user.getUserID()
        roastedCoffeeID = roastedCoffee['roastedCoffeeID']

        points = int(input("Enter points: "))

        while not (0 <= points <= 10):
            points = int(input("Points has to be between 0 and 10. Enter points: "))

        tasteNote = str(input("Enter taste note: "))

        try:
            if ins.addTasting(tasteNote, points, userID, roastedCoffeeID):
                print("\nAdded tasting")
            else:
                print("\nFailed to add tasting")
        except Exception as e:
            print("Error:", e)


main = Main()
main.bh1()
