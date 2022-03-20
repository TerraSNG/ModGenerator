# #!/usr/bin/python3.8
import os
import sys
from shutil import copyfile
from termcolor import colored

print(colored('''
 
███    ███  ██████  ██████   ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
████  ████ ██    ██ ██   ██ ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██ ████ ██ ██    ██ ██   ██ ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██  ██  ██ ██    ██ ██   ██ ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██      ██  ██████  ██████   ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
                                                                                                         
                                                                                                         
                                                                                                                              
                                                    сделано в Terraria-SNG с <3                                                                               
''','magenta'))

def coderun():
    z = 0
    x = 0
    c = 0
    v = 0
    erz = None
    erx = None
    erc = None
    erv = None

cred()
    try:
        Mn = raw_input("Напишите название мода (Без пробелов и специальных символов!): ")
        Mn = Mn.translate(None, ' \\/":.,><`~!@#$%^&?;*+=')
        if not Mn:
            raise ValueError
        else:
            z = 1
    except ValueError:
        erz = "Название мода"
    
    try:
        Md = raw_input("Напишите имя мода: ")
        if not Md:
            raise ValueError
        else:
            x = 1
    except ValueError:
        erx = "Имя мода"

    try:
        It = raw_input("Название первого предмета (Без пробелов и специальных символов!): ")
        It = It.translate(None, ' \\/":.,><`~!@#$%^&?;*+=')
        if not It:
            raise ValueError
        else:
            c = 1
    except ValueError:
        erc = "Название первого предмета+"
    
