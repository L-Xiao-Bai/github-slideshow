class StringTest(object):
    def _init_(self):
        self.s=""
    def getString(self):
        self.s=input()
    def putString(self):
        print(self.s.upper())

strObj = StringTest()
strObj.getString()
strObj.putString()