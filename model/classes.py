class User:
    def __init__(self, userID: int, email: str, password: str, firstName: str, surname: str, countryID: int):
        self.__userID = None
        self.__email = None
        self.__password = None
        self.__firstName = None
        self.__surname = None
        self.__countryID = None

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
    def __init__(self):
        pass


class Species:
    def __init__(self):
        pass


class RoastedCoffee:
    def __init__(self):
        pass


class Bean:
    def __init__(self):
        pass


class ProcessingMethod:
    def __init__(self):
        pass


class Tasting:
    def __init__(self):
        pass
