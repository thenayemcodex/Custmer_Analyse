import json,os


def log():
    with open('data.json','r') as log1:
        log2=json.load(log1)
    userid = input("\033[1;31mEnter your id >>   ")
    if (log2["aims"]["id"].get(userid,False)):
        print(log2["aims"]["id"][userid].get("name"))
        print(log2["aims"]["id"][userid].get("post"))
        

    else:
        pass
        print("\033[1;31mUser not found sir \nPlease Register ")
        
        reg()

def reg():
    with open('data.json','r') as log1:
        log2=json.load(log1)
    name=input(' \033[1;32mEnter your Name <<>>  ')
    userid2=input(" \033[1;33mEnter your ID <<>>   ")
    post2=input(" \033[1;34mEnter your post <<>>   ")
    if (log2["aims"]["id"].get(userid2,False)):
        print(" \033[1;31mAlready Exist sir ")
    else:
        log=open("data.json",'r')
        log_read = log.read()
        log_str=(log_read)
        log_cal=len(log_str)
        log_cal2=log_cal-3
        log_array=log_str[:log_cal2]+',"'+userid2+'":{"name":"'+name+'","post":"'+post2+'"}}}}'
        fuck=open('data.json','w')
        fuck.write(str(log_array))
        print("\033[1;31mThank You Sir\n\n \033[;32Run it again *_*\n")
log()
run=input('\033[1;35mDo you want to run again : ')
if run=="yes":
    os.system('python demo.py')
else:
    print('\033[1;36\n<< Thank you for using >>')