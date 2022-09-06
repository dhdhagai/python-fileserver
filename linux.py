import threading
import os
from shutil import copy2
import subprocess
import random
import time
port = random.random() * 10000
port = int(port)
p = 0
count = 1
def host(f):
    try:
        with open(f) as f:
            global count
            global p
            global port
            os.mkdir(os.getcwd() + '/host'+str(count))
            copy2(os.getcwd() +"/" + f.name, os.getcwd() + '/host'+str(count))
            print(count)
            count += 1
            p = subprocess.call(["sudo","python3","-m","http.server",str(port)], cwd=os.getcwd() +"/host"+str(count-1)+ "/",stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            
            print(count)
            port = int(random.random() * 100000)
            time.sleep(0.9)
            print("File Name( Case SensEtive ): ")
            
            
            f.close()
    except FileNotFoundError or PermissionError as err:
        print("File not found or permission error")
while True:
    try:
        
        
        filename = input("File Name( Case SensEtive ): ")
        th = threading.Thread(target=host,args=(filename,))
        th.start()
        print("server on http://localhost:" +str(port))
        
        continue
    except KeyboardInterrupt or TypeError or PermissionError as e:
        os.system("sudo pkill "+str(p))
        for i in range(1,count):
            
            os.system("rm -r "+os.getcwd()+ '/host'+str(i))
            count -= 1
        break
