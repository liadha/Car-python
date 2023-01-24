import os
from car.logfile import LogFile

class Car:
    def __init__(self):
        self.speed = int(os.getenv('speed'))
        self.gear = int(os.getenv('gear'))
        self.feul = int(os.getenv('feul'))
        self.maxFeul = int(os.getenv('maxFeul'))
        self.km = int(os.getenv('km'))
        self.pricePerLiter = int(os.getenv('pricePerLiter'))
        self.maxPrice = int(os.getenv('maxPrice'))
        self.starter = int(os.getenv('starter'))
        self.logFile = LogFile



    def stopDrive(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if stopDrive function resets the variable
                 :return: pass/failed"""
        #resrt the variable to 0 -> stop drive
        self.speed = 0
        self.gear = 0
        self.starter = 0
        self.inDrive = 0
    def returnSpeed(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
                 this func return the current speed
                 :return: pass/failed"""
        #return the current speed
        return self.speed
    def returnstartMode(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
                 this func return the current started"
                 :return: pass/failed"""
        #return the current started
        return self.starter
    def returninDrive(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
                 this func return the current inDrive"
                 :return: pass/failed"""
        #return the current inDrive
        return self.inDrive
    def returnGear(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
                 this func return the current gear"
                 :return: pass/failed"""
        #return the current gear
        return self.gear
    def addSpeed(self, val):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
                this func update the speed(add)
                 :return: pass/failed"""
        # check if the engine on
        if self.starter == 0:
            raise Exception(os.getenv('car_off_msg'))
        # check if the speed that get is negative or 0
        elif val <= 0:
            raise Exception(os.getenv('val_not_valid_msg'))
        self.speed += val
    def subSpeed(self,val):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this func update the speed(sub)
                 :return: pass/failed"""
        # check if the engine on
        if self.starter == 0:
            raise Exception(os.getenv('car_off_msg'))
        # check if the speed that get is negative
        elif self.speed == 0:
            raise Exception(os.getenv('speed_zero_msg'))
        # check if the speed is 0
        elif val < 0:
            raise Exception(os.getenv('val_not_valid_msg'))
        else:
            self.speed -= val
    def addGear(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this func update the gear(add)
                 :return: pass/failed"""
        # check if the engine on
        if self.starter == 0:
            raise Exception(os.getenv('car_off_msg'))
        # check if the gear on 6
        if self.gear == int(os.getenv('max_gear')):
            raise Exception(os.getenv('gear_msg').format(os.getenv('max_gear')))
        else :
            self.gear += 1
            self.addSpeed(int(os.getenv('speed_per_gear')))
    def subGear(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this func update the gear(sub)
                 :return: pass/failed"""
        # check if the engine on
        if self.starter == 0:
            raise Exception(os.getenv('car_off_msg'))
        # check if the gear is 0
        elif self.gear == 0:
            raise Exception(os.getenv('zero_gear_msg'))
        # check if the gear is 1
        elif self.gear == 1:
            self.gear -= 1
            self.subSpeed(int(os.getenv('speed_per_gear')))
            self.stopDrive()
        else:
            self.gear -= 1
            self.subSpeed(int(os.getenv('speed_per_gear')))

    def addFeul(self,liter):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this function check if it is possible to add feul
                 :return: pass/failed"""

        #Checking if there is enough money for the required amount of liters
        if self.maxPrice < (self.pricePerLiter*liter):
            raise Exception(os.getenv('money_msg').format(self.maxPrice,self.pricePerLiter*liter))
        else:
            self.maxPrice= self.maxPrice-self.pricePerLiter*liter
            self.feul= self.feul+liter


    def returnFeul(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this func return the current feul
                 :return: pass/failed"""
        #return current feul
        return self.feul
    def updateFeul(self,val):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this func update the current feul after drive
                 :return: pass/failed"""
        # check if there is enough feul
        if self.feul == 0:
            raise Exception(os.getenv('feul_msg'))
        # check if tha liter that get is zero or negative
        elif val <=0:
            raise Exception(os.getenv('val_not_valid_msg'))
        self.feul -= val
    def calcKmPerLiter(self,km):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this func convert km to liter
                 :return: pass/failed"""
        # return how many liter needed for the request km
        return km / self.km

    def isItPossiboleToDrive(self, km):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
              this func check if is it enough fuel for the km
                 :return: pass/failed"""
        # check if there is enough feul for the km that send
        if (km // self.km) > self.feul:
            raise Exception(os.getenv('feul_msg'))
        else:
            return 1


    def startDrive(self):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
                this func reset the variable of starter and inDrive to 1
                 :return: pass/failed"""
        # reset engine on and inDrive flag on
        self.inDrive = 1
        self.starter = 1


    def drive(self,km):
        """       name : Liad
                 date : 22/01/2023
                 :param : none
             this func check if it possibole to drive and start drive
                 :return: pass/failed"""
        #check if the engine on
        if self.starter == 0:
            self.startDrive()
        # check if there is enough feul
        if (self.isItPossiboleToDrive(km)) != 1:
            raise Exception(os.getenv('feul_msg'))

        else:
            self.startDrive()
            self.addGear()
            self.addSpeed(int(os.getenv('speed_per_gear')))
            self.updateFeul(self.calcKmPerLiter(km))
            self.stopDrive()










