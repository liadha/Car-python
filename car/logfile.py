import os
import datetime


class LogFile:
    def Log(mes):
        """this function write output into the log file"""
        os.chdir("C:\\Python")
        if not os.path.exists('log.txt'):
                file = open('log.txt', 'x')
        else:
             file = open('log.txt', 'a')
        file.write(mes+" ---> "+str(datetime.datetime.now())+"\n")
        file.flush()
        file.close()