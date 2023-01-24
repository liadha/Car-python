import pytest
from car.car_class import Car
from dotenv import load_dotenv
from car.logfile import LogFile
import os


@pytest.fixture
def mycar():
    load_dotenv()
    logFile = LogFile
    return Car()
@pytest.mark.one
def test_stopDrive_BySpeed(mycar):
    """
         name : Liad
         date : 22/01/2023
         :param : none
         function that checks if stopDrive function resets speed
         :return: pass/failed
         """
    try:
        mycar.stopDrive()
        assert mycar.returnSpeed() == 0
        mycar.logFile.Log(f'Pass (test_stopDrive_BySpeed): with parameters {mycar.returnSpeed()}  ')
    except AssertionError as assErr:
        mycar.logFile.Log(f'Failed (test_stopDrive_BySpeed): {assErr}')


def test_stopDriveGear(mycar):
        """
            name : Liad
            date : 22/01/2023
            :param : none
            function that checks if stopDrive function resets the gear
            :return: pass/failed
            """
        try:
            mycar.stopDrive()
            assert mycar.returnGear() == 0
            mycar.logFile.Log(f'Pass (test_stopDrive_ByGear): with parameters {mycar.returnGear()}  ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_stopDrive_ByGear): {assErr}')

def test_stopDrive_ByStartter(mycar):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if stopDrive function resets the starter
                 :return: pass/failed
                 """
        try:
            mycar.stopDrive()
            assert mycar.returnstartMode() == 0
            mycar.logFile.Log(f'Pass (test_stopDrive_ByStartter): with parameters {mycar.returnstartMode()}  ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_stopDrive_ByStartter): {assErr}')

def test_stopDrive_ByInDrive(mycar):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if stopDrive function resets the inDrive variable
                 :return: pass/failed
                 """
        try:
            mycar.stopDrive()
            assert mycar.returninDrive() == 0
            mycar.logFile.Log(f'Pass (test_stopDrive_ByInDrive): with parameters {mycar.returninDrive()} ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_stopDrive_ByInDrive): {assErr}')
#---------------------------------------------------------
def test_addSpeed_0(mycar):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if addSpeed function add 0 speed
        :return: pass/failed

                        """
        try:
            mycar.startDrive()
            with pytest.raises (Exception):
                mycar.addSpeed(0)
            mycar.logFile.Log(f'Pass (test_addSpeed_0): with error raised Exception   ')
        except AssertionError as assErr:
                mycar.logFile.Log(f'Failed (test_addSpeed_0): {assErr}')
def test_addSpeed_Negative(mycar):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if addSpeed function add negative speed
        :return: pass/failed
          """
        try:
            mycar.startDrive()
            with pytest.raises (Exception):
                mycar.addSpeed(-5)
            mycar.logFile.Log(f'Pass (test_addSpeed_Negative): with error raised Exception   ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_addSpeed_Negative): {assErr}')
def test_addSpeedStarterFalse(mycar):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if addSpeed function add speed when the started is off
        :return: pass/failed
          """
        try:
            mycar.stopDrive()
            with pytest.raises (Exception):
                mycar.addSpeed(20)
            mycar.logFile.Log(f'Pass (test_addSpeedStartModeFalse): with error raised Exception   ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_addSpeedStartModeFalse): {assErr}')
def test_addSpeedStarterTrue(mycar):
    """
     name : Liad
     date : 22/01/2023
     :param : none
     function that checks if addSpeed function add speed when the started is on
     :return: pass/failed
       """
    try:
            mycar.startDrive()
            mycar.addSpeed(20)
            mycar.logFile.Log(f'Pass (test_addSpeedStarterTrue): with parameters {mycar.returnSpeed()}  ')
    except  AssertionError as assErr:
        mycar.logFile.Log(f'Failed (test_addSpeedStarterTrue): {assErr}')
 #----------------------------------------------------
def test_subSpeedStarter(mycar):
        """
        name : Liad
        date : 22/01/2023
        :param : none
        function that checks if subSpeed function Reduces speed when the started is off
        :return: pass/failed
          """
        try:
            mycar.stopDrive()
            mycar.speed=5
            with pytest.raises(Exception):
                mycar.addSpeed(20)
            mycar.logFile.Log(f'Pass (test_subSpeedStarter): with error raised Exception  ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_subSpeedStarter): {assErr}')

def test_subSpeed(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subSpeed function Reduces speed
           :return: pass/failed

             """
        try :
            mycar.startDrive()
            mycar.addSpeed(10)
            mycar.subSpeed(5)
            assert mycar.returnSpeed() == 5
            mycar.logFile.Log(f'Pass (test_subSpeed): with parameters {mycar.returnSpeed()}  ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_subSpeed): {assErr}')



def test_subSpeedNegative(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subSpeed function Reduces negative speed
           :return: pass/failed

             """
        try :
            mycar.startDrive()
            mycar.speed = 20
            with pytest.raises (Exception):
                mycar.subSpeed(-5)
            mycar.logFile.Log(f'Pass (test_subSpeedNegative):: with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_subSpeedNegative): {assErr}')
#---------------------------------------------------------
def test_addGear_starter(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addGear function turn on gear when the starter is off
           :return: pass/failed

             """
        try:
            mycar.stopDrive()
            with pytest.raises (Exception):
                mycar.addGear()
            mycar.logFile.Log(f'Pass (test_addGear_starter): with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_addGear_starter): {assErr}')
def test_addGear_moreThanMax(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addGear function turn on gear more than 6
           :return: pass/failed

             """
        try:
            mycar.startDrive()
            for i in range(int(os.getenv('max_gear'))):
                mycar.addGear()
            with pytest.raises (Exception):
                 mycar.addGear()
            mycar.logFile.Log(f'Pass (test_addGear_moreThanMax): with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_addGear_moreThanMax): {assErr}')
def test_addGear(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addGear function turn on gear
           :return: pass/failed

             """
        try:
            mycar.startDrive()
            for i in range(3):
                mycar.addGear()
            mycar.logFile.Log(f'Pass (test_addGear): with parameters {mycar.returnGear()} ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_addGear): {assErr}')
#----------------------------------------------------
def test_subGear_0(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the current gear is 0
           :return: pass/failed

             """
        try:
            mycar.startDrive()
            with pytest.raises (Exception):
                 mycar.subGear()
            mycar.logFile.Log(f'Pass (test_subGear_0): with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_subGear_0): {assErr}')

def test_subGearStarter(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the starter is off
           :return: pass/failed

             """
        try:
            mycar.stopDrive()
            with pytest.raises (Exception):
                mycar.subGear()
            mycar.logFile.Log(f'Pass (test_subGearStarter): with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_subGearStarter): {assErr}')
def test_subGearWith0Speed(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the speed is 0
           :return: pass/failed

             """
        try :
            mycar.startDrive()
            mycar.gear = 2
            with pytest.raises (Exception):
                mycar.subGear()
            mycar.logFile.Log(f'Pass (test_subGearWith0Speed): with error raised Exception  ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_subGearWith0Speed): {assErr}')

def test_subGearWithSpeed(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if subGear function turn off gear when the speed
           :return: pass/failed

             """
        try :
            mycar.startDrive()
            mycar.gear = 2
            mycar.addSpeed(15)
            mycar.subGear()
            mycar.logFile.Log(f'Pass (test_subGearWithSpeed): with parameters {mycar.returnGear()} ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_subGearWithSpeed): {assErr}')
def test_subGear1(mycar):
    """
         name : Liad
         date : 22/01/2023
         :param : none
         function that checks if subGear function turn off gear when the gear on 1
         :return: pass/failed

           """
    try:
        mycar.startDrive()
        mycar.gear = 1
        assert mycar.speed == 0
        mycar.logFile.Log(f'Pass (test_subGear1): with parameters {mycar.returnSpeed()} ')
    except  AssertionError as assErr:
        mycar.logFile.Log(f'Failed (test_subGear1): {assErr}')
    #-------------------------------------------

def test_addFeul_ByMaxFeulLiter(mycar):
        """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if addFeul function allows to fill more than allowed
           :return: pass/failed

             """
        try:
            with pytest.raises (Exception):
                mycar.addFeul(100)
            mycar.logFile.Log(f'Pass (test_addFeul_ByMaxFeulLiter): with error raised Exception  ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_addFeul_ByMaxFeulLiter): {assErr}')

def test_addFeu_BylMaxPrice(mycar):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if addFeul function allows to fill more than max price
             :return: pass/failed

               """
        try:
            mycar.maxPrice=20
            with pytest.raises (Exception):
                mycar.addFeul(30)
            mycar.logFile.Log(f'Pass (test_addFeu_BylMaxPrice): with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_addFeu_BylMaxPrice): {assErr}')

#----------------------------------------------------
def test_updateFeulNegative(mycar):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update negative liter after drive
             :return: pass/failed

               """
        try:
            mycar.feul=30
            with pytest.raises (Exception):
                mycar.updateFeul(-5)
            mycar.logFile.Log(f'Pass (test_updateFeulNegative): with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_updateFeulNegative): {assErr}')

def test_updateFeulZero(mycar):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update 0 liter after drive
             :return: pass/failed

               """
        try:
            mycar.feul = 30
            with pytest.raises (Exception):
                mycar.updateFeul(0)
            mycar.logFile.Log(f'Pass (test_updateFeulZero): with error raised Exception  ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_updateFeulZero): {assErr}')
def test_updateFeulempty(mycar):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update empty feul liter after drive
             :return: pass/failed

               """
        try:
            mycar.feul = 0
            with pytest.raises (Exception):
                mycar.updateFeul(3)
            mycar.logFile.Log(f'Pass (test_updateFeulempty): with error raised Exception  ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_updateFeulempty): {assErr}')
@pytest.mark.skip
def test_updateFeulempty(mycar):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if updateFeul function update feul liter after drive
             :return: pass/failed

               """
        try :
            mycar.feul = 30
            mycar.updateFeul(3)
            mycar.logFile.Log(f'Pass (test_updateFeulempty): with parameters {mycar.returnFeul()} ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_updateFeulempty): {assErr}')
#----------------------------------------------
def test_calcKmPerLiter(mycar):
        """
             name : Liad
             date : 22/01/2023
             :param : none
             function that checks if calcKmPerLiter function correctly
             :return: pass/failed
           """
        try:
            assert mycar.calcKmPerLiter(10) == 50
            mycar.logFile.Log(f'Pass (test_calcKmPerLiter): with parameters {mycar.calcKmPerLiter(10)} ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_calcKmPerLiter) actual val : 50 except val : {mycar.calcKmPerLiter(10)}')
    #------------------------------------------------
def test_isItPossiboleToDriveEmptyFaul(mycar):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if isItPossiboleToDrive function return true when the feul is empty
              :return: pass/failed

                """
        try:
            mycar.feul=0
            with pytest.raises (Exception):
                mycar.isItPossiboleToDrive(50)
            mycar.logFile.Log(f'Pass (test_isItPossiboleToDriveEmptyFaul): with error raised Exception   ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_isItPossiboleToDriveEmptyFaul): {assErr}')

def test_isItPossiboleToDrive1(mycar):
    """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if isItPossiboleToDrive function return true when the feul noe enough is empty
           :return: pass/failed

             """
    try:
        mycar.feul = 5
        with pytest.raises (Exception):
            mycar.isItPossiboleToDrive(100)
        mycar.logFile.Log(f'Pass (test_isItPossiboleToDrive1): with error raised Exception  ')
    except  AssertionError as assErr:
        mycar.logFile.Log(f'Failed (test_isItPossiboleToDrive1): {assErr}')
def test_isItPossiboleToDrive(mycar):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if isItPossiboleToDrive function return true when the feul
              :return: pass/failed

                """
        try:
            mycar.feul=1
            mycar.isItPossiboleToDrive(10)
            mycar.logFile.Log(f'Pass (test_isItPossiboleToDrive): with parameters {mycar.isItPossiboleToDrive(10)} ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_isItPossiboleToDrive): {assErr}')
    #------------------------------------------
def test_startDrive_Bystarted(mycar):
        """
              name : Liad
              date : 22/01/2023
              :param : none
              function that checks if startDrive function reset the variable starter to 1
              :return: pass/failed

                """
        try:
            mycar.startDrive()
            assert mycar.returnstartMode() == 1
            mycar.logFile.Log(f'Pass (test_startDrive_Bystarted): with parameters {mycar.returnstartMode()} ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_startDrive_Bystarted): {assErr}')
def test_startDrive_ByinDrive(mycar):
    """
           name : Liad
           date : 22/01/2023
           :param : none
           function that checks if startDrive function reset the variable inDrive to 1
           :return: pass/failed

             """
    try:
        mycar.startDrive()
        assert mycar.returninDrive() == 1
        mycar.logFile.Log(f'Pass (test_startDrive_ByinDrive): with parameters {mycar.returninDrive()} ')
    except AssertionError as assErr:
        mycar.logFile.Log(f'Failed (test_startDrive_ByinDrive): {assErr}')
#----------------------------------------------
def test_drive_Bystarter(mycar):
        """
               name : Liad
               date : 22/01/2023
               :param : none
               function that checks if drive function apply to drive when started is off
               :return: pass/failed

                 """
        try:
            mycar.stopDrive()
            with pytest.raises (Exception):
                mycar.drive()
            mycar.logFile.Log(f'Pass (test_drive_Bystarter): with error raised Exception  ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_drive_Bystarter): {assErr}')
def test_driveEmptyFeul(mycar):
        """
               name : Liad
               date : 22/01/2023
               :param : none
               function that checks if drive function apply to drive when the feul is empty
               :return: pass/failed

                 """
        try:
            mycar.startDrive()
            mycar.feul = 0
            with pytest.raises(Exception):
                mycar.drive()
            mycar.logFile.Log(f'Pass (test_driveEmptyFeul): with error raised Exception  ')
        except  AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_driveEmptyFeul): {assErr}')
def test_drive(mycar):
        """
               name : Liad
               date : 22/01/2023
               :param : none
               function that checks if drive function apply to drive when everything good
               :return: pass/failed

                 """
        try:
            mycar.startDrive()
            mycar.feul=20
            mycar.drive(10)
            mycar.logFile.Log(f'Pass (test_drive) ')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_drive): {assErr}')

def test_drive_speed(mycar):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (speed)
                :return: pass/failed

                  """
        try:
            mycar.startDrive()
            mycar.feul = 20
            mycar.drive(10)
            assert mycar.speed == 0
            mycar.logFile.Log(f'Pass (test_drive) : with parameters {mycar.returnSpeed()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_drive): {assErr}')
def test_drive_gear(mycar):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (gear)
                :return: pass/failed

                  """
        try:
            mycar.startDrive()
            mycar.feul = 20
            mycar.drive(10)
            assert mycar.gear == 0
            mycar.logFile.Log(f'Pass (test_drive_gear) : with parameters {mycar.returnGear()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_drive_gear): {assErr}')

def test_drive_feul(mycar):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (feul)
                :return: pass/failed

                  """
        try:
            mycar.startDrive()
            mycar.feul = 20
            mycar.drive(10)
            assert mycar.feul == 19
            mycar.logFile.Log(f'Pass (test_drive_feul) : with parameters {mycar.returnFeul()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_drive_feul): {assErr}')

def test_drive_starter(mycar):
        """
                name : Liad
                date : 22/01/2023
                :param : none
                function that checks if drive function doing stop drive (starter)
                :return: pass/failed

                  """
        try:
            mycar.startDrive()
            mycar.feul = 20
            mycar.drive(10)
            assert mycar.starter == 0
            mycar.logFile.Log(f'Pass (test_drive_starter) : with parameters {mycar.returnstartMode()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_drive_starter): {assErr}')
def test_drive_inDrive(mycar):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if drive function doing stop drive (inDrive)
                 :return: pass/failed

                   """
        try:
            mycar.startDrive()
            mycar.feul = 20
            mycar.drive(10)
            assert mycar.inDrive == 0
            mycar.logFile.Log(f'Pass (test_drive_starter) : with parameters {mycar.returninDrive()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_drive_starter): {assErr}')
    #----------------------------------------
def test_returnSpeed(mycar):
        """
                 name : Liad
                 date : 22/01/2023
                 :param : none
                 function that checks if returnSpeed function correctly
                 :return: pass/failed

                   """
        try:
            mycar.startDrive()
            mycar.speed=30
            assert mycar.returnSpeed() == 30
            mycar.logFile.Log(f'Pass (test_returnSpeed) : with parameters {mycar.returnSpeed()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_returnSpeed): {assErr}')
    #-----------------------------------------------
def test_returnstarter(mycar):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnstarter function correctly
                   :return: pass/failed

                     """
        try:
            mycar.startDrive()
            assert mycar.returnstartMode() == 1
            mycar.logFile.Log(f'Pass (test_returnstarter) : with parameters {mycar.returnstartMode()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_returnstarter): {assErr}')
    #-----------------------------------------------
def test_returninDrive(mycar):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnIndrive function correctly
                   :return: pass/failed

                     """
        try:
            mycar.startDrive()
            assert mycar.returninDrive() == 1
            mycar.logFile.Log(f'Pass (test_returninDrive) : with parameters {mycar.returninDrive()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_returninDrive): {assErr}')

    # -----------------------------------------------
def test_returnGear(mycar):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnGear function correctly
                   :return: pass/failed

                     """
        try:
            mycar.startDrive()
            mycar.gear=5
            assert mycar.returnGear() == 5
            mycar.logFile.Log(f'Pass (test_returnGear) : with parameters {mycar.returnGear()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_returnGear): {assErr}')
    #---------------------------------------------------
def test_returnFeul(mycar):
        """
                   name : Liad
                   date : 22/01/2023
                   :param : none
                   function that checks if returnFeul function correctly
                   :return: pass/failed

                     """
        try:
            mycar.feul = 30
            assert mycar.returnFeul() == 30
            mycar.logFile.Log(f'Pass (test_returnFeul) : with parameters {mycar.returnFeul()}')
        except AssertionError as assErr:
            mycar.logFile.Log(f'Failed (test_returnFeul): {assErr}')




