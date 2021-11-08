import json,os
try:
  import lolcat
except:
  print("\033[1;36m")
  os.system("pip install lolcat")
  print("\033[1;36m\n[+] lolcat has been installed")
  sleep(1)
try:
  import python3
except:
  
  os.system('apt install python3 -y |lolcat')
  print('"\033[1;36m\n[+] python has been install ')
  sleep(2)
try:
  import figlet
except:
  
  os.system('apt install figlet -y | lolcat')
  print('"\033[1;36m\n[+] figlet has been isntalled ')
  sleep(2)
while True:
    loguser = input('\033[1;35m\n\n[+] Enter Tool Username :')
    sleep(2)
    if loguser == "AIMS":
        print('\033[1;92m\n\n\t[+] Currect ')
        logpas = input('\033[1;91m\n\n[+] Enter Tool Password :')
        sleep(2)
        if logpas == "GROUP":
            print("\033[1;32m\n\n\t[+] Access Granted\n\n[+] Wellcome to <<Noob-Hacker71>> World")
            sleep(1)
            print(usr)
            break
        else:
            print("\033[1;91m \n\n\t[+] Access Denied")
            os.system("xdg-open https://github.com/Noob-hacker71/Custmer_Analyse")
    else:
        print('\033[1;91m\n\n\t[+] Wrong UserName\n\n[+] Try Again',usr,'sir')
        os.system("xdg-open https://github.com/Noob-hacker71/Custmer_Analyse")
        

logo='''\033[1;32m

░█████╗░██╗███╗░░░███╗░██████╗
██╔══██╗██║████╗░████║██╔════╝
███████║██║██╔████╔██║╚█████╗░
██╔══██║██║██║╚██╔╝██║░╚═══██╗
██║░░██║██║██║░╚═╝░██║██████╔╝
╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═════╝░

\033[1;36m
          █▀▀ █▀█ █▀█ █░█ █▀█
          █▄█ █▀▄ █▄█ █▄█ █▀▀       Recycling And Landfill Service (L.L.C)
          ________________________________________________________________
'''

print(logo)
print('\033[1;33m Developer >> Tahsan Nayem [Noob-Programmer]\n\n')
def log():
    with open('data.json','r') as log1:
        log2=json.load(log1)
    userid = input("\033[1;31mEnter your id >>   ")
    if (log2["aims"]["id"].get(userid,False)):
        print('\033[1;31m'+log2["aims"]["id"][userid].get("name"))
        print('\033[1;32m'+log2["aims"]["id"][userid].get("post"))
        

    else:
        pass
        print("\033[1;31mUser not found sir \n\nP ")
        
        Reg=input(' Do you want to Register your Name >> ')
        if Reg=="yes":
            log=open('data.json','r')
            log=json.load(log)
            admin=input(' Enter Adminastration Key >> ')
            if (log["aims"]["id"].get(admin,False)):
                print("Access Granted ")
                reg()
            else:
                print("Access Denied")
                exit()

        else:
            exit()

def reg():
    with open('data.json','r') as log1:
        log2=json.load(log1)
    name=input(' \033[1;32mEnter your Name <<>>  ')
    userid2=input(" \033[1;33m\nEnter your ID <<>>   ")
    post2=input(" \033[1;34m\nEnter your post <<>>   ")
    if (log2["aims"]["id"].get(userid2,False)):
        print(" \033[1;31m\nAlready Exist sir ")
    else:
        log=open("data.json",'r')
        log_read = log.read()
        log_str=(log_read)
        log_cal=len(log_str)
        log_cal2=log_cal-3
        log_array=log_str[:log_cal2]+',"'+userid2+'":{"name":"'+name+'","post":"'+post2+'"}}}}'
        fuck=open('data.json','w')
        fuck.write(str(log_array))
        print("\033[1;31m\n\nThank You Sir\n\n \033[;32Run it again *_*\n")
log()

while True:
    run=input('\033[1;35m\nDo you want to run again : ')
    if run=="yes":
     os.system('python3 demo.py')
    else:
     print('\033[1;36\n<< Thank you for using >>')
     break
