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


class Region:
    def __init__(self, regionID: int, name: str, countryID: int):
        self.__regionID = None
        self.__name = None
        self.__countryID = None

        self.setRegionID(regionID)
        self.setName(name)
        self.setCountryID(countryID)

    def getRegionID(self) -> int:
        return self.__regionID

    def setRegionID(self, regionID: int):
        self.__regionID = regionID

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getCountryID(self) -> int:
        return self.__countryID

    def setCountryID(self, countryID: int):
        self.__countryID = countryID


class Farm:
    def __init__(self, farmID: int, name: str, masl: int, regionID: int):
        self.__farmID = None
        self.__name = None
        self.__masl = None  # meters above sea level
        self.__regionID = None

        self.setFarmID(farmID)
        self.setName(name)
        self.setMasl(masl)
        self.setRegionID(regionID)

    def getFarmID(self) -> int:
        return self.__farmID

    def setFarmID(self, farmID: int):
        self.__farmID = farmID

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getMasl(self) -> int:
        return self.__masl

    def setMasl(self, masl: int):
        self.__masl = masl

    def getRegionID(self) -> int:
        return self.__regionID

    def setRegionID(self, regionID: int):
        self.__regionID = regionID


class CoffeeRoastery:
    def __init__(self, roasteryID: int, name: str):
        self.__roasteryID = None
        self.__name = None

        self.setRoasteryID(roasteryID)
        self.setName(name)

    def getRoasteryID(self) -> int:
        return self.__roasteryID

    def setRoasteryID(self, roasteryID: int):
        self.__roasteryID = roasteryID

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name


class Species:
    def __init__(self, speciesID: int, name: str):
        self.__speciesID = None
        self.__name = None

        self.setSpeciesID(speciesID)
        self.setName(name)

    def getSpeciesID(self) -> int:
        return self.__speciesID

    def setSpeciesID(self, speciesID: int):
        self.__speciesID = speciesID

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name


class RoastedCoffee:
    def __init__(self, roastedCoffeeID: int, name: str, roastnessDegree: str, kiloPrice: float, description: str, coffeePartyID: int,
                 roasteryID: int, roastedDate: datetime.date):
        self.__roastedCoffeeID = None
        self.__name = None
        self.__roastnessDegree = None
        self.__kiloPrice = None
        self.__description = None
        self.__coffeePartyID = None
        self.__roastedDate = None
        self.__roasteryID = None

        self.setRoastedCoffeeID(roastedCoffeeID)
        self.setName(name)
        self.setRoastnessDegree(roastnessDegree)
        self.setKiloPrice(kiloPrice)
        self.setDescription(description)
        self.setCoffeePartyID(coffeePartyID)
        self.setRoastedDate(roastedDate)
        self.setRoasteryID(roasteryID)

    def getRoastedCoffeeID(self) -> int:
        return self.__roastedCoffeeID

    def setRoastedCoffeeID(self, roastedCoffeeID: int):
        self.__roastedCoffeeID = roastedCoffeeID

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getRoastnessDegree(self) -> str:
        return self.__roastnessDegree

    def setRoastnessDegree(self, roastnessDegree: str):
        self.__roastnessDegree = roastnessDegree

    def getKiloPrice(self) -> float:
        return self.__kiloPrice

    def setKiloPrice(self, kiloPrice: float):
        self.__kiloPrice = kiloPrice

    def getDescription(self) -> str:
        return self.__description

    def setDescription(self, description: str):
        self.__description = description

    def getCoffeePartyID(self) -> int:
        return self.__coffeePartyID

    def setCoffeePartyID(self, coffeePartyID: int):
        self.__coffeePartyID = coffeePartyID

    def getRoastedDate(self) -> datetime.date:
        return self.__roastedDate

    def setRoastedDate(self, roastedDate: datetime.date):
        self.__roastedDate = roastedDate

    def getRoasteryID(self) -> int:
        return self.__roasteryID

    def setRoasteryID(self, roasteryID: int):
        self.__roasteryID = roasteryID

    class Bean:
        def __init__(self, beanID: int, name: str, speciesID: int):
            self.__beanID = None
            self.__name = None
            self.__speciesID = None

            self.setBeanID(beanID)
            self.setName(name)
            self.setSpeciesID(speciesID)

        def getBeanID(self) -> int:
            return self.__beanID

        def setBeanID(self, beanID: int):
            self.__beanID = beanID

        def getName(self) -> str:
            return self.__name

        def setName(self, name: str):
            self.__name = name

        def getSpeciesID(self) -> int:
            return self.__speciesID

        def setSpeciesID(self, speciesID: int):
            self.__speciesID = speciesID


class ProcessingMethod:
    def __init__(self, processingMethodID: int, name: str, description: str):
        self.__processingMethodID = None
        self.__name = None
        self.__description = None

        self.setProcessingMethodID(processingMethodID)
        self.setName(name)
        self.setDescription(description)

    def getProcessingMethodID(self) -> int:
        return self.__processingMethodID

    def setProcessingMethodID(self, processingMethodID):
        self.__processingMethodID = processingMethodID

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getDescription(self) -> str:
        return self.__description

    def setDescription(self, description: str):
        self.__description = description


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


class FarmHasBean:
    def __init__(self, farmID: int, beanID: int):
        self.__farmID = None
        self.__beanID = None

        self.setFarmID(farmID)
        self.setBeanID(beanID)

    def getFarmID(self) -> int:
        return self.__farmID

    def setFarmID(self, farmID: int):
        self.__farmID = farmID

    def getBeanID(self) -> int:
        return self.__beanID

    def setBeanID(self, beanID: int):
        self.__beanID = beanID


class CoffeePartyHasBean:
    def __init__(self, coffeePartyID: int, beanID: int):
        self.__coffeePartyID = None
        self.__beanID = None

        self.setCoffeePartyID(coffeePartyID)
        self.setBeanID(beanID)

    def getCoffeePartyID(self) -> int:
        return self.__coffeePartyID

    def setCoffeePartyID(self, coffeePartyID: int):
        self.__coffeePartyID = coffeePartyID

    def getBeanID(self) -> int:
        return self.__beanID

    def setBeanID(self, beanID: int):
        self.__beanID = beanID
