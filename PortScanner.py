import socket
from turtle import bgcolor
import pycolor
from colorama import Fore, Back, Style

print(Fore.LIGHTCYAN_EX + """

 ███▄ ▄███▓ ▄▄▄       ██▀███  ▄████▄  ▒█████    ██████    ▓█████▄ ▓█████  ██▀███  ▓█████  ██ ▄█▀
▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒██▀ ▀█ ▒██▒  ██▒▒██    ▒    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒▓█   ▀  ██▄█▒ 
▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▓█    ▄▒██░  ██▒░ ▓██▄      ░██   █▌▒███   ▓██ ░▄█ ▒▒███   ▓███▄░ 
▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄ ▒▓▓▄ ▄██▒██   ██░  ▒   ██▒   ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄ 
▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒ ▓███▀ ░ ████▓▒░▒██████▒▒   ░▒████▓ ░▒████▒░██▓ ▒██▒░▒████▒▒██▒ █▄
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ░▒ ▒  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░    ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▒ ▓▒
░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░  ▒    ░ ▒ ▒░ ░ ░▒  ░ ░    ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░ ░ ░  ░░ ░▒ ▒░
░      ░     ░   ▒     ░░   ░░       ░ ░ ░ ▒  ░  ░  ░      ░ ░  ░    ░     ░░   ░    ░   ░ ░░ ░ 
       ░         ░  ░   ░    ░ ░         ░ ░        ░        ░       ░  ░   ░        ░  ░░  ░   
                             ░                             ░                                    

""" + Style.RESET_ALL)

remoteServer = input("Enter the ip address: ")
remoteServerIP = socket.gethostbyname(remoteServer)

ports = [20, 21, 22, 23, 42, 43, 43, 69, 80, 109, 110, 115, 118, 143,
       156, 220, 389, 443, 465, 513, 514, 530, 547, 587, 636, 873,
       989, 990, 992, 993, 995, 1433, 1521, 2049, 2081, 2083, 2086,
       3306, 3389, 5432, 5500, 5800]

for port in ports:
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.settimeout(0.1)
       code = client.connect_ex((remoteServerIP, port))

       if(code == 0):
              print(port, Fore.GREEN + " Opened" + Style.RESET_ALL)
       else:
              print(port, Fore.RED + " Closed" + Style.RESET_ALL)