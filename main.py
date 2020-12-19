import os
from multiprocessing import Pool
from multiprocessing.dummy import freeze_support

processes = ('gui.py', 'spotifyMain.py')


def run_process(process):
    os.system('python ' + process)


if __name__ == '__main__':
    pool = Pool(processes=2)
    freeze_support()
    pool.map(run_process, processes)
    print("done")




class checker:
    def __init__(self):
        pass

    def end(self):
        os.popen("taskkill /f /t /im python.exe")