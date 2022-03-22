import datetime


class User:
    """This class need validation"""

    def __init__(self, userID: int, email: str, password: str, firstName: str, surname: str, countryID: int):
        self.__userID = None
        self.__email = None
        self.__password = None
        self.__firstName = None
        self.__surname = None
        self.__countryID = None

        """
        There hasn't been generated any userIDs before all the user-data has been added to the DB. 
        In that case input userID = 0, and which allows the program to reassign userID to 999 999 
        """
        if userID == 0:
            userID = 999_999_999

        self.setUserID(userID)
        self.setEmail(email)
        self.setPassword(password)
        self.setFirstName(firstName)
        self.setSurname(surname)
        self.setCountryID(countryID)

    def getUserID(self) -> int:
        return self.__userID

    def setUserID(self, userID: int):
        if userID <= 0:
            raise TypeError("User ID must be an integer larger than 0")

        self.__userID = userID

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str):
        self.__email = email

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, password: str):
        self.__password = password

    def getFirstName(self) -> str:
        return self.__firstName

    def setFirstName(self, firstName: str):
        self.__firstName = firstName

    def getSurname(self) -> str:
        return self.__surname

    def setSurname(self, surname: str):
        self.__surname = surname

    def getCountryID(self) -> int:
        return self.__countryID

    def setCountryID(self, countryID: int):
        if countryID <= 0:
            raise TypeError("Country ID must be an integer larger than 0")

        self.__countryID = countryID


class Country:
    def __init__(self, countryID: int, name: str):
        self.__countryID = None
        self.__name = None

        self.setCountryID(countryID)
        self.setName(name)

    def getCountryID(self) -> int:
        return self.__countryID

    def setCountryID(self, countryID: int):
        self.__countryID = countryID

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name


class Tasting:
    """This class needs validation"""

    def __init__(self, tastingID: int, tasteNotes: str, points: int, tastingDate: datetime.date, userID: int,
                 roastedCoffeeID: int):
        self.__tastingID = None
        self.__tasteNotes = None
        self.__points = None
        self.__tastingDate = None
        self.__userID = None
        self.__roastedCoffeeID = None

        if tastingID == 0:
            tastingID = 999_999_999

        self.setTastingID(tastingID)
        self.setTasteNotes(tasteNotes)
        self.setPoints(points)
        self.setTastingDate(tastingDate)
        self.setUserID(userID)
        self.setRoastedCoffeeID(roastedCoffeeID)

    def getTastingID(self) -> int:
        return self.__tastingID

    def setTastingID(self, tastingID: int):
        self.__tastingID = tastingID

    def getTasteNotes(self) -> str:
        return self.__tasteNotes

    def setTasteNotes(self, tasteNotes: str):
        self.__tasteNotes = tasteNotes

    def getPoints(self) -> int:
        return self.__points

    def setPoints(self, points: int):
        self.__points = points

    def getTastingDate(self) -> datetime.date:
        return self.__tastingDate

    def setTastingDate(self, tastingDate: datetime.date):
        self.__tastingDate = tastingDate

    def getUserID(self) -> int:
        return self.__userID

    def setUserID(self, userID: int):
        self.__userID = userID

    def getRoastedCoffeeID(self) -> int:
        return self.__roastedCoffeeID

    def setRoastedCoffeeID(self, roastedCoffeeID: int):
        self.__roastedCoffeeID = roastedCoffeeID
