import threading
import os
from shutil import copy2
import subprocess
import random
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
            print("\n")
            p = subprocess.Popen(["python3","-m","http.server",str(port)], cwd=os.getcwd() +"/host"+str(count)+ "/").pid

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
    except KeyboardInterrupt or TypeError as e:
        os.system("sudo pkill "+str(p))
        for i in range(1,count):
            
            os.system("rm -r "+os.getcwd()+ '/host'+str(i))
            count -= 1
        break
