#noaddiction
from datetime import datetime
now = datetime.now()



#functions



def retry():
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




def loop():
    save = open("save.txt","a")
    save.write(str(now))
    save.close()
    save = open("save.txt","r")
    file_contents = save.read()
    print("mark the date: "+str(file_contents))
    pass

    

def start():
    print("GOOD LUCK SOLIDER! TriHard 7 ")
    loop()
    
    
def current():
    f = open("save.txt","r")
    file_contents = f.read()
    print("you started on: ")
    print(file_contents)
    f.close()
    
def end():
    print("it's ok we all have bad days ")
    f = open("save.txt","r")
    file_contents = f.read()
    print("you started on: ")
    print(file_contents)
    f.close()
    print("you lost! BETTER LUCK NEXT TIME! ")
    f = open("save.txt","w")
    f.write("LLLLLLL")
    print("WIPING STREAK!")
    retry()
    
    

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
    
