#!/usr/bin/python

class IphoneSE:

    def __init__(self):
        print ('IphoneSE constructor invoked ...')

    def printSpec(self):
        print ('Vendor : '+ 'Apple')
        print ('Model : '+ 'Iphone SE')
        print ('Front Camera : ' + 'Yes')

class Iphone7(IphoneSE):
#above class iphone7 inherits the feature of iphonese

    def __init__(self):
        IphoneSE.__init__(self)
        print ('Iphone7 Constructor invoked ..')

    def printSpec(self):
        IphoneSE.printSpec(self)
        print ('Rear Camera : ' + 'Yes')

def main():
    iPhone7 = Iphone7()
    iPhone7.printSpec()
    

main()

