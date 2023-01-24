import os
import unittest
from car.car_class import Car
from dotenv import load_dotenv
from car.logfile import LogFile


class TestCar(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.car = Car()
        self.logFile = LogFile

    def test_stopDrive_BySpeed(self):        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if stopDrive function resets speed
        :return: pass/failed
        """

        try:
            self.car.stopDrive()

            self.assertEqual(self.car.returnSpeed(), 0)
            self.logFile.Log(f'Pass (test_stopDrive_BySpeed): with parameters {self.car.returnSpeed()} ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_stopDrive_BySpeed): {assErr}')

    def test_stopDrive_ByGear(self):
        """
            name : Liad
            date : 22/01/2023
            :param : none
            function that checks if stopDrive function resets the gear
            :return: pass/failed
            """

        try:
            self.car.stopDrive()
            self.assertEqual(self.car.returnGear(), 0)
            self.logFile.Log(f'Pass (test_stopDrive_ByGear): with parameters {self.car.returnGear()}  ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_stopDrive_ByGear): {assErr}')

    def test_stopDrive_ByStartter(self):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if stopDrive function resets the starter
                 :return: pass/failed
                 """

        try:
            self.car.stopDrive()
            self.assertEqual(self.car.returnstartMode(), 0)
            self.logFile.Log(f'Pass (test_stopDrive_ByStartter): with parameters {self.car.returnstartMode()}  ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_stopDrive_ByStartter): {assErr}')


    def test_stopDrive_ByInDrive(self):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if stopDrive function resets the inDrive variable
                 :return: pass/failed
                 """

        try:
            self.car.stopDrive()
            self.assertEqual(self.car.returninDrive(), 0)
            self.logFile.Log(f'Pass (test_stopDrive_ByInDrive): with parameters {self.car.returninDrive()} ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_stopDrive_ByInDrive): {assErr}')

    #---------------------------------------------------------
    def test_addSpeed_0(self):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if addSpeed function add 0 speed
        :return: pass/failed

                        """
        try:
            self.car.startDrive()

            with self.assertRaises(Exception):
                self.car.addSpeed(0)
            self.logFile.Log(f'Pass (test_addSpeed_0): with error raised Exception   ')
        except AssertionError as assErr:
                self.logFile.Log(f'Failed (test_addSpeed_0): {assErr}')
    def test_addSpeed_Negative(self):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if addSpeed function add negative speed
        :return: pass/failed
          """
        try:
            self.car.startDrive()
            with self.assertRaises(Exception):
                self.car.addSpeed(-5)
            self.logFile.Log(f'Pass (test_addSpeed_Negative): with error raised Exception   ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addSpeed_Negative): {assErr}')
    def test_addSpeedStarterFalse(self):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if addSpeed function add speed when the started is off
        :return: pass/failed
          """
        try:
            self.car.stopDrive()
            with self.assertRaises(Exception):
                self.car.addSpeed(20)
            self.logFile.Log(f'Pass (test_addSpeedStartModeFalse): with error raised Exception   ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addSpeedStartModeFalse): {assErr}')
    def test_addSpeedStarterTrue(self):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if addSpeed function add speed when the started is on
        :return: pass/failed
          """
        try :
            self.car.startDrive()
            self.car.addSpeed(20)
            self.logFile.Log(f'Pass (test_addSpeedStarterTrue): with parameters {self.car.returnSpeed()}  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addSpeedStarterTrue): {assErr}')
    #----------------------------------------------------
    def test_subSpeedStarter(self):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if subSpeed function Reduces speed when the started is off
        :return: pass/failed
          """
        try:
            self.car.stopDrive()
            self.car.speed=5
            with self.assertRaises(Exception):
                self.car.addSpeed(20)
            self.logFile.Log(f'Pass (test_subSpeedStarter): with error raised Exception  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subSpeedStarter): {assErr}')

    def test_subSpeed(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subSpeed function Reduces speed
           :return: pass/failed

             """
        try :
            self.car.startDrive()
            self.car.addSpeed(10)
            self.car.subSpeed(5)
            self.assertEqual(self.car.returnSpeed(), 5)
            self.logFile.Log(f'Pass (test_subSpeed): with parameters {self.car.returnSpeed()}  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subSpeed): {assErr}')




    def test_subSpeedNegative(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subSpeed function Reduces negative speed
           :return: pass/failed

             """
        try :
            self.car.startDrive()
            self.car.speed = 20
            with self.assertRaises(Exception):
                self.car.subSpeed(-5)
            self.logFile.Log(f'Pass (test_subSpeedNegative):: with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subSpeedNegative): {assErr}')

    #---------------------------------------------------------
    def test_addGear_starter(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addGear function turn on gear when the starter is off
           :return: pass/failed

             """
        try:
            self.car.stopDrive()
            with self.assertRaises(Exception ):
                self.car.addGear()
            self.logFile.Log(f'Pass (test_addGear_starter): with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addGear_starter): {assErr}')
    def test_addGear_moreThanMax(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addGear function turn on gear more than 6
           :return: pass/failed

             """
        try:
            self.car.startDrive()
            for i in range(int(os.getenv('max_gear'))):
                self.car.addGear()
            with self.assertRaises(Exception):
                self.car.addGear()
            self.logFile.Log(f'Pass (test_addGear_moreThanMax): with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addGear_moreThanMax): {assErr}')
    def test_addGear(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addGear function turn on gear
           :return: pass/failed

             """
        try:
            self.car.startDrive()
            for i in range(3):
                self.car.addGear()
            self.logFile.Log(f'Pass (test_addGear): with parameters {self.car.returnGear()} ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addGear): {assErr}')
    #----------------------------------------------------
    def test_subGear_0(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the current gear is 0
           :return: pass/failed

             """
        try:
            self.car.startDrive()
            with self.assertRaises(Exception):
                self.car.subGear()
            self.logFile.Log(f'Pass (test_subGear_0): with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subGear_0): {assErr}')


    def test_subGearStarter(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the starter is off
           :return: pass/failed

             """
        try:
            self.car.stopDrive()
            with self.assertRaises(Exception):
                self.car.subGear()
            self.logFile.Log(f'Pass (test_subGearStarter): with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subGearStarter): {assErr}')
    def test_subGearWith0Speed(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the speed is 0
           :return: pass/failed

             """
        try :
            self.car.startDrive()
            self.car.gear = 2
            with self.assertRaises(Exception):
                self.car.subGear()
            self.logFile.Log(f'Pass (test_subGearWith0Speed): with error raised Exception  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subGearWith0Speed): {assErr}')

    def test_subGearWithSpeed(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the speed
           :return: pass/failed

             """
        try :
            self.car.startDrive()
            self.car.gear = 2
            self.car.addSpeed(15)
            self.car.subGear()
            self.logFile.Log(f'Pass (test_subGearWithSpeed): with parameters {self.car.returnGear()} ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subGearWithSpeed): {assErr}')
    def test_subGear1(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the gear on 1
           :return: pass/failed

             """
        try :
            self.car.startDrive()
            self.car.gear = 1
            self.assertEqual(self.car.speed, 0)
            self.logFile.Log(f'Pass (test_subGear1): with parameters {self.car.returnSpeed()} ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_subGear1): {assErr}')

    #-------------------------------------------

    def test_addFeul_ByMaxFeulLiter(self):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addFeul function allows to fill more than allowed
           :return: pass/failed

             """
        try:
            with self.assertRaises(Exception):
                self.car.addFeul(100)
            self.logFile.Log(f'Pass (test_addFeul_ByMaxFeulLiter): with error raised Exception  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addFeul_ByMaxFeulLiter): {assErr}')

    def test_addFeu_BylMaxPrice(self):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if addFeul function allows to fill more than max price
             :return: pass/failed

               """
        try:
            self.car.maxPrice=20
            with self.assertRaises(Exception):
                self.car.addFeul(30)
            self.logFile.Log(f'Pass (test_addFeu_BylMaxPrice): with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addFeu_BylMaxPrice): {assErr}')
    def test_addFeul(self):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if addFeul function allows to fill feul
             :return: pass/failed

               """
        try:
            self.car.addFeul(50)
            self.logFile.Log(f'Pass (test_addFeul): with parameters {self.car.returnFeul()} ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_addFeul): {assErr}')
    #----------------------------------------------------
    def test_updateFeulNegative(self):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update negative liter after drive
             :return: pass/failed

               """
        try:
            self.car.feul=30
            with self.assertRaises(Exception):
                self.car.updateFeul(-5)
            self.logFile.Log(f'Pass (test_updateFeulNegative): with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_updateFeulNegative): {assErr}')

    def test_updateFeulZero(self):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update 0 liter after drive
             :return: pass/failed

               """
        try:
            self.car.feul = 30
            with self.assertRaises(Exception):
                self.car.updateFeul(0)
            self.logFile.Log(f'Pass (test_updateFeulZero): with error raised Exception  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_updateFeulZero): {assErr}')

    def test_updateFeulempty(self):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update empty feul liter after drive
             :return: pass/failed

               """
        try:
            self.car.feul = 0
            with self.assertRaises(Exception):
                self.car.updateFeul(3)
            self.logFile.Log(f'Pass (test_updateFeulempty): with error raised Exception  ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_updateFeulempty): {assErr}')


    def test_updateFeulempty(self):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update feul liter after drive
             :return: pass/failed

               """
        try :
            self.car.feul = 30
            self.car.updateFeul(3)
            self.logFile.Log(f'Pass (test_updateFeulempty): with parameters {self.car.returnFeul()} ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_updateFeulempty): {assErr}')
    #----------------------------------------------
    def test_calcKmPerLiter(self):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if calcKmPerLiter function correctly
             :return: pass/failed

               """
        try:
            self.assertEqual(self.car.calcKmPerLiter(10),1)
            self.logFile.Log(f'Pass (test_calcKmPerLiter): with parameters {self.car.calcKmPerLiter(10)} ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_calcKmPerLiter): {assErr}')

    #------------------------------------------------
    def test_isItPossiboleToDriveEmptyFaul(self):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if isItPossiboleToDrive function return true when the feul is empty
              :return: pass/failed

                """
        try:
            self.car.feul=0
            with self.assertRaises(Exception):
                self.car.isItPossiboleToDrive(10)
            self.logFile.Log(f'Pass (test_isItPossiboleToDriveEmptyFaul): with error raised Exception   ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_isItPossiboleToDriveEmptyFaul): {assErr}')

    def test_isItPossiboleToDrive1(self):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if isItPossiboleToDrive function return true when the feul noe enough is empty
              :return: pass/failed

                """
        try:
            self.car.feul = 5
            with self.assertRaises(Exception):
                 self.car.isItPossiboleToDrive(100)
            self.logFile.Log(f'Pass (test_isItPossiboleToDrive1): with error raised Exception  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_isItPossiboleToDrive1): {assErr}')
    def test_isItPossiboleToDrive(self):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if isItPossiboleToDrive function return true when the feul
              :return: pass/failed

                """
        try:
            self.car.feul=1
            self.car.isItPossiboleToDrive(10)
            self.logFile.Log(f'Pass (test_isItPossiboleToDrive): with parameters {self.car.isItPossiboleToDrive(10)} ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_isItPossiboleToDrive): {assErr}')

    #------------------------------------------
    def test_startDrive_Bystarted(self):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if startDrive function reset the variable starter to 1
              :return: pass/failed

                """
        try:
            self.car.startDrive()
            self.assertEqual(self.car.returnstartMode(), 1)
            self.logFile.Log(f'Pass (test_startDrive_Bystarted): with parameters {self.car.returnstartMode()} ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_startDrive_Bystarted): {assErr}')
    def test_startDrive_ByinDrive(self):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if startDrive function reset the variable inDrive to 1
              :return: pass/failed

                """
        try:
            self.car.startDrive()
            self.assertEqual(self.car.returninDrive(), 1)
            self.logFile.Log(f'Pass (test_startDrive_ByinDrive): with parameters {self.car.returninDrive()} ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_startDrive_ByinDrive): {assErr}')
    #----------------------------------------------
    def test_drive_Bystarter(self):
        """
               name : Liad
               date : 22/01/2023
               :param : none
               function that checks if drive function apply to drive when started is off
               :return: pass/failed

                 """
        try:
            self.car.stopDrive()
            with self.assertRaises(Exception):
                self.car.drive()
            self.logFile.Log(f'Pass (test_drive_Bystarter): with error raised Exception  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_drive_Bystarter): {assErr}')
    def test_driveEmptyFeul(self):
        """
               name : Liad
               date : 22/01/2023
               :param : none
               function that checks if drive function apply to drive when the feul is empty
               :return: pass/failed

                 """
        try:
            self.car.startDrive()
            self.car.feul = 0
            with self.assertRaises(Exception):
                self.car.drive()
            self.logFile.Log(f'Pass (test_driveEmptyFeul): with error raised Exception  ')
        except  AssertionError as assErr:
            self.logFile.Log(f'Failed (test_driveEmptyFeul): {assErr}')

    def test_drive(self):
        """
               name : Liad
               date : 22/01/2023
               :param : none
               function that checks if drive function apply to drive when everything good
               :return: pass/failed

                 """
        try:
            self.car.startDrive()
            self.car.feul=20
            self.car.drive(10)
            self.logFile.Log(f'Pass (test_drive) ')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_drive): {assErr}')

    def test_drive_speed(self):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (speed)
                :return: pass/failed

                  """
        try:
            self.car.startDrive()
            self.car.feul = 20
            self.car.drive(10)
            self.assertEqual(self.car.speed,0)
            self.logFile.Log(f'Pass (test_drive) : with parameters {self.car.returnSpeed()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_drive): {assErr}')
    def test_drive_gear(self):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (gear)
                :return: pass/failed

                  """
        try:
            self.car.startDrive()
            self.car.feul = 20
            self.car.drive(10)
            self.assertEqual(self.car.gear,0)
            self.logFile.Log(f'Pass (test_drive_gear) : with parameters {self.car.returnGear()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_drive_gear): {assErr}')

    def test_drive_feul(self):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (feul)
                :return: pass/failed

                  """
        try:
            self.car.startDrive()
            self.car.feul = 20
            self.car.drive(10)
            self.assertEqual(self.car.feul, 19)
            self.logFile.Log(f'Pass (test_drive_feul) : with parameters {self.car.returnFeul()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_drive_feul): {assErr}')

    def test_drive_starter(self):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (starter)
                :return: pass/failed

                  """
        try:
            self.car.startDrive()
            self.car.feul = 20
            self.car.drive(10)
            self.assertEqual(self.car.starter, 0)
            self.logFile.Log(f'Pass (test_drive_starter) : with parameters {self.car.returnstartMode()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_drive_starter): {assErr}')

    def test_drive_inDrive(self):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if drive function doing stop drive (inDrive)
                 :return: pass/failed

                   """
        try:
            self.car.startDrive()
            self.car.feul = 20
            self.car.drive(10)
            self.assertEqual(self.car.inDrive, 0)
            self.logFile.Log(f'Pass (test_drive_starter) : with parameters {self.car.returninDrive()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_drive_starter): {assErr}')
    #----------------------------------------
    def test_returnSpeed(self):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if returnSpeed function correctly
                 :return: pass/failed

                   """
        try:
            self.car.startDrive()
            self.car.speed=30
            self.assertEqual(self.car.returnSpeed(),30)
            self.logFile.Log(f'Pass (test_returnSpeed) : with parameters {self.car.returnSpeed()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_returnSpeed): {assErr}')
    #-----------------------------------------------
    def test_returnstarter(self):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnstarter function correctly
                   :return: pass/failed

                     """
        try:
            self.car.startDrive()
            self.assertEqual(self.car.returnstartMode(),1)
            self.logFile.Log(f'Pass (test_returnstarter) : with parameters {self.car.returnstartMode()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_returnstarter): {assErr}')
    #-----------------------------------------------
    def test_returninDrive(self):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnIndrive function correctly
                   :return: pass/failed

                     """
        try:
            self.car.startDrive()
            self.assertEqual(self.car.returninDrive(),1)
            self.logFile.Log(f'Pass (test_returninDrive) : with parameters {self.car.returninDrive()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_returninDrive): {assErr}')

    # -----------------------------------------------
    def test_returnGear(self):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnGear function correctly
                   :return: pass/failed

                     """
        try:
            self.car.startDrive()
            self.car.gear=5
            self.assertEqual(self.car.returnGear(), 5)
            self.logFile.Log(f'Pass (test_returnGear) : with parameters {self.car.returnGear()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_returnGear): {assErr}')
    #---------------------------------------------------
    def test_returnFeul(self):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnFeul function correctly
                   :return: pass/failed

                     """
        try:
            self.car.feul = 30
            self.assertEqual(self.car.returnFeul(), 30)
            self.logFile.Log(f'Pass (test_returnFeul) : with parameters {self.car.returnFeul()}')
        except AssertionError as assErr:
            self.logFile.Log(f'Failed (test_returnFeul): {assErr}')







if __name__ == '__main__':
    unittest.main()