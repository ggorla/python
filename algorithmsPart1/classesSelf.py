class testClass:
    def createName(self,name):
        self.name = name

    def displayName(self):
        return  self.name

    def saying(self):
        print("hello %s" % self.name)

first = testClass()
second = testClass()

first.createName('bucky')
second.createName('tony')
first.displayName()
first.saying()
second.saying()
