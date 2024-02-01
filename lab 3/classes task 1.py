class myclass():
    def __init__(self):
        self.input_string= ""
    
    def getString(self):
        self.input_string = input()
        
    def printString(self):
        print(self.input_string.upper())
        
s=myclass()
s.getString()
s.printString()