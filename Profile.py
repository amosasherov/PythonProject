import datetime
from point import Location

class Profile:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.gender = ""
        self.bday = ""
        self.address = {
        "Country": "",
        "City": "",
        "Address": "",
        "Zip": ""}
        self.regiseration_date = datetime.datetime.now()
        self.locations = Location()

    def setName(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def setGender(self, gender):
        self.gender = gender

    def setBirthday(self, bday):
        self.bday = bday

    def setAddress(self, address):
        self.address["Country"] = address["Country"]
        self.address["City"] = address["City"]
        self.address["Address"] = address["Address"]
        self.address["Zip"] = address["Zip"]

    def setHome(self, x, y):
        self.locations.setHome(x, y)
        return True

    def setCurrent(self, x, y):
        self.locations.setCurrent(x, y)
        return True

    def toString(self):
        print("Profile")
        print("name: " + self.fname + " " + self.lname)
        print("Gender: " + self.gender)
        print("Birthday: " + self.bday)
        for x, y in self.address.items():
            print(x + ": " + y)
        self.locations.toString()
        return True
