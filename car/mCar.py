from car_class import Car
from dotenv import load_dotenv
from logfile import LogFile

if __name__ == '__main__':
    logFile=LogFile
    try :
        load_dotenv()
        car = Car()
        car.startDrive()
        car.gear=6
        car.addGear()
        car.feul=0
        car.addFeul(60)

    except Exception as e:
        #logFile.Log(str(e))
        print(e)

