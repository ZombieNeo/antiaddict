#noaddiction
from datetime import datetime
now = datetime.now()



#functions
def loop():
    if start == "y":
        print("you started! "+str(now))
        save = open("save.txt","a")
        save.write(str(now))
        save.close()
        pass
    else:
        while True:
            print("ok puss")

    

def start():
    start = input("start? ")
    start.lower()
    loop()
    
    
def current():
    f = open("save.txt","r")
    file_contents =int(f.read())
    print("you started on: ")
    print (int(file_contents))
    now1 =int(datetime.now())
    f.close()
    
def end():
    print("it's ok we all have bad days ")
    print("WIPING STREAK!")
    start()
    

#functions


print("start, current streak or end streak ")
choice = input("state ya purpose ")
choice.lower()
if choice == "start":
    start()
    pass

if choice == "current":
    current()

if choice == "end":
    end()
    
