class Point:
    def __init__(self):
        pass

    def getPoint(self):
        return {"x": self.x, "y": self.y}

    def setPoint(self, x, y):
        self.x = x
        self.y = y
        return True

    def toString(self):
        print("x:" + str(self.x) + " y: " + str(self.y))
        return True


class Location:
    def __init__(self):
        self.home = Point()
        self.current = Point()

    def getHome(self):
        return {"x": self.home.getPoint["x"], "y": self.home.getPoint["y"]}

    def setHome(self, x, y):
        self.home.setPoint(x,y)
        return True

    def getCurrent(self):
        return {"x": self.current.getPoint["x"], "y": self.current.getPoint["y"]}

    def setCurrent(self, x, y):
        self.current.setPoint(x, y)
        return True

    def toString(self):
        print("Home:")
        self.home.toString()
        print("Current:")
        self.current.toString()
        return True
