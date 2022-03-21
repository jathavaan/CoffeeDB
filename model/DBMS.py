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

    def getCoffeeByCountryAndProcessingMethod(self) -> list[dict]:
        cursor = self.getCursor()
        result = []

        query = """
                select CoffeeRoastery.name, RoastedCoffee.name from RoastedCoffee
                inner join CoffeeRoastery on RoastedCoffee.roastaryID == CoffeeRoastery.roastaryID
                inner join CoffeeParty on RoastedCoffee.coffeePartyID == CoffeeParty.coffeePartyID
                inner join Farm on CoffeeParty.producedFarmID == Farm.farmID
                inner join Region on Farm.regionID == Region.regionID
                inner join Country on Region.countryID == Country.countryID
                inner join ProcessingMethod on CoffeeParty.processingMethodID == ProcessingMethod.processingMethodID
                where (Country.name == "Rwanda" or Country.name == "Colombia") 
                and ProcessingMethod.name != "Vasket"
                """

        for row in cursor.execute(query):
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

    def getUniqueTastings(self) -> list[dict]:
        cursor = self.getCursor()
        result = []

        query = """
                select User.firstName, User.surname, count(distinct Tasting.roastedCoffeeID) from Tasting
                inner join User on Tasting.userID
                where User.userID == Tasting.userID
                group by Tasting.userID
                order by count(Tasting.roastedCoffeeID) desc
                """

        for row in cursor.execute(query):
            firstName, surname, count = row

            data = {
                "firstName": firstName,
                "surname": surname,
                "count": count
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
                print("Incorrect email and password. Try again!")
                email = str(input("Enter email: "))
                password = str(input("Enter password: "))
                user = list(
                    filter(lambda row: row.getEmail() == email.lower() and row.getPassword() == password, users))

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
            return None

    def bh1(self):
        user = self.loginAndRegister()

        if not user:
            user = self.loginAndRegister()

        ret = Retrieve()
        ins = Insert()
        result = ret.getRoastedCoffees()

        roasteries = []
        for row in result:
            if row["roasteryName"] not in roasteries:
                roasteries.append(row["roasteryName"])

        print("Select a roastery from the list")

        for roastery in roasteries:
            print(f"\t=> {roastery}")

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

    def bh2(self):
        ret = Retrieve()
        result = ret.getUniqueTastings()

        for row in result:
            print(f"\t=> {row['firstName']} {row['surname']} has tasted {row['count']} unique coffees")

    def bh3(self):
        ret = Retrieve()
        result = ret.getCoffeeByValue()

        print("Here are the coffees that got the highest score compared to price\n")
        for row in result:
            print("\tRoastery Name:", row["roasteryName"])
            print("\tCoffee name:", row["coffeeName"])
            print("\tKilo price:", row["kiloPrice"])
            print("\tScore:", round(row["score"], 2), "\n")

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

    def bh5(self):
        ret = Retrieve()
        result = ret.getCoffeeByCountryAndProcessingMethod()

        print("Showing unwashed coffees from Rwanda and Colombia: ")
        if len(result) == 0:
            print("No matches")
        else:
            for row in result:
                print("Roastery name:", row["roasteryName"])
                print("Coffeename:", row["coffeeName"], "\n")


main = Main()
print("Userstory 1")
main.bh1()
print("\nUserstory 2")
main.bh2()
print("\nUserstory 3")
main.bh3()
print("\nUserstory 4")
main.bh4()
print("\nUserstory 5")
main.bh5()
