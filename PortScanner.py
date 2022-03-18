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

ports = []

for port in ports:
       client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       client.settimeout(0.1)
       code = client.connect_ex((remoteServerIP, port))

       if(code == 0):
              print(port, Fore.GREEN + " Opened" + Style.RESET_ALL)
       else:
              print(port, Fore.RED + " Closed" + Style.RESET_ALL)