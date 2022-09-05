import threading
import os
from shutil import copy2
import subprocess
import random
port = random.random() * 10000
port = int(port)
count = 1
def host(f):
    try:
        with open(f) as f:
            global count
            global port
            os.mkdir(os.getcwd() + '/host'+str(count))
            copy2(os.getcwd() +"/" + f.name, os.getcwd() + '/host'+str(count))
            p = subprocess.Popen(["py","-m","http.server",str(port)], cwd=os.getcwd() +"/host"+str(count)+ "/",creationflags =0x08000000).pid

            port = int(random.random() * 10000)
            count += 1
            f.close()
    except FileNotFoundError as err:
        print("File not found")

while True:
    try:
        
        
        filename = input("File Name( Case SensEtive ): ")
        th = threading.Thread(target=host,args=(filename,))
        th.start()
        print("server on http://localhost:" +str(port))
        continue
    except KeyboardInterrupt as e:
        os.system("taskkill /f /im py.exe>nul")
        for i in range(1,count):
            
            os.system("rmdir  /q /s "+os.getcwd()+ '\\host'+str(i))
            count -= 1
        break
